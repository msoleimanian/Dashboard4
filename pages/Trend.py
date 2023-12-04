import streamlit as st
import warnings

warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")


def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth2(title, context):
    return f"""
        <div class="jumbotron">
        <h2>{title}</h2>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """


st.markdown(printCostumTitleAndContenth1("Trend" , "In this section, the trend of plant traits and nutrients is displayed") , unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import plotly.express as px
import io

# Your CSV data
csv_data = """
Season,Plot Number,Plant Height,No. of Tiller,No. of Panicle,SPAD,No. of Spikelet,No. of Filled Grain,No. Of Unfilled Grain,Weight Grain (1000 grains)
Season 1,Plot1,98.51,6,5,28.48,42,195,154,26.27
Season 1,Plot3,98,5,5,26.35,35,122,155,24.26
Season 1,Plot4,93.2,5,4,28.81,27,137,46,25.95
Season 1,Plot5,93.99,7,5,32.22,35,150,163,23.25
Season 2,Plot1,103.16,5,5,0,38,188,271,33.31
Season 2,Plot3,98.75,5,5,0,38,803,250,31.01
Season 2,Plot4,88.8,4,4,0,30,643,343,30.55
Season 2,Plot5,92.07,5,5,0,37,662,290,33.46
Season 3,Plot1,100.16,5,5,0,41,84,16,33.19
Season 3,Plot3,96.95,5,4,0,41,84,16,31.43
Season 3,Plot4,88.17,3,4,0,30,86,14,26.2
Season 3,Plot5,93.98,4,4,0,37,82,5,24.23
"""

# Create a DataFrame from CSV data
df = pd.read_csv(io.StringIO(csv_data))

# List of traits to plot
traits = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'SPAD', 'No. of Spikelet', 'No. of Filled Grain', 'No. Of Unfilled Grain', 'Weight Grain (1000 grains)']

# Streamlit App
st.title('Trait Analysis across Seasons and Plots')

for selected_trait in traits:
# Plot grouped bar chart using Plotly Express
    fig = px.bar(df, x='Season', y=selected_trait, color='Plot Number',
                 barmode='group',
                 title=f'{selected_trait} across Seasons for different Plots',
                 labels={'Season': 'Season', selected_trait: f'{selected_trait}', 'Plot Number': 'Plot'})

    # Display the plot using st.plotly_chart
    st.plotly_chart(fig)

# Additional information
st.write("Note: Each group represents a season, and each bar within the group represents a plot.")











