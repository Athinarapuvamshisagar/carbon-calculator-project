# carbon-calculator-project
streamlit app to calculate an individuals  carbon food print 

# Project Report: Carbon Emission Calculator

**STUDENT:**Vamshi (Athinarapuvamshisagar)
**Project:** Carbon Emission Calculator
**Theme:** Sustainability
**Week:** 2 of 4
**Date:** 09/11/2025

-----

## **Weekly Focus: Week 2 - Core Model Development & Data Integration**

# 1. Objective

The primary objective for Week 2 was to transition from the research and planning phase (Week 1) to a functional, code-based solution. The goal was to build the core "engine" or "model" of the calculator—a robust, testable, and separate Python module capable of performing all the necessary carbon footprint calculations.

# 2. Tasks Completed

1.  **Architecture Design:** Architected the project into three distinct parts for scalability and maintainability:
      * `app.py`: The user interface (UI) and web dashboard.
      * `calculator.py`: The core calculation engine (the "model").
      * `factors.json`: A centralized database for all emission factors.
2.  **Data File Creation:** Created the `factors.json` file to store all emission factors (e.g., kg CO2e per kWh) as a structured JSON object. This separation means we can update factors without changing the application code.
3.  **Model Development:** Wrote the complete `calculator.py` module. This module contains two essential functions:
      * `load_emission_factors(file_path)`: A function to read and parse the `factors.json` file.
      * `calculate_footprint(inputs, factors)`: The main engine function. It takes user inputs (as a dictionary) and the loaded factors, then returns the total emissions and a detailed breakdown by category.
4.  **Integration & Testing:** Integrated the new `calculator.py` module into the main `app.py` file. The web app now calls the engine to perform its calculations, receives the results, and displays them.
5.  **Initial Validation:** Performed unit testing on the `calculator.py` module to ensure its mathematical accuracy before connecting it to the UI.

# 3. Core Model Architecture

The project now follows a modern, 3-tier structure. This separation is a best practice in software development.

  * **`app.py` (View):** The user-facing part, built with Dash. Its only job is to get inputs and show results.
  * **`calculator.py` (Controller/Logic):** The "brains" of the operation. It knows nothing about the UI. It just receives data, performs calculations, and returns results.
  * **`factors.json` (Data):** The "database." It stores all the scientific data in one place, making it easy to manage.

# 4. Data Integration (`factors.json`)

A structured JSON file was created to act as a database for our emission factors.

**Sample Structure:**

```json
{
  "electricity": {
    "factor": 0.37,
    "unit": "kg CO2e per kWh"
  },
  "natural_gas": {
    "factor": 5.3,
    "unit": "kg CO2e per therm"
  },
  "gasoline_car": {
    "factor": 0.40,
    "unit": "kg CO2e per mile"
  },
  "diet": {
    "avg": 180,
    "veg": 120,
    "vegan": 90
  }
}
```

**Justification:** Using an external JSON file allows the application to be more flexible. If a new, more accurate emission factor for electricity is released, we can update the `factors.json` file without needing to re-write or stop the main application code.

# 5. Week 2 Deliverables

  * **`calculator.py`:** A complete, documented, and testable Python module that handles all business logic for carbon calculation.
  * **`factors.json`:** A structured data file containing the. initial set of emission factors for electricity, natural gas, transportation, and diet.
  * **Updated `app.py`:** A functional web application that successfully imports and utilizes the `calculator.py` module to produce a correct, data-driven output (Total emissions + Pie Chart).

**Conclusion:** Week 2 successfully concludes the development of the core logic. The project is no longer just a plan; it is a functional, data-driven application with a scalable architecture. The focus for Week 3 will be to enhance the "Analysis" and "Suggestions" part of the app.
