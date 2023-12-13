import streamlit as st
import time
import numpy as np
import pandas as pd
import time


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


st.set_page_config(page_title="Summary", page_icon="📈")


best_season_pot_text = """
The system has the ability to distinguish the best and worst seasons and plots based on the most important attribute for ranking, while also considering the efficiency of other attributes relative to the best among plots. 
"""

# Title for the card
card_title = "Cultivation Excellence: Unveiling the Worst and Best Season and Pot 🌾"

# Render the card with HTML format using Streamlit
st.markdown(
    f"""
    <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">
        <h1 style="text-align:center;font-size:32px;color:#2a3f54">{card_title}</h1>
        <hr style="border:1px solid #2a3f54">
        <p style="font-size:18px;colorCultivation Excellence: Unveiling the Worst and Best Season and Pot:#2a3f54">{best_season_pot_text}</p>
    </div>
    """,
    unsafe_allow_html=True
)

option2 = st.sidebar.selectbox(
   "Select the Farm",
   ("Pok choy", "Rice"),
   index=1,
   placeholder="Select the farm...",
)

# Continue with other code after the progress animation
farmsdfst = pd.read_csv ('Dataset/FarmsStatus.csv')

st.write("")
st.write("")
st.markdown(animated_line_html, unsafe_allow_html=True)

if option2 == 'Rice':
    st.markdown(printCostumTitleAndContenth2("Best Performance",
                                             "The best performance is displayed among Seasons and plots."),
                unsafe_allow_html=True)

    st.markdown(printCostumTitleAndContenth3("Season2",""),unsafe_allow_html=True)


    col11 , col22 = st.columns(2)
    with col11:
        st.write("High Value Trait")
        max_weight = 33  # Maximum weight in KG
        current_weight = 32.08  # Current weight in KG
        progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                       color='green',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)
    with col22:
        st.write("Other Traits Value")
        col1, col2,col3 = st.columns(3)
        with col1:
            max_weight = 7  # Maximum weight in KG
            current_weight = 5  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='orange',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col2:
            max_weight = 5  # Maximum weight in KG
            current_weight = 4  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col3:
            max_weight = 42  # Maximum weight in KG
            current_weight = 36  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)
        col4, col5, col6 = st.columns(3)
        with col4:
            max_weight = 803  # Maximum weight in KG
            current_weight = 574  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='orange',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col5:
            max_weight = 343  # Maximum weight in KG
            current_weight = 288  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                           color='orange',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)


    st.markdown(printCostumTitleAndContenth3("Pot5 in Season2",
                                             ""),
                unsafe_allow_html=True)

    col11 , col22 = st.columns(2)
    with col11:
        st.write("High Value Trait")
        max_weight = 33.46  # Maximum weight in KG
        current_weight = 33.46  # Current weight in KG
        progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                       color='green',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)
    with col22:
        st.write("Other Trait Value")
        col1, col2,col3 = st.columns(3)
        with col1:
            max_weight = 7  # Maximum weight in KG
            current_weight = 5  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='orange',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col2:
            max_weight = 5  # Maximum weight in KG
            current_weight = 5  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col3:
            max_weight = 42  # Maximum weight in KG
            current_weight = 37  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)
        col4, col5, col6 = st.columns(3)
        with col4:
            max_weight = 803  # Maximum weight in KG
            current_weight = 662  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col5:
            max_weight = 343  # Maximum weight in KG
            current_weight = 290  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                           color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

    st.write("")
    st.write("")
    st.markdown(animated_line_html, unsafe_allow_html=True)
    st.markdown(printCostumTitleAndContenth2("Worst Performance",
                                             "The Worst performance is displayed among Seasons and plots."),
                unsafe_allow_html=True)
    st.markdown(printCostumTitleAndContenth3("Season1",
                                             ""),
                unsafe_allow_html=True)


    col11 , col22 = st.columns(2)
    with col11:
        st.write("High Value Trait")
        max_weight = 33  # Maximum weight in KG
        current_weight = 24.99  # Current weight in KG
        progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                       color='orange',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)
    with col22:
        st.write("Other Trait Value")
        col1, col2,col3 = st.columns(3)
        with col1:
            max_weight = 7  # Maximum weight in KG
            current_weight = 6  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col2:
            max_weight = 5  # Maximum weight in KG
            current_weight = 4  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col3:
            max_weight = 42  # Maximum weight in KG
            current_weight = 34  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)
        col4, col5, col6 = st.columns(3)
        with col4:
            max_weight = 803  # Maximum weight in KG
            current_weight = 151  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='red',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col5:
            max_weight = 343  # Maximum weight in KG
            current_weight = 130  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                           color='orange',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)


    st.markdown(printCostumTitleAndContenth3("Pot5 in Season1",
                                             ""),
                unsafe_allow_html=True)

    col11 , col22 = st.columns(2)
    with col11:
        st.write("High Value Trait")
        max_weight = 33.46  # Maximum weight in KG
        current_weight = 23.25  # Current weight in KG
        progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                       color='orange',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)
    with col22:
        st.write("High Value Trait")
        col1, col2,col3 = st.columns(3)
        with col1:
            max_weight = 7  # Maximum weight in KG
            current_weight = 7  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col2:
            max_weight = 5  # Maximum weight in KG
            current_weight = 4  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col3:
            max_weight = 42  # Maximum weight in KG
            current_weight = 35  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)
        col4, col5,col6 = st.columns(3)
        with col4:
            max_weight = 803  # Maximum weight in KG
            current_weight = 150  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='red',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col5:
            max_weight = 343  # Maximum weight in KG
            current_weight = 163  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                           color='orange',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)




