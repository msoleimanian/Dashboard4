import streamlit as st
import time
import numpy as np
import pandas as pd
import time
import plotly.express as px
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


def printCostumTitleAndContenth4(title, context):
    return f"""
        <div class="jumbotron">
        <h4>{title}</h4>
        <h4>{context}</h4>
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

st.markdown(printCostumTitleAndContenth2("Best Performace",
                                         ""),
            unsafe_allow_html=True)

col1 , col2 = st.columns(2)

with col1:
    st.markdown(printCostumTitleAndContenth3("Season2", ""), unsafe_allow_html=True)
    st.write("High Value Trait")
    max_weight = 33  # Maximum weight in KG
    current_weight = 32.08  # Current weight in KG
    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                   color='green',
                                                   max_size=200)
    st.components.v1.html(progress_html, height=210)

with col2:
    st.markdown(printCostumTitleAndContenth3(f"Plot5", ""), unsafe_allow_html=True)
    st.write("High Value Trait")
    max_weight = 33  # Maximum weight in KG
    current_weight = 33  # Current weight in KG
    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                   color='green',
                                                   max_size=200)
    st.components.v1.html(progress_html, height=210)


st.markdown(printCostumTitleAndContenth2("Selected Season and Plot",
                                         ""),
            unsafe_allow_html=True)
col1 , col2 = st.columns(2)
with col1:
    optionseasson = st.selectbox(
       "Select the Season...",
       ("1", "2" , "3"),
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


dfs = pd.read_csv(f'Dataset/Rice/Season{optionseasson}.csv')
dfp = dfs.query(f"""Plot == 'P{optionplot}'""")

col1, col2 = st.columns(2)
with col1:
    st.markdown(printCostumTitleAndContenth3(f"Season{optionseasson}", ""), unsafe_allow_html=True)
    st.write("High Value Trait")
    max_weight = 33  # Maximum weight in KG
    current_weight = dfs['Weight Grain (1000 grains)'].mean() # Current weight in KG
    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                   color='green',
                                                   max_size=200)
    st.components.v1.html(progress_html, height=210)

with col2:
    st.markdown(printCostumTitleAndContenth3(f"Plot{optionplot}", ""), unsafe_allow_html=True)
    st.write("High Value Trait")
    max_weight = 33  # Maximum weight in KG
    current_weight = dfp['Weight Grain (1000 grains)'].mean()  # Current weight in KG
    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                   color='green',
                                                   max_size=200)
    st.components.v1.html(progress_html, height=210)

df = pd.read_csv(f'Dataset/Rice/Season{optionseasson}.csv')
df = df.query(f"""Plot == 'P{optionplot}'""")
st.markdown(printCostumTitleAndContenth3(f"Nutrients Level",
                                         ""),
            unsafe_allow_html=True)


dfn = pd.read_csv(f'Dataset/Rice/N.csv')

fn = dfn.query(f"""Season == {optionseasson} & Plot == {optionplot}""")
fn30 = fn.query(f"""Day == 30""")
fn60 = fn.query(f"""Day == 60""")
fn90 = fn.query(f"""Day == 90""")


fnbest = dfn.query(f"""Season == 2 & Plot == 5""")
fnbest30 = fnbest.query(f"""Day == 30""")
fnbest60 = fnbest.query(f"""Day == 60""")
fnbest90 = fnbest.query(f"""Day == 90""")
# Nutrient data dictionary with initial values
nutrients = ['Mg', 'Ca', 'N', 'P', 'K']
for i in range(5):
    n =nutrients[i]
    nutrient_data = {f'{n} Season2 pot5 (Best Performance)': [fnbest30[nutrients[i]].values[0], fnbest60[nutrients[i]].values[0], fnbest90[nutrients[i]].values[0]], f'{nutrients[i]} Season{optionseasson} plot{optionplot}(Selected season)': [fn30[nutrients[i]].values[0], fn60[nutrients[i]].values[0], fn90[nutrients[i]].values[0]]}

    # Create a DataFrame with the dictionary
    df = pd.DataFrame.from_dict(nutrient_data, orient='index', columns=[30, 60, 90])

    # Animated line chart with Plot
    fig = px.line(df.transpose(), x=df.columns, y=df.index,
                  labels={'value': 'Nutrient Level', 'variable': 'Nutrient'},
                  title=n)
    fig.update_layout(xaxis_title='DAYS')
    fig.update_traces(mode='lines+markers')

    # Display the animated chart
    st.plotly_chart(fig)
