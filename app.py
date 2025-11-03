import streamlit as st

# --- 1. SET UP THE PAGE ---
# Set the page title and add a header
st.set_page_config(page_title="Carbon Calculator", layout="wide")
st.title("🌱 My Carbon Emission Calculator")
st.write("Enter your consumption data below to estimate your monthly carbon footprint.")

# --- 2. DEFINE EMISSION FACTORS ---
# These are the "magic numbers" from our Week 1 research (in kg CO2e)
# We can add more to this dictionary later
EMISSION_FACTORS = {
    "electricity": 0.37,  # kg CO2e per kWh
    "natural_gas": 5.3,   # kg CO2e per therm
    "gasoline_car": 0.40, # kg CO2e per mile
    "flights": 0.13,      # kg CO2e per passenger-mile
    # Simple diet estimates (per month) - these are very rough!
    "diet_avg": 180,      # Average/Meat-Eater (kg CO2e)
    "diet_veg": 120,      # Vegetarian (kg CO2e)
    "diet_vegan": 90      # Vegan (kg CO2e)
}

# --- 3. GET USER INPUTS (The UI) ---
# Use columns to organize the layout
col1, col2 = st.columns(2)

with col1:
    st.header("🏡 Home Energy")
    # Get number inputs from the user
    kwh_electricity = st.number_input("Monthly electricity used (in kWh):", min_value=0.0, step=1.0)
    therms_gas = st.number_input("Monthly natural gas used (in therms):", min_value=0.0, step=1.0)

with col2:
    st.header("🚗 Transportation")
    miles_car = st.number_input("Monthly miles driven (in a petrol car):", min_value=0.0, step=1.0)
    miles_flights = st.number_input("Monthly miles flown (on planes):", min_value=0.0, step=1.0)

# Input for consumption
st.header("🍽️ Consumption")
diet_choice = st.selectbox("What is your primary diet?", 
                           ("Average / Meat-Eater", "Vegetarian", "Vegan"))


# --- 4. THE CALCULATION LOGIC ---
# This section will run when the user clicks the button
if st.button("Calculate My Footprint"):
    
    # Calculate emissions for each category
    electricity_emissions = kwh_electricity * EMISSION_FACTORS["electricity"]
    gas_emissions = therms_gas * EMISSION_FACTORS["natural_gas"]
    car_emissions = miles_car * EMISSION_FACTORS["gasoline_car"]
    flight_emissions = miles_flights * EMISSION_FACTORS["flights"]
    
    # Get diet emissions
    if diet_choice == "Average / Meat-Eater":
        diet_emissions = EMISSION_FACTORS["diet_avg"]
    elif diet_choice == "Vegetarian":
        diet_emissions = EMISSION_FACTORS["diet_veg"]
    else:
        diet_emissions = EMISSION_FACTORS["diet_vegan"]

    # Calculate total
    total_emissions = electricity_emissions + gas_emissions + car_emissions + flight_emissions + diet_emissions

    # --- 5. DISPLAY THE RESULTS ---
    st.success(f"Your estimated total monthly footprint is: **{total_emissions:,.2f} kg CO2e**")
    
    st.subheader("Your Footprint Breakdown:")
    # (Week 3 task will be to add a pie chart here)
    st.write(f"* **Home Energy:** {electricity_emissions + gas_emissions:,.2f} kg")
    st.write(f"* **Transportation:** {car_emissions + flight_emissions:,.2f} kg")
    st.write(f"* **Diet:** {diet_emissions:,.2f} kg")

    st.subheader("💡 Your Personalized Suggestion:")
    # (Week 3 task will be to make this logic smarter)
    st.info("Based on your data, a great place to start reducing is by looking at your home energy use.")