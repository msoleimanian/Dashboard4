import streamlit as st
import pandas as pd

# Function to create HTML cell with color based on performance range
def color_cell(value, best_value, lower_limit, upper_limit):
    if value == best_value:
        return f'<span style="background-color: green; padding: 10px; display: block; font-weight: bold;">{value}</span>'
    elif value < best_value * 0.15:
        return f'<span style="background-color:red; padding: 10px; display: block; font-weight: bold;">{value}</span>'
    elif value < best_value * 0.45:
        return f'<span style="background-color: #ff6666; padding: 10px; display: block; font-weight: bold;">{value}</span>'
    elif value < best_value * 0.85:
        return f'<span style="background-color: #ffcc99; padding: 10px; display: block; font-weight: bold;">{value}</span>'
    elif value > best_value * 0.85:
        return f'<span style="background-color: #b3ffb3; padding: 10px; display: block; font-weight: bold;">{value}</span>'

# Data
seasons = ['Season 1', 'Season 2', 'Season 3']
plot_numbers = {'Season 1': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                'Season 2': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                'Season 3': ['Plot1', 'Plot3', 'Plot4', 'Plot5']}

columns = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'SPAD', 'No. of Spikelet',
           'No. of Filled Grain', 'No. Of Unfilled Grain', 'Weight Grain (1000 grains)']

# Create an empty list to store data
data_rows = []

# Populate the data list for data entry
for season in seasons:
    for plot in plot_numbers[season]:
        row = {'Season': season, 'Plot Number': plot}
        for col in columns:
            row[col] = None  # Initialize with None for data entry
        data_rows.append(row)

# Create DataFrame for data entry
data_entry = pd.DataFrame(data_rows)

# Provide a 2D array to fill in the numbers
numbers_to_fill = [
    [98.51, 6, 5, 28.48, 42, 195, 154, 26.27],
    [98, 5, 5, 26.35, 35, 122, 155, 24.26],
    [93.20, 5, 4, 28.81, 27, 137, 46, 25.95],
    [93.99, 7, 5, 32.22, 35, 150, 163, 23.25],

    [103.16, 5, 5, 0, 38, 188, 271, 33.31],
    [98.75, 5, 5, 0, 38, 803, 250, 31.01],
    [88.80, 4, 4, 0, 30, 643, 343, 30.55],
    [92.07, 5, 5, 0, 37, 662, 290, 33.46],

    [100.16, 5, 5, 0, 41, 84, 16, 33.19],
    [96.95, 5, 4, 0, 41, 84, 16, 31.43],
    [88.17, 3, 4, 0, 30, 86, 14, 26.20],
    [93.98, 4, 4, 0, 37, 82, 5, 24.23],
]

# Fill up the DataFrame with the provided numbers
for col_index, col_values in enumerate(zip(*numbers_to_fill)):
    max_value_index = max(enumerate(col_values), key=lambda x: x[1])[0]
    for row_index, value in enumerate(col_values):
        cell_color = color_cell(value, col_values[max_value_index], 0, 1)
        data_entry.at[row_index, columns[col_index]] = cell_color

# HTML styling with inline styles for black text color, thicker black border lines, and increased width
html_code = f"""
    <h1 style="color: #000; text-align: center;">Summary of the farm</h1>
    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
        <tr>
            <th style="border: 2px solid #000; padding: 10px;">Season</th>
            <th style="border: 2px solid #000; padding: 10px;">Plot Number</th>
            {" ".join(f'<th style="border: 2px solid #000; padding: 10px;">{col}</th>' for col in columns)}
        </tr>
        {"".join(
            f"<tr><td style='border: 2px solid #000; padding: 10px;'>{row['Season']}</td><td style='border: 2px solid #000; padding: 10px;'>{row['Plot Number']}</td>"
            + "".join(f"<td style='border: 2px solid #000; padding: 10px;'>{value}</td>" for col, value in zip(columns, data_entry.iloc[row_index, 2:]))
            + "</tr>"
            for row_index, row in data_entry.iterrows()
        )}
    </table>
"""

# Guide content
guide_content = """
## 

- <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: green; margin-right: 5px;"></div> Best Performance
- <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: red; margin-right: 5px;"></div> Poor Performance

For each metric:
- The cell with the **green background** represents the highest value, indicating the best performance.
- The cell with the **red background** represents the lowest value, indicating poor performance.
- The color shades indicate the performance range:
  - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: #ff6666; margin-right: 5px;"></div> Light Red (15-45% with the best)
  - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: #ffcc99; margin-right: 5px;"></div> Orange (45-85% with the best)
  - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: #b3ffb3; margin-right: 5px;"></div> Light Green (45-85% with the best)
"""

# Display the HTML content and the guide
st.header("Performance Guide")
st.markdown(guide_content, unsafe_allow_html=True)
st.markdown(html_code, unsafe_allow_html=True)



# Function to scale the numbers in a column to a 0-10 range
def scale_numbers(column_values):
    max_value = max(column_values)
    return [round((value / max_value) * 10, 2) for value in column_values]

# Function to get color based on percentage difference from the best
def get_color(percent_difference):
    if percent_difference <= 15:
        return 'red'  # Light Red
    elif 15 < percent_difference <= 45:
        return '#b3ffb3'  # Orange
    elif 45 < percent_difference <= 85:
        return '#ff6666'  # Light Green
    else:
        return 'lightblue'  # Light Blue

# Data
seasons = ['Season 1', 'Season 2', 'Season 3']
plot_numbers = {'Season 1': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                'Season 2': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                'Season 3': ['Plot1', 'Plot3', 'Plot4', 'Plot5']}

columns = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'SPAD', 'No. of Spikelet',
           'No. of Filled Grain', 'No. Of Unfilled Grain', 'Weight Grain (1000 grains)']

# Create an empty list to store data
data_rows = []

# Populate the data list for data entry
for season in seasons:
    for plot in plot_numbers[season]:
        row = {'Season': season, 'Plot Number': plot}
        for col in columns:
            row[col] = None  # Initialize with None for data entry
        data_rows.append(row)

# Create DataFrame for data entry
data_entry = pd.DataFrame(data_rows)

# Provide a 2D array to fill in the numbers
numbers_to_fill = [
    [98.51, 6, 5, 28.48, 42, 195, 154, 26.27],
    [98, 5, 5, 26.35, 35, 122, 155, 24.26],
    [93.20, 5, 4, 28.81, 27, 137, 46, 25.95],
    [93.99, 7, 5, 32.22, 35, 150, 163, 23.25],

    [103.16, 5, 5, 0, 38, 188, 271, 33.31],
    [98.75, 5, 5, 0, 38, 803, 250, 31.01],
    [88.80, 4, 4, 0, 30, 643, 343, 30.55],
    [92.07, 5, 5, 0, 37, 662, 290, 33.46],

    [100.16, 5, 5, 0, 41, 84, 16, 33.19],
    [96.95, 5, 4, 0, 41, 84, 16, 31.43],
    [88.17, 3, 4, 0, 30, 86, 14, 26.20],
    [93.98, 4, 4, 0, 37, 82, 5, 24.23],
]

# Fill up the DataFrame with the provided numbers
for col_index, col_values in enumerate(zip(*numbers_to_fill)):
    for row_index, value in enumerate(col_values):
        data_entry.at[row_index, columns[col_index]] = value

# Scale the numbers and sum each row
scaled_data = data_entry.copy()
for col in columns:
    scaled_values = scale_numbers(data_entry[col])
    scaled_data[col] = scaled_values

scaled_data['Total Score'] = scaled_data[columns].sum(axis=1)

# Find the best and worst total scores
max_total_score = scaled_data['Total Score'].max()
min_total_score = scaled_data['Total Score'].min()

# HTML styling with inline styles for black text color, thicker black border lines, and increased width
html_code = f"""
    <h1 style="color: #000; text-align: center;">Season Scores</h1>
    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
        <tr>
            <th style="border: 2px solid #000; padding: 10px;">Season</th>
            <th style="border: 2px solid #000; padding: 10px;">Plot Number</th>
            <th style="border: 2px solid #000; padding: 10px;">Total Score</th>
        </tr>
        {"".join(
            f"<tr><td style='border: 2px solid #000; padding: 10px;'>{row['Season']}</td>"
            f"<td style='border: 2px solid #000; padding: 10px;'>{row['Plot Number']}</td>"
            f"<td style='border: 2px solid #000; padding: 10px; "
            f"background-color: {get_color((100 - row['Total Score']))};'>"
            f"{row['Total Score']}</td></tr>"
            for _, row in scaled_data.iterrows()
        )}
    </table>
"""

# Display the HTML content
st.markdown(html_code, unsafe_allow_html=True)


