
# Task 4: A Dashboard with Dash
# Ok, deep breath.  Start by copying python-assignment11\assignment11\lesson11_c.py to python-assignment11\myapp.py.
# We can reuse the template.  This is in the root of the project folder because you are going to deploy this to the cloud in Task 5.

# The dataset to use is the Plotly built in gapminder dataset. This has, among other things, 
# the per capita GDP for various countries for each year. For a given country, there will be one row per year. 
# This means that the 'countries' column has many duplicates.
# You want a dropdown that has each unique country name. You create a Series called countries that is 
# the list of countries with duplicates removed. You use this Series to populate the dropdown. Give the dropdown the initial value of 'Canada'.
# You give the dropdown the id of 'country-dropdown' and also create a dcc.Graph with id 'gdp-growth'.
# You create the decorator for the callback, associating the input with the dropdown and the output with the graph.
# The decorator decorates an update_graph() function. This is passed the country name as a parameter. 
# You need to filter the dataset to get only the rows where the country column matches this name. 
# Then you create a line plot for 'year' vs. 'gdpPercap`. 
# Give the plot a descriptive name that includes the country name.
# The line to run the app doesn't need to change.
# Run the program, and check it out in the browser. Make bug fixes as needed.
# Building Dashboard with Dash

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas')


# Initialize Dash app
app = Dash(__name__)

countries = df['country'].drop_duplicates()

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    country_df = df[df['country']==country]
    fig = px.line(country_df, x="year", y="gdpPercap", title=f"{country} Per Capita GDP")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 