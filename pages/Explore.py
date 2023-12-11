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



st.set_page_config(page_title="Explore", page_icon="📈")




# Function to scale the numbers in a column to a 0-10 range
def scale_numbers(column_values):
    max_value = max(column_values)
    return [round((value / max_value) * 10, 2) for value in column_values]

# Function to get color based on percentage difference from the best
def get_color(percent_difference):
    if percent_difference == 0:
        return 'green'  # Light Red
    elif 0 < percent_difference <= 1.5:
        return '#b3ffb3'
    elif 1.5 < percent_difference <= 3:
        return 'orange'
    elif 3 < percent_difference <= 3.5:
        return '#ff6666'


# Data
seasons = ['Season 1', 'Season 2', 'Season 3']
plot_numbers = {'Season 1': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                'Season 2': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                'Season 3': ['Plot1', 'Plot3', 'Plot4', 'Plot5']}

columns = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'No. of Spikelet',
           'No. of Filled Grain', 'No. Of Unfilled Grain', 'Weight Grain (1000 grains)']

column_score = ['Weight Grain (1000 grains)']

# Create an empty list to store data
data_rows = []

# Populate the data list for data entry
for season in seasons:
    for plot in plot_numbers[season]:
        row = {'Season': season, 'Plot Number': plot}
        for col in column_score:
            row[col] = None  # Initialize with None for data entry
        data_rows.append(row)
print(data_rows)
# Create DataFrame for data entry
data_entry = pd.DataFrame(data_rows)

# Provide a 2D array to fill in the numbers
numbers_to_fill = [
    [98.51, 6, 5,  42, 195, 154, 26.27],
    [98, 5, 5,  35, 122, 155, 24.26],
    [93.20, 5, 4,  27, 137, 46, 25.95],
    [93.99, 7, 5,  35, 150, 163, 23.25],

    [103.16, 5, 5,  38, 188, 271, 33.31],
    [98.75, 5, 5,  38, 803, 250, 31.01],
    [88.80, 4, 4,  30, 643, 343, 30.55],
    [92.07, 5, 5,  37, 662, 290, 33.46],

    [100.16, 5, 5,  41, 84, 16, 33.19],
    [96.95, 5, 4,  41, 84, 16, 31.43],
    [88.17, 3, 4,  30, 86, 14, 26.20],
    [93.98, 4, 4,  37, 82, 5, 24.23],
]

# Fill up the DataFrame with the provided numbers
for col_index, col_values in enumerate(zip(*numbers_to_fill)):
    for row_index, value in enumerate(col_values):
        data_entry.at[row_index, columns[col_index]] = value

# Scale the numbers and sum each row
scaled_data = data_entry.copy()
print("#####123")
print(scaled_data)
for col in columns:
    scaled_values = scale_numbers(data_entry[col])
    scaled_data[col] = scaled_values

scaled_data['Total Score'] = scaled_data[column_score].sum(axis=1)

# Find the best and worst total scores
max_total_score = scaled_data['Total Score'].max()
min_total_score = scaled_data['Total Score'].min()

# HTML styling with inline styles for black text color, thicker black border lines, and increased width
html_code = f"""

    <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">

    <h1 style="color: #000; text-align: center;">Scores</h1>
    <h5>Explore the captivating table that scores each season and pot, considering the crucial factors of weight grain , and a scaling system from 1 to 10. </h5>
    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
        <tr>
            <th style="border: 2px solid #000; padding: 10px;">Season</th>
            <th style="border: 2px solid #000; padding: 10px;">Plot Number</th>
            <th style="border: 2px solid #000; padding: 10px;">Score</th>
        </tr>
        {"".join(
            f"<tr><td style='border: 2px solid #000; padding: 10px;'>{row['Season']}</td>"
            f"<td style='border: 2px solid #000; padding: 10px;'>{row['Plot Number']}</td>"
            f"<td style='border: 2px solid #000; padding: 10px; "
            f"background-color: {get_color((10 - row['Total Score'])) };'>"
            f"{row['Total Score']}</td></tr>"
            for _, row in scaled_data.iterrows()
        )}
    </table>
    </div>
"""

# Display the HTML content
st.write("")
st.markdown(html_code, unsafe_allow_html=True)




option = st.sidebar.selectbox(
   "Select the Season...",
   ("Season1", "Season2", "Season3"),
   index=0,
   placeholder="Select the farm...",
)

optionplot = st.sidebar.selectbox(
   "Select the Season...",
   ("plot1", "plot3", "plot4", "plot5"),
   index=0,
   placeholder="Select the farm...",
)



if option == 'Season1':
   st.markdown(printCostumTitleAndContenth3(f"Rice trait: {option}",
                                            "what is the Risk level of each growth trait that has been measured."),
               unsafe_allow_html=True)
   col1, col2, col3, col4, col5, col6 = st.columns(6)
   with col1:
      max_weight = 129  # Maximum weight in KG
      current_weight = 95.93  # Current weight in KG
      progress_html = animated_circular_progress_bar('No. of Tiller', current_weight, max_weight, color='orange',
                                                     max_size=95)
      st.components.v1.html(progress_html, height=105)

   with col2:
      max_weight = 7  # Maximum weight in KG
      current_weight = 6  # Current weight in KG
      progress_html = animated_circular_progress_bar('No. of Panicle', current_weight, max_weight, color='green',
                                                     max_size=95)
      st.components.v1.html(progress_html, height=105)

   with col3:
      max_weight = 9  # Maximum weight in KG
      current_weight = 4  # Current weight in KG
      progress_html = animated_circular_progress_bar('No. of Spikelet', current_weight, max_weight, color='red',
                                                     max_size=95)
      st.components.v1.html(progress_html, height=105)

   with col4:
      max_weight = 180  # Maximum weight in KG
      current_weight = 151  # Current weight in KG
      progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight, color='green',
                                                     max_size=95)
      st.components.v1.html(progress_html, height=105)

   with col5:
      max_weight = 155  # Maximum weight in KG
      current_weight = 130  # Current weight in KG
      progress_html = animated_circular_progress_bar('No. Of Unfilled Grain', current_weight, max_weight, color='green',
                                                     max_size=95)
      st.components.v1.html(progress_html, height=105)

   with col6:
      max_weight = 28  # Maximum weight in KG
      current_weight = 24.99  # Current weight in KG
      progress_html = animated_circular_progress_bar('Weight Grain(1000 grains)', current_weight, max_weight,
                                                     color='green',
                                                     max_size=95)
      st.components.v1.html(progress_html, height=105)

   st.markdown(printCostumTitleAndContenth3(f"Nutrients Level: {option}",
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
      animated_linear_progress_bar_with_metric("3.56%", "N", 35.6, color='#55a630', width=85,
                                               height=30)
   with col11:
      # Example usage
      animated_linear_progress_bar_with_metric("1.6%", "N", 16, color='#55a630', width=85,
                                               height=30)
   with col21:
      # Example usage
      animated_linear_progress_bar_with_metric("2.35%", "N", 23.5, color='#55a630', width=85,
                                               height=30)
   with col2:
      # Example usage
      animated_linear_progress_bar_with_metric("0.3%", "P", 30, color='#55a630', width=85,
                                               height=30)
   with col12:
      # Example usage
      animated_linear_progress_bar_with_metric("0.2%", "P", 20, color='#55a630', width=85,
                                               height=30)
   with col22:
      # Example usage
      animated_linear_progress_bar_with_metric("0.28%", "P", 28, color='#55a630', width=85,
                                               height=30)

   with col3:
      # Example usage
      animated_linear_progress_bar_with_metric("2.5%", "K", 25, color='#55a630', width=85,
                                               height=30)
   with col13:
      # Example usage
      animated_linear_progress_bar_with_metric("2.12%", "K", 21.2, color='#55a630', width=85,

                                               height=30)
   with col23:
      # Example usage
      animated_linear_progress_bar_with_metric("2.3%", "K", 23, color='#55a630', width=85,
                                               height=30)

   with col4:
      # Example usage
      animated_linear_progress_bar_with_metric("0.155%", "Mg", 15, color='#55a630', width=85,
                                               height=30)

   with col14:
      # Example usage

      animated_linear_progress_bar_with_metric("0.151%", "Mg", 15, color='#55a630', width=85,
                                               height=30)
   with col24:
      # Example usage
      animated_linear_progress_bar_with_metric("0.16%", "Mg", 16, color='#55a630', width=85,
                                               height=30)

   with col5:
      # Example usage
      animated_linear_progress_bar_with_metric("0.27%", "Ca", 27, color='#55a630', width=85,
                                               height=30)
   with col15:
      # Example usage
      animated_linear_progress_bar_with_metric("0.30%", "Ca", 30, color='#55a630', width=85,
                                               height=30)
   with col25:
      # Example usage
      animated_linear_progress_bar_with_metric("0.28%", "Ca", 28, color='#55a630', width=85,
                                               height=30)

if option == 'Season2':
   st.markdown(printCostumTitleAndContenth3(f"Rice trait : {option}",
                                            "what is the Risk level of each growth trait that has been measured."),
               unsafe_allow_html=True)
   col1, col2, col3, col4, col5, col6 = st.columns(6)
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
      progress_html = animated_circular_progress_bar('No. of Filled Grain', current_weight, max_weight,
                                                     color='orange',
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

   st.markdown(printCostumTitleAndContenth3(f"Nutrients Level: {option}",
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
      animated_linear_progress_bar_with_metric("2.8%", "N", 28, color='#55a630', width=85,
                                               height=30)
   with col11:
      # Example usage
      animated_linear_progress_bar_with_metric("2.23%", "N", 22.3, color='#55a630', width=85,
                                               height=30)
   with col21:
      # Example usage
      animated_linear_progress_bar_with_metric("2.8%", "N", 28.5, color='#55a630', width=85,
                                               height=30)
   with col2:
      # Example usage
      animated_linear_progress_bar_with_metric("3.25%", "P", 32.5, color='#55a630', width=85,
                                               height=30)
   with col12:
      # Example usage
      animated_linear_progress_bar_with_metric("2.12%", "P", 21, color='#55a630', width=85,
                                               height=30)
   with col22:
      # Example usage
      animated_linear_progress_bar_with_metric("0.28%", "P", 28, color='#55a630', width=85,
                                               height=30)

   with col3:
      # Example usage
      animated_linear_progress_bar_with_metric("0.14%", "K", 14, color='#55a630', width=85,
                                               height=30)
   with col13:
      # Example usage
      animated_linear_progress_bar_with_metric("0.14%", "K", 14, color='#55a630', width=85,

                                               height=30)
   with col23:
      # Example usage
      animated_linear_progress_bar_with_metric("0.13%", "K", 13, color='#55a630', width=85,
                                               height=30)

   with col4:
      # Example usage
      animated_linear_progress_bar_with_metric("25%", "Mg", 27, color='#55a630', width=85,
                                               height=30)

   with col14:
      # Example usage

      animated_linear_progress_bar_with_metric("55%", "Mg", 55, color='#55a630', width=85,
                                               height=30)
   with col24:
      # Example usage
      animated_linear_progress_bar_with_metric("36%", "Mg", 36, color='#55a630', width=85,
                                               height=30)

   with col5:
      # Example usage
      animated_linear_progress_bar_with_metric("0.55%", "Ca", 55, color='#55a630', width=85,
                                               height=30)
   with col15:
      # Example usage
      animated_linear_progress_bar_with_metric("0.45%", "Ca", 45, color='#55a630', width=85,
                                               height=30)
   with col25:
      # Example usage
      animated_linear_progress_bar_with_metric("0.15%", "Ca", 15, color='#55a630', width=85,
                                               height=30)

if option == 'Season3':
   st.write(farmsdfst.iloc[2])
