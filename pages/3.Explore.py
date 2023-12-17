import streamlit as st
import time
import numpy as np
import pandas as pd
import time
import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.express as px
import io




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


def animated_linear_progress_bar(label, value, color='green'):
    progress_html = f"""
        <svg width="300" height="30" style="background-color: #f1f1f1; border-radius: 5px;">
            <rect id="progress-rect" width="0%" height="100%" fill="{color}">
                <animate attributeName="width" from="0%" to="{value}%" dur="2s" fill="freeze" />
            </rect>
            <text x="50%" y="50%" fill="black" font-size="14" font-weight="bold" text-anchor="middle" dy=".3em">{label}</text>
        </svg>

        <script>
            const progressRect = document.getElementById('progress-rect');
            progressRect.setAttribute('width', '{value}%');
        </script>
    """
    st.markdown(progress_html, unsafe_allow_html=True)

# Example usage with animated linear progress bar

def animated_circular_progress_bar(label, value, max_value, color='red', max_size=150):
    normalized_value = min(value / max_value, 1.0)  # Normalize value to be between 0 and 1
    progress_html = f"""
        <div id="progress-container" style="width: {max_size}px; height: {max_size}px; position: relative; border-radius: 50%; overflow: hidden;">
            <div id="progress-circle" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
            <div id="animated-circle" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: {color}; font-size: 11px; font-weight: bold;">{label}<br>{value} </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/progressbar.js/1.0.1/progressbar.min.js"></script>
        <script>
            const container = document.getElementById('progress-container');
            const bar = new ProgressBar.Circle(container, {{
                strokeWidth: 13,
                easing: 'easeInOut',
                duration: 2000,
                color: '{color}',
                trailColor: '#e0e0e0',
                trailWidth: 10,
                svgStyle: null
            }});

            bar.animate({normalized_value});
        </script>
    """
    return progress_html

def animated_linear_progress_bar_with_metric(metric_value, label, value, color='green', width=200, height=20):
    progress_html = f"""
        <div style="display: flex; align-items: center; text-align: left;">
            <div style="font-size: 14px; font-weight: bold; margin-right: 10px;">{metric_value}</div>
            <div style="position: relative; width: {width}px;">
                <svg width="{width}" height="{height}" style="background-color: #f1f1f1; border-radius: 5px;">
                    <rect id="progress-rect" x="0" y="0" width="0%" height="100%" fill="{color}">
                        <animate attributeName="width" from="0%" to="{value}%" dur="2s" fill="freeze" />
                    </rect>
                    <text x="50%" y="50%" fill="black" font-size="14" font-weight="bold" text-anchor="middle" dy=".3em">{label}</text>
                </svg>
            </div>
        </div>

        <script>
            const progressRect = document.getElementById('progress-rect');
            progressRect.setAttribute('width', '{value}%');
        </script>
    """
    st.markdown(progress_html, unsafe_allow_html=True)

# HTML and CSS for animated line
animated_line_html = """
<style>
    @keyframes drawLine {
        to {
            stroke-dashoffset: 0;
        }
    }

    .animated-line {
        width: 100%;
        height: 12px;
        background-color: black;
        position: relative;
        overflow: hidden;
    }

    .line-path {
        stroke-dasharray: 1000;
        stroke-dashoffset: 1000;
        animation: drawLine 2s forwards;
        stroke: #3498db;
        stroke-width: 2px;
    }
</style>

<div class="animated-line">
    <svg width="100%" height="100%">
        <line class="line-path" x1="0" y1="1" x2="100%" y2="1"/>
    </svg>
</div>
"""

# Display the animated line using HTML



st.set_page_config(page_title="Explore", page_icon="📈")


st.markdown(printCostumTitleAndContenth1("Explore" , "") , unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(
       "Select the Season...",
       ("1", "2", "3"),
       index=0,
       placeholder="Select the farm...",
    )

with col2:
    optionplot = st.selectbox(
       "Select the Plot...",
       ("1", "3", "4", "5"),
       index=0,
       placeholder="Select the farm...",
    )

df = pd.read_csv(f'Dataset/Rice/Season{option}.csv')
st.header(f"Season{option}")
st.markdown(printCostumTitleAndContenth3(f"Rice Traits",
                                         ""),
            unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    max_weight = 7  # Maximum weight in KG
    current_weight = df['No. of Tiller'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='orange',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col2:
    max_weight = 7  # Maximum weight in KG
    current_weight = df['No. of Panicle'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col3:
    max_weight = 42  # Maximum weight in KG
    current_weight = df['No. of Spikelet'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='red',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col4:
    max_weight = 180  # Maximum weight in KG
    current_weight = df['No. of Filled Grain'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col5:
    max_weight = 155  # Maximum weight in KG
    current_weight = df['No. Of Unfilled Grain'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight, color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col6:
    max_weight = 28  # Maximum weight in KG
    current_weight = df['Weight Grain (1000 grains)'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                   color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)



dfn = pd.read_csv(f'Dataset/Rice/N.csv')

fn = dfn.query(f"""Season == {option} & Plot == {optionplot}""")
fn30 = fn.query(f"""Day == 30""")
fn60 = fn.query(f"""Day == 60""")
fn90 = fn.query(f"""Day == 90""")
# Nutrient data dictionary with initial values
nutrient_data = {'Mg': [fn30['Mg'].values[0], fn60['Mg'].values[0], fn90['Mg'].values[0]],
                 'Ca': [fn30['Ca'].values[0], fn60['Ca'].values[0], fn90['Ca'].values[0]],
                 'N': [fn30['N'].values[0], fn60['N'].values[0], fn90['N'].values[0]],
                 'P': [fn30['P'].values[0], fn60['P'].values[0], fn90['P'].values[0]],
                 'K': [fn30['K'].values[0], fn60['K'].values[0], fn90['K'].values[0]]}


# Create a DataFrame with the dictionary
df = pd.DataFrame.from_dict(nutrient_data, orient='index', columns=[30, 60, 90])
# Animated line chart with Plotly
fig = px.line(df.transpose(), x=df.columns, y=df.index,
              labels={'value': 'Nutrient Level', 'variable': 'Nutrient'},
              title='Nutrient Trend')
fig.update_layout(xaxis_title='DAYS')

fig.update_traces(mode='lines+markers')

# Display the animated chart
st.plotly_chart(fig)

######### FOR PLOT ############



df = pd.read_csv(f'Dataset/Rice/Season{option}.csv')
st.header(f"Plot {optionplot}")
df = df.query(f"""Plot == 'P{optionplot}'""")
st.markdown(printCostumTitleAndContenth3(f"Rice Traits",
                                         ""),
            unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    max_weight = 7  # Maximum weight in KG
    current_weight = df['No. of Tiller'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='orange',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col2:
    max_weight = 7  # Maximum weight in KG
    current_weight = df['No. of Panicle'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col3:
    max_weight = 9  # Maximum weight in KG
    current_weight = df['No. of Spikelet'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='red',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col4:
    max_weight = 180  # Maximum weight in KG
    current_weight = df['No. of Filled Grain'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col5:
    max_weight = 155  # Maximum weight in KG
    current_weight = df['No. Of Unfilled Grain'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight, color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

with col6:
    max_weight = 28  # Maximum weight in KG
    current_weight = df['Weight Grain (1000 grains)'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                   color='green',
                                                   max_size=95)
    st.components.v1.html(progress_html, height=105)

st.markdown(printCostumTitleAndContenth3(f"Nutrients Trend",
                                         ""),
            unsafe_allow_html=True)

dfn = pd.read_csv(f'Dataset/Rice/N.csv')

fn = dfn.query(f"""Season == {option} & Plot == {optionplot}""")
fn30 = fn.query(f"""Day == 30""")
fn60 = fn.query(f"""Day == 60""")
fn90 = fn.query(f"""Day == 90""")
# Nutrient data dictionary with initial values
nutrient_data = {'Mg': [fn30['Mg'].values[0], fn60['Mg'].values[0], fn90['Mg'].values[0]],
                 'Ca': [fn30['Ca'].values[0], fn60['Ca'].values[0], fn90['Ca'].values[0]],
                 'N': [fn30['N'].values[0], fn60['N'].values[0], fn90['N'].values[0]],
                 'P': [fn30['P'].values[0], fn60['P'].values[0], fn90['P'].values[0]],
                 'K': [fn30['K'].values[0], fn60['K'].values[0], fn90['K'].values[0]]}
# Create a DataFrame with the dictionary
df = pd.DataFrame.from_dict(nutrient_data, orient='index', columns=[30, 60, 90])

# Animated line chart with Plotly
fig = px.line(df.transpose(), x=df.columns, y=df.index,
              labels={'value': 'Nutrient Level', 'variable': 'Nutrient'},
              title='Nutrient Trend')
fig.update_layout(xaxis_title='DAYS')

fig.update_traces(mode='lines+markers')

# Display the animated chart
st.plotly_chart(fig)
st.markdown(animated_line_html, unsafe_allow_html=True)
st.markdown(printCostumTitleAndContenth1("Trend" , "") , unsafe_allow_html=True)


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
traits = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'SPAD', 'No. of Spikelet', 'No. of Filled Grain', 'No. Of Unfilled Grain', 'Weight Grain (1000 grains)']

optionTrait = st.selectbox(
    "Select the Trait...",
    traits,
    index=0,
    placeholder="Select the farm...",
)

# Create a DataFrame from CSV data
df = pd.read_csv(io.StringIO(csv_data))
# List of traits to plot
# Streamlit App
st.title('')
# Plot grouped bar chart using Plotly Express
fig = px.bar(df, x='Season', y=optionTrait, color='Plot Number',
             barmode='group',
             title=f'{optionTrait} across Seasons for different Plots',
             labels={'Season': 'Season', optionTrait: f'{optionTrait}', 'Plot Number': 'Plot'})

# Display the plot using st.plotly_chart
st.plotly_chart(fig)
# Additional information
st.write("")

