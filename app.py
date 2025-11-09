# CELL 4: Run the main Dash app (Corrected Code)
import dash
from dash import Dash, dcc, html  # <-- Import Dash from dash
from dash.dependencies import Input, Output, State
import calculator
import plotly.graph_objects as go
import pandas as pd

factors = calculator.load_emission_factors("factors.json")

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']) # <-- Use Dash()
app.title = "Carbon Calculator"

app.layout = html.Div(children=[
    html.H1(children='🌱 Carbon Footprint Calculator', style={'textAlign': 'center'}),
    html.P("Enter your monthly data below to estimate your footprint.", style={'textAlign': 'center'}),
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            html.H3("🏡 Home Energy"),
            html.Label("Monthly electricity used (in kWh):"),
            dcc.Input(id='kwh-input', value=0, type='number'),
            html.Label("Monthly natural gas used (in therms):"),
            dcc.Input(id='therms-input', value=0, type='number'),
            html.H3("🚗 Transportation"),
            html.Label("Monthly miles driven (petrol car):"),
            dcc.Input(id='miles-car-input', value=0, type='number'),
            html.Label("Monthly miles flown:"),
            dcc.Input(id='miles-flights-input', value=0, type='number'),
            html.H3("🍽️ Consumption"),
            html.Label("Primary diet:"),
            dcc.Dropdown(
                id='diet-input',
                options=[
                    {'label': 'Average / Meat-Eater', 'value': 'Average / Meat-Eater'},
                    {'label': 'Vegetarian', 'value': 'Vegetarian'},
                    {'label': 'Vegan', 'value': 'Vegan'}
                ],
                value='Average / Meat-Eater'
            ),
            html.Button('Calculate Footprint', id='calculate-button', n_clicks=0, style={'marginTop': '20px'})
        ]),
        html.Div(className='six columns', children=[
            html.H2("Your Results", style={'textAlign': 'center'}),
            html.Div(id='output-total-div'),
            dcc.Graph(id='output-pie-chart')
        ])
    ])
], style={'padding': '20px'})

@app.callback(
    [Output('output-total-div', 'children'),
     Output('output-pie-chart', 'figure')],
    [Input('calculate-button', 'n_clicks')],
    [State('kwh-input', 'value'),
     State('therms-input', 'value'),
     State('miles-car-input', 'value'),
     State('miles-flights-input', 'value'),
     State('diet-input', 'value')]
)
def update_output(n_clicks, kwh, therms, miles_car, miles_flights, diet):
    if n_clicks == 0:
        empty_fig = go.Figure()
        empty_fig.update_layout(title="Your breakdown will appear here", title_x=0.5)
        return html.H3("Click 'Calculate' to see your total.", style={'textAlign': 'center'}), empty_fig

    user_inputs = {
        "kwh": float(kwh), "therms": float(therms),
        "miles_car": float(miles_car), "miles_flights": float(miles_flights),
        "diet": diet
    }

    results, df = calculator.calculate_footprint(user_inputs, factors)

    if results is None:
        return html.H3("An error occurred.", style={'color': 'red'}), dash.no_update

    total_emissions = results["total_emissions"]
    total_output = html.H3(
        f"Total: {total_emissions:,.2f} kg CO2e",
        style={'textAlign': 'center', 'color': '#1f77b4'}
    )

    pie_fig = go.Figure(data=[
        go.Pie(
            labels=df['Category'],
            values=df['Emissions (kg CO2e)'],
            hole=.3
        )
    ])
    pie_fig.update_layout(title="Your Footprint Breakdown", title_x=0.5)
    return total_output, pie_fig

# Run the app and print the link
print("Your app is ready! Click the link below to open it:")
app.run(jupyter_mode="external") # <-- Use app.run()
