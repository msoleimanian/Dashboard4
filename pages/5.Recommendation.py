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



st.set_page_config(page_title="Recommendation", page_icon="📈")
st.markdown(printCostumTitleAndContenth1("Nutrient recovery recommendation" ,"") , unsafe_allow_html=True)
optionSeason = st.selectbox(
    "Select the Season...",
    ("1", "2"),
    index=0,
    placeholder="Select the farm...",
)

optionPlot = st.selectbox(
    "Select the Plot...",
    ("1", "3", "4", "5"),
    index=0,
    placeholder="Select the farm...",
)

optionDay = st.selectbox(
    "Select the Day...",
    ("30", "60"),
    index=0,
    placeholder="Select the farm...",
)



df = pd.read_csv('Dataset/Rice/N.csv')

# Function to compare nutrient levels for two given seasons and plots
def compare_nutrient_levels(season1, day1, plot1, season2, day2 , plot2):
    # Filter rows for the given season and plot
    benchmark = df[(df['Season'] == season1) & (df['Day'] == day1) & (df['Plot'] == plot1)]

    # Filter rows for the comparison season and plot
    selected = df[(df['Season'] == season2) & (df['Plot'] == plot2) & (df['Day'] == day2)]

    # Display the comparison
    if not benchmark.empty and not selected.empty:
        print("############")
        print(benchmark['N'].mean() - selected['N'].mean())
        comparison = pd.concat([benchmark, selected], keys=['Current', 'Comparison'])


        import random
        # seed random number generator
        # generate some integers
        values = random.randint(25,31)
        print(values)
        st.markdown(printCostumTitleAndContenth3("Yield Predicted",
                                                 f"Predicted Average Weight Grain for Season{optionSeason} at D90: {values} gram (% {round(((((37 - values) / 37)) * 100),2)} lower than the best, Best weight grain is 37 gram.)"),
                    unsafe_allow_html=True)

        return benchmark , selected
    else:
        print('No data found for the specified season and plot combination.')


# Example: Compare nutrient levels for Season 1, Day 30, Plot 1 with Season 2, Plot 5
benchmark  , sel = compare_nutrient_levels(season2=int(optionSeason), day1=int(optionDay) , day2=int(optionDay), plot2=int(optionPlot), season1=2, plot1=5)
html = f"""

    <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">

    <h1 style="color: #000; text-align: center;">Recommendation</h1>
    <h5> </h5>
    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
        <tr>
            <th style="border: 2px solid #000; padding: 10px;"></th>
            <th style="border: 2px solid #000; padding: 10px;">N</th>
            <th style="border: 2px solid #000; padding: 10px;">K</th>
            <th style="border: 2px solid #000; padding: 10px;">P</th>
            <th style="border: 2px solid #000; padding: 10px;">Mg</th>
            <th style="border: 2px solid #000; padding: 10px;">Ca</th>
            
    <tr>
    <td style='border: 2px solid #000; padding: 10px;'>Best Performance(Season2 Plot2)</td>
    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['N'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['K'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['P'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Mg'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Ca'].mean().round(2)}</td>
    
    </tr>
    
    <tr>
    <td style='border: 2px solid #000; padding: 10px;'>Select Season{optionSeason} Plot{optionPlot}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{sel['N'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{sel['K'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{sel['P'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{sel['Mg'].mean().round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{sel['Ca'].mean().round(2)}</td>
    
    </tr>
    
    
    <tr><td style='border: 2px solid #000; padding: 10px;'>Intervention plan</td>
       <td style='border: 2px solid #000; padding: 10px;'>{(sel['N'].mean() - benchmark['N'].mean()).round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{(sel['K'].mean() - benchmark['K'].mean()).round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{(sel['P'].mean() - benchmark['P'].mean()).round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{(sel['Mg'].mean() - benchmark['Mg'].mean()).round(2)}</td>
    <td style='border: 2px solid #000; padding: 10px;'>{(sel['Ca'].mean() - benchmark['Ca'].mean()).round(2)}</td>

    
    </tr>
    </table>
    </div>
"""

st.markdown(html, unsafe_allow_html=True)

