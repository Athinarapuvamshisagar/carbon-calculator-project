# CELL 3: Create calculator.py
%%writefile calculator.py
import json
import pandas as pd

def load_emission_factors(file_path="factors.json"):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading factors: {e}")
        return None

def calculate_footprint(inputs, factors):
    try:
        electricity_emissions = inputs["kwh"] * factors["electricity"]["factor"]
        gas_emissions = inputs["therms"] * factors["natural_gas"]["factor"]
        car_emissions = inputs["miles_car"] * factors["gasoline_car"]["factor"]
        flight_emissions = inputs["miles_flights"] * factors["flights"]["factor"]

        if inputs["diet"] == "Average / Meat-Eater": diet_emissions = factors["diet"]["avg"]
        elif inputs["diet"] == "Vegetarian": diet_emissions = factors["diet"]["veg"]
        else: diet_emissions = factors["diet"]["vegan"]

        total_energy = electricity_emissions + gas_emissions
        total_transport = car_emissions + flight_emissions
        total_emissions = total_energy + total_transport + diet_emissions

        results = {
            "total_emissions": total_emissions,
            "breakdown": {
                "Home Energy": total_energy,
                "Transportation": total_transport,
                "Diet": diet_emissions
            }
        }

        breakdown_df = pd.DataFrame(
            list(results["breakdown"].items()),
            columns=['Category', 'Emissions (kg CO2e)']
        )
        return results, breakdown_df
    except Exception as e:
        print(f"Error in calculation: {e}")
        return None, None
