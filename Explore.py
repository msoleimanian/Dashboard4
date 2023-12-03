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
        height: 2px;
        background-color: #3498db;
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


st.set_page_config(page_title="Insight", page_icon="📈")

# Sample data



option2 = st.sidebar.selectbox(
   "Select the Farm",
   ("Pok choy", "Rice"),
   index=1,
   placeholder="Select the farm...",
)



option = st.sidebar.selectbox(
   "Select the Season...",
   ("Season1", "Season2", "Season3"),
   index=0,
   placeholder="Select the farm...",
)

# Continue with other code after the progress animation
farmsdfst = pd.read_csv ('Dataset/FarmsStatus.csv')


if option2 == 'Rice':

    # Streamlit app
    st.header("Season Scores")
    col1, col2, col3, col4 = st.columns(4)

    # HTML for the hardcoded table
    table_html = """
    <table>
        <tr>
            <th>Season</th>
            <th>Score</th>
        </tr>
        <tr>
            <td>1</td>
            <td>57.38</td>
        </tr>
        <tr>
            <td>2</td>
            <td>59.21</td>
        </tr>
        <tr>
            <td>3</td>
            <td>42.64</td>
        </tr>
    </table>
    """

    # Display the HTML table in Streamlit
    col1.markdown(table_html, unsafe_allow_html=True)

    with col2:
        max_weight = 100  # Maximum weight in KG
        current_weight = 57.38  # Current weight in KG
        progress_html = animated_circular_progress_bar('Season1', current_weight, max_weight, color='orange',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)


    with col3:
        max_weight = 100  # Maximum weight in KG
        current_weight = 59.21  # Current weight in KG
        progress_html = animated_circular_progress_bar('Season2', current_weight, max_weight, color='orange',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)


    with col4:
        max_weight = 100  # Maximum weight in KG
        current_weight = 42.64  # Current weight in KG
        progress_html = animated_circular_progress_bar('Season3', current_weight, max_weight, color='red',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)

    st.header("Comparison Best Season and Worst Season in Rice Traits")

    st.markdown(printCostumTitleAndContenth3("Best Season",
                                             ""),
                unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
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

    with col6:
        max_weight = 33  # Maximum weight in KG
        current_weight = 32.08  # Current weight in KG
        progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                       color='green',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)


    st.markdown(printCostumTitleAndContenth3("Worst Season",
                                             ""),
                unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
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
        progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='orange',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)

    with col4:
        max_weight = 803  # Maximum weight in KG
        current_weight = 151  # Current weight in KG
        progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight,
                                                       color='red',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)

    with col5:
        max_weight = 343  # Maximum weight in KG
        current_weight = 130  # Current weight in KG
        progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                       color='red',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)

    with col6:
        max_weight = 33  # Maximum weight in KG
        current_weight = 20  # Current weight in KG
        progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                       color='orange',
                                                       max_size=95)
        st.components.v1.html(progress_html, height=105)

    st.markdown(printCostumTitleAndContenth3("Nutrients Level",
                                             "what is the Risk level of each Nutrients that has been measured."),
                unsafe_allow_html=True)








    if option == 'Season1':
        st.markdown(printCostumTitleAndContenth3("Rice trait",
                                                 "what is the Risk level of each growth trait that has been measured."),
                    unsafe_allow_html=True)
        col1, col2,col3, col4, col5, col6 = st.columns(6)
        with col1:
            max_weight = 129  # Maximum weight in KG
            current_weight = 95.93  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='orange', max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col2:
            max_weight = 7  # Maximum weight in KG
            current_weight = 6  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col3:
            max_weight = 9  # Maximum weight in KG
            current_weight = 4 # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='red',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)


        with col4:
            max_weight = 180  # Maximum weight in KG
            current_weight = 151 # Current weight in KG
            progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='green', max_size=95)
            st.components.v1.html(progress_html, height=105)


        with col5:
            max_weight = 155  # Maximum weight in KG
            current_weight = 130  # Current weight in KG
            progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        with col6:
            max_weight = 28  # Maximum weight in KG
            current_weight = 24.99 # Current weight in KG
            progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight, color='green',
                                                           max_size=95)
            st.components.v1.html(progress_html, height=105)

        st.markdown(printCostumTitleAndContenth3("Nutrients Level",
                                                 "what is the Risk level of each Nutrients that has been measured."),
                    unsafe_allow_html=True)
        st.write("Day 30")
        col1, col2, col3, col4, col5 = st.columns(5)
        st.write("Day 60")
        col11, col12, col13, col14, col15 = st.columns(5)
        st.write("Day 90")
        col21, col22, col23, col24, col25 = st.columns(5)

        with col1:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "N", 50, color='#55a630', width=85,
                                                     height=30)
        with col11:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "N", 50, color='#55a630', width=85,
                                                     height=30)
        with col21:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "N", 50, color='#55a630', width=85,
                                                     height=30)
        with col2:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "P", 50, color='#55a630', width=85,
                                                     height=30)
        with col12:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "P", 50, color='#55a630', width=85,
                                                     height=30)
        with col22:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "P", 50, color='#55a630', width=85,
                                                     height=30)

        with col3:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "K", 50, color='#55a630', width=85,
                                                     height=30)
        with col13:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "K", 50, color='#55a630', width=85,

                                                     height=30)
        with col23:
            # Example usage
            animated_linear_progress_bar_with_metric("2.2%", "K", 50, color='#55a630', width=85,
                                                     height=30)

        with col4:
                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=85,
                                                         height=30)

        with col14:
                        # Example usage

                animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=85,
                                                         height=30)
        with col24:
                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=85,
                                                         height=30)

        with col5:

                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Ca", 50, color='#55a630', width=85,
                                                         height=30)
        with col15:
                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Ca", 50, color='#55a630', width=85,
                                                         height=30)
        with col25:
                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Ca", 50, color='#55a630', width=85,
                                                         height=30)

        st.markdown(printCostumTitleAndContenth3("Plot Status",
                                                 "There are Plot Status."), unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            max_weight = 100  # Maximum weight in KG
            current_weight = 22  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plot1', current_weight, max_weight, color='red',
                                                           max_size=110)
            st.components.v1.html(progress_html, height=120)

        with col2:
            max_weight = 100  # Maximum weight in KG
            current_weight = 65  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plot2', current_weight, max_weight, color='orange',
                                                           max_size=110)
            st.components.v1.html(progress_html, height=120)

        col3, col4 = st.columns(2)
        with col3:
            max_weight = 100  # Maximum weight in KG
            current_weight = 55  # Current weight in KG
            progress_html = animated_circular_progress_bar('Plot3', current_weight, max_weight, color='blue',
                                                           max_size=110)
            st.components.v1.html(progress_html, height=120)



        plotoption = st.sidebar.radio(
        "Selct the Plot",
        [ "***Plot 1***" , "***Plot 2***",  "***Plot 3***" ] , index=None )
        if plotoption == "***Plot 1***":
            # HTML code for a horizontal line
            horizontal_line_html = "<hr>"

            # Display the horizontal line using HTML
            st.markdown(horizontal_line_html, unsafe_allow_html=True)
            st.markdown(printCostumTitleAndContenth3("Plot1 Progress",
                                                     "You can see the status of the Plot1."),
                        unsafe_allow_html=True)


            colmain1, colmain2 = st.columns(2)
            with colmain1:


                st.markdown(printCostumTitleAndContenth3("Growth trait",
                                                         "what is the Risk level of each growth trait that has been measured."),
                            unsafe_allow_html=True)

                col1, col2 = st.columns(2)
                with col1:
                    max_weight = 130  # Maximum weight in KG
                    current_weight = 44  # Current weight in KG
                    progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight,
                                                                   color='red', max_size=140)
                    st.components.v1.html(progress_html, height=180)

                with col2:
                    max_weight = 7  # Maximum weight in KG
                    current_weight = 3  # Current weight in KG
                    progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight,
                                                                   color='red',
                                                                   max_size=140)
                    st.components.v1.html(progress_html, height=180)

                col3, col4 = st.columns(2)
                with col3:
                    max_weight = 9  # Maximum weight in KG
                    current_weight = 5  # Current weight in KG
                    progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight,
                                                                   color='orange',
                                                                   max_size=140)
                    st.components.v1.html(progress_html, height=180)

                with col4:
                    max_weight = 180  # Maximum weight in KG
                    current_weight = 151  # Current weight in KG
                    progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight,
                                                                   color='green', max_size=140)
                    st.components.v1.html(progress_html, height=180)

                col1, col2 = st.columns(2)
                with col1:
                    max_weight = 155  # Maximum weight in KG
                    current_weight = 100  # Current weight in KG
                    progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight,
                                                                   color='orange',
                                                                   max_size=140)
                    st.components.v1.html(progress_html, height=180)

                with col2:
                    max_weight = 28  # Maximum weight in KG
                    current_weight = 24.99  # Current weight in KG
                    progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                                   color='green',
                                                                   max_size=140)
                    st.components.v1.html(progress_html, height=180)

            with colmain2:
                st.markdown(printCostumTitleAndContenth3("Nutrients Level",
                                                         "what is the Risk level of each Nutrients that has been measured."),
                            unsafe_allow_html=True)

                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=200,
                                                         height=30)
                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=200,
                                                         height=30)
                # Example usage
                animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=200,
                                                         height=30)



                ca = 95  # Replace with your actual nutrient level
                animated_linear_progress_bar('N', ca, color='green')  # Use your preferred color


                # Set the percentage increase for Calcium (Ca) and Magnesium (Mg)
                ca_increase_percentage = 29
                mg_increase_percentage = 55

                # Generate suggestions for increasing Ca and Mg levels
                ca_suggestion, mg_suggestion = generate_nutrient_increase_suggestions(ca_increase_percentage,
                                                                                      mg_increase_percentage)

                # Define the CSS for the card style
                card_style = """
                            background-color: #f1f1f1;
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                            margin: 10px;
                        """

                # Show the suggestions in separate cards
                with st.container():
                    # Card for increasing Ca levels
                    st.markdown('<div style="{}">{}</div>'.format(card_style, ca_suggestion), unsafe_allow_html=True)

                    # Card for increasing Mg levels
                    st.markdown('<div style="{}">{}</div>'.format(card_style, mg_suggestion), unsafe_allow_html=True)

    if option == 'Season2':
        import streamlit as st



        # Example usage
        animated_linear_progress_bar_with_metric("2.2%", "Mg", 50, color='#55a630', width=200,
                                                 height=30)

    if option == 'Season3':
        st.write(farmsdfst.iloc[2])