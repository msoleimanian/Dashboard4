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


def color_cell2(best_value, value, lower_limit, upper_limit):
    if value == best_value:
        return f'green'
    elif value < best_value * 0.15:
        return f'red'
    elif value < best_value * 0.45:
        return f'#ff6666'
    elif value < best_value * 0.85:
        return f'#ffcc99'
    elif value > best_value * 0.85:
        return f'#b3ffb3'

# Data



option2 = st.sidebar.selectbox(
   "Select the Farm",
   ("Pak choy", "Rice", "Aqua"),
   index=1,
   placeholder="Select the farm...",
)

if option2 == "Rice":

    performance_text = """
    On the Performance Page, witness the epic saga of crop seasons and generations. Our cutting-edge system meticulously scores each season or generation, evaluating crucial crop traits. The comparison unfolds, revealing how other plots and pots measure up to the best. Behold the vibrant landscape, color-coded to showcase the performance hierarchy. Embark on this animated journey where each plot and pot tells a unique tale!
    """

    seasons = ['Season 1', 'Season 2', 'Season 3']
    plot_numbers = {'Season 1': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                    'Season 2': ['Plot1', 'Plot3', 'Plot4', 'Plot5'],
                    'Season 3': ['Plot1', 'Plot3', 'Plot4', 'Plot5']}

    columns = ['Plant Height', 'No. of Tiller', 'No. of Panicle', 'No. of Spikelet',
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
        [98.51, 6, 5,  42, 195, 154, 26.27],
        [98, 5, 5,  35, 122, 155, 24.26],
        [93.20, 5, 4,  27, 137, 46, 25.95],
        [93.99, 7, 5,  35, 150, 163, 23.25],

        [103.16, 5, 5,  38, 188, 271, 33.31],
        [98.75, 5, 5, 38, 803, 250, 31.01],
        [88.80, 4, 4,  30, 643, 343, 30.55],
        [92.07, 5, 5, 37, 662, 290, 33.46],

        [100.16, 5, 5, 41, 84, 16, 33.19],
        [96.95, 5, 4,  41, 84, 16, 31.43],
        [88.17, 3, 4,  30, 86, 14, 26.20],
        [93.98, 4, 4,  37, 82, 5, 24.23],
    ]

    # Fill up the DataFrame with the provided numbers
    for col_index, col_values in enumerate(zip(*numbers_to_fill)):
        max_value_index = max(enumerate(col_values), key=lambda x: x[1])[0]
        for row_index, value in enumerate(col_values):
            cell_color = color_cell(value, col_values[max_value_index], 0, 1)
            data_entry.at[row_index, columns[col_index]] = cell_color

    # HTML styling with inline styles for black text color, thicker black border lines, and increased width

    html_code = f"""
        <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">
        <h2 style="color: #000; text-align: center;">Performance Table</h2>
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
        </div>
    """
    # Guide content
    guide_content = """
    ## 
    <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">
    <h3>Performance Guide</h3>
    
    - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: green; margin-right: 5px;"></div> Best Performance
    - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: red; margin-right: 5px;"></div> Poor Performance
    
    For each metric:
    - The cell with the **green background** represents the highest value, indicating the best performance.
    - The cell with the **red background** represents the lowest value, indicating poor performance.
    - The color shades indicate the performance range:
      - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: #ff6666; margin-right: 5px;"></div> Light Red (15-45% with the best)
      - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: #ffcc99; margin-right: 5px;"></div> Orange (45-85% with the best)
      - <div style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; background-color: #b3ffb3; margin-right: 5px;"></div> Light Green (45-85% with the best)
    </div>
    """

    # Display the HTML content and the guide
    #st.markdown(guide_content, unsafe_allow_html=True)
    st.write("")
    st.markdown(html_code, unsafe_allow_html=True)



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


    st.markdown(printCostumTitleAndContenth2("Select Season and Plot",
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

def get_color(percent_difference):
    if percent_difference == 0:
        return 'green'  # Light Red
    elif 0 < percent_difference <= 1.5:
        return '#b3ffb3'
    elif 1.5 < percent_difference <= 3:
        return 'orange'
    elif 3 < percent_difference <= 3.5:
        return '#ff6666'
    else:
        return 'red'
if option2 == 'Pak choy':


    # Create DataFrame
    df = pd.read_csv('Dataset/Pock choy /generation.csv')
    # Filter columns
    filtered_df = df[['generation', 'pot', 'leavescount', 'longestleaf', 'plantheight']]

    # Group by pot and subpot, calculate averages
    grouped_df = filtered_df.groupby(['generation', 'pot']).mean().reset_index()

    # Scale the values based on the height (score)
    max_score = 10
    height_scaling = max_score / grouped_df['plantheight'].max()
    grouped_df['score'] = grouped_df['plantheight'] * height_scaling

    # HTML code
    html_code_packchoy = f"""
            <div style="background-color:#f4f4f4;padding:20px;border-radius:10px">
                <h5> </h5>
                <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                    <tr>
                        <th style="border: 2px solid #000; padding: 10px;">Generation</th>
                        <th style="border: 2px solid #000; padding: 10px;">Pot Number</th>
                        <th style="border: 2px solid #000; padding: 10px;">Score</th>
                        <th style="border: 2px solid #000; padding: 10px;">AVG Plant Height</th>
                        <th style="border: 2px solid #000; padding: 10px;">AVG Longest leaf</th>
                        <th style="border: 2px solid #000; padding: 10px;">AVG leaves count</th>
                    </tr>
                    {''.join([f'<tr><td style="border: 2px solid #000; padding: 10px;">{row["generation"]}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px;">{row["pot"]}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px; background-color: {color_cell2(10 , min(row["score"], max_score) , 0 ,1 )}">{min(row["score"], max_score):.2f}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px; background-color: {color_cell2(214.25 , row["plantheight"], 0 ,1)}">{row["plantheight"]:.2f}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px; background-color: {color_cell2(214.25 , row["plantheight"], 0 ,1)}">{row["plantheight"]:.2f}</td>'
                              f'<td style="border: 2px solid #000; padding: 10px; background-color: {color_cell2(214.25 , row["plantheight"], 0 ,1)}">{row["plantheight"]:.2f}</td></tr>'
                              for index, row in grouped_df.iterrows()])}
                </table>
            </div>
        """

    # Streamlit app
    st.markdown(html_code_packchoy, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(printCostumTitleAndContenth3("Generaion1", ""), unsafe_allow_html=True)

        st.write("High Value Trait")
        max_weight = 214.25  # Maximum weight in KG
        current_weight = 128  # Current weight in KG
        progress_html = animated_circular_progress_bar('AVG Plant Height', current_weight, max_weight,
                                                       color='green',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)

    with col2:
        st.markdown(printCostumTitleAndContenth3("Pot1", ""), unsafe_allow_html=True)

        st.write("High Value Trait")
        max_weight = 214.25  # Maximum weight in KG
        current_weight = 214.25  # Current weight in KG
        progress_html = animated_circular_progress_bar('AVG Plant Height', current_weight, max_weight,
                                                       color='green',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)

    st.markdown(printCostumTitleAndContenth2("Select Season and Plot",
                                             ""),
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        optionseasson = st.selectbox(
            "Select the Generation...",
            ("1", "2"),
            index=0,
            placeholder="Select the farm...",
        )

    with col2:
        optionplot = st.selectbox(
            "Select the Pot...",
            ("1", "2"),
            index=0,
            placeholder="Select the farm...",
        )



    dfs = pd.read_csv(f'Dataset/Pock choy /generation.csv')
    print(dfs)

    dfp1 = dfs.query(f"""generation == {optionseasson}""")
    dfp2 = dfs.query(f"""pot == {optionplot} & generation == {optionseasson}""")
    print(dfp1)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(printCostumTitleAndContenth3(f"Generation{optionseasson}", ""), unsafe_allow_html=True)
        st.write("High Value Trait")
        max_weight = 214.25   # Maximum weight in KG
        current_weight = dfp1['plantheight'].mean()  # Current weight in KG
        progress_html = animated_circular_progress_bar('AVG Plant Height', current_weight, max_weight,
                                                       color='green',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)

    with col2:
        st.markdown(printCostumTitleAndContenth3(f"Plot{optionplot}", ""), unsafe_allow_html=True)
        st.write("High Value Trait")
        max_weight = 214.25   # Maximum weight in KG
        current_weight = dfp2['plantheight'].mean()  # Current weight in KG
        progress_html = animated_circular_progress_bar('AVG Plant Height', current_weight, max_weight,
                                                       color='green',
                                                       max_size=200)
        st.components.v1.html(progress_html, height=210)

    df = pd.read_csv(f'Dataset/Rice/Season{optionseasson}.csv')
    df = df.query(f"""Plot == 'P{optionplot}'""")
    st.markdown(printCostumTitleAndContenth3(f"Nutrients Level",
                                             ""),
                unsafe_allow_html=True)

    df = pd.read_csv(f'Dataset/Pock choy /PackchoyGeneration2.csv')
    # Calculate the day count for each unique date
    df['Day'] = df['Date'].rank(method='dense').astype(int)
    # Keep only the relevant columns
    df = df[['Day', 'Pot', 'SubPot', 'EC', 'pH', 'Leaves Count', 'Longest Leaf', 'Plant Height(mm)']]
    # Display the modified DataFrame
    print("####################")
    fn2 = df.query(f"""Day == 2""")
    fn3 = df.query(f"""Day == 3""")
    fn4 = df.query(f"""Day == 4""")
    fn5 = df.query(f"""Day == 5""")
    fn6 = df.query(f"""Day == 6""")
    fn7 = df.query(f"""Day == 7""")
    fn8 = df.query(f"""Day == 8""")
    fn9 = df.query(f"""Day == 9""")
    fn10 = df.query(f"""Day == 10""")
    fn11 = df.query(f"""Day == 11""")
    print(df)


    dfbest = pd.read_csv(f'Dataset/Pock choy /PackchoyGeneration1.csv')
    # Calculate the day count for each unique date
    dfbest['Day'] = dfbest['Date'].rank(method='dense').astype(int)
    # Keep only the relevant columns
    dfbest = dfbest[['Day', 'Pot', 'SubPot', 'EC', 'pH', 'Leaves Count', 'Longest Leaf', 'Plant Height(mm)']]
    # Display the modified DataFrame
    print("####################")
    print(dfbest)
    nutrients = ['EC', 'pH']
    fnbest2 = dfbest.query(f"""Day == 2""")
    fnbest3 = dfbest.query(f"""Day == 3""")
    fnbest4 = dfbest.query(f"""Day == 4""")
    fnbest5 = dfbest.query(f"""Day == 5""")
    fnbest6 = dfbest.query(f"""Day == 6""")
    fnbest7 = dfbest.query(f"""Day == 7""")
    fnbest8 = dfbest.query(f"""Day == 8""")
    fnbest9 = dfbest.query(f"""Day == 9""")
    fnbest10 = dfbest.query(f"""Day == 10""")
    fnbest11 = dfbest.query(f"""Day == 11""")
    for i in range(2):
        n = nutrients[i]
        nutrient_data = {f'{n} generation1 pot1 (Best Performance)': [fnbest2[nutrients[i]].values[0],
                                                                  fnbest3[nutrients[i]].values[0],
                                                                  fnbest4[nutrients[i]].values[0],
                                                                  fnbest5[nutrients[i]].values[0],
                                                                  fnbest6[nutrients[i]].values[0],
                                                                  fnbest7[nutrients[i]].values[0],
                                                                  fnbest8[nutrients[i]].values[0],
                                                                  fnbest9[nutrients[i]].values[0],
                                                                  fnbest10[nutrients[i]].values[0],
                                                                  fnbest11[nutrients[i]].values[0]] ,
                         f'{nutrients[i]} generation{optionseasson} pot{optionplot}(Selected generation)': [
                             fn2[nutrients[i]].values[0], fn3[nutrients[i]].values[0],
                             fn4[nutrients[i]].values[0],
                             fn5[nutrients[i]].values[0],
                             fn6[nutrients[i]].values[0],
                             fn7[nutrients[i]].values[0],
                             fn8[nutrients[i]].values[0],
                             fn9[nutrients[i]].values[0],
                             fn10[nutrients[i]].values[0],
                             fn10[nutrients[i]].values[0]]}

        # Create a DataFrame with the dictionary
        df = pd.DataFrame.from_dict(nutrient_data, orient='index', columns=[2, 3, 4,5,6,7,8,9,10,11])

        # Animated line chart with Plot
        fig = px.line(df.transpose(), x=df.columns, y=df.index,
                      labels={'value': 'Nutrient Level', 'variable': 'Nutrient'},
                      title=n)
        fig.update_layout(xaxis_title='DAYS')
        fig.update_traces(mode='lines+markers')

        # Display the animated chart
        st.plotly_chart(fig)

if option2 == "Aqua":
    st.title('the growth rate of the Fishes')
    # Load the CSV data
    df = pd.read_csv('Dataset/Aqua/GrowthRate.csv')

    # Highlight rows with negative growth rates using a custom CSS class
    def highlight_negative(val):
        color = 'red' if '-' in str(val) else 'black'
        return f'color: {color}; background-color: #FFD2D2' if color == 'red' else ''


    # Apply the custom styling
    styled_df = df.style.applymap(highlight_negative, subset=['GROWTH RATE LENGTH', 'GROWTH RATE WEIGHT'])

    # Display the table using Streamlit
    st.write(styled_df.to_html(classes='data-table', escape=False), unsafe_allow_html=True)

    import streamlit as st
    import pandas as pd
    import io
    import plotly.express as px

    # Load the dataset
    data = """Date,Temperature,pH,Ammonia,DO,Salinity,LENGTH (cm),WEIGHT (kg)
    4-Jul-23,26.69,4.89,0.27,8.2,30,55.6,2.04
    11-Jul-23,26.69,4.89,0.27,8.2,30,55.8,1.76
    18-Jul-23,26.69,4.89,0.27,8.2,30,56,1.7
    25-Jul-23,26.69,4.89,0.27,8.2,30,56.2,1.64
    1-Aug-23,26.69,4.89,0.27,8.2,30,56.5,1.96
    8-Aug-23,26.69,4.89,0.27,8.2,30,56.6,1.98
    15-Aug-23,26.69,4.89,0.27,8.2,30,56.7,1.37
    22-Aug-23,26.69,4.89,0.27,8.2,30,56.8,1.82
    29-Aug-23,27.88,6.33,0.46,6.54,29.79,57,1.9
    5-Sep-23,27.88,5.66,0.28,5.99,29.6,57.2,2
    12-Sep-23,29.56,6.98,0.29,6.54,29.78,57.4,2.01
    19-Sep-23,28.81,7.17,0.27,7.1,30.17,57.5,1.9
    26-Sep-23,29.56,17.67,0.02,5.99,29.81,57.8,1.93"""

    # Convert the string data to a DataFrame
    df = pd.read_csv(io.StringIO(data))

    # Display the dataset

    # Plot line charts for Temperature, pH, Ammonia, DO, and Salinity with anomalies highlighted
    fig_temperature = px.line(df, x='Date', y='Temperature', title='Temperature Trend')
    fig_temperature.add_scatter(x=df['Date'][df['Temperature'] < df['Temperature'].mean() - df['Temperature'].std()],
                                y=df['Temperature'][
                                    df['Temperature'] < df['Temperature'].mean() - df['Temperature'].std()],
                                mode='markers', marker=dict(color='red'), name='Anomaly')
    fig_temperature.update_layout(xaxis_title='Date', yaxis_title='Temperature (°C)')

    fig_pH = px.line(df, x='Date', y='pH', title='pH Trend')
    fig_pH.add_scatter(x=df['Date'][df['pH'] < df['pH'].mean() - df['pH'].std()],
                       y=df['pH'][df['pH'] < df['pH'].mean() - df['pH'].std()],
                       mode='markers', marker=dict(color='red'), name='Anomaly')
    fig_pH.update_layout(xaxis_title='Date', yaxis_title='pH')

    fig_ammonia = px.line(df, x='Date', y='Ammonia', title='Ammonia Trend')
    fig_ammonia.add_scatter(x=df['Date'][df['Ammonia'] > df['Ammonia'].mean() + df['Ammonia'].std()],
                            y=df['Ammonia'][df['Ammonia'] > df['Ammonia'].mean() + df['Ammonia'].std()],
                            mode='markers', marker=dict(color='red'), name='Anomaly')
    fig_ammonia.update_layout(xaxis_title='Date', yaxis_title='Ammonia')

    fig_DO = px.line(df, x='Date', y='DO', title='DO Trend')
    fig_DO.add_scatter(x=df['Date'][df['DO'] < df['DO'].mean() - df['DO'].std()],
                       y=df['DO'][df['DO'] < df['DO'].mean() - df['DO'].std()],
                       mode='markers', marker=dict(color='red'), name='Anomaly')
    fig_DO.update_layout(xaxis_title='Date', yaxis_title='DO')

    fig_salinity = px.line(df, x='Date', y='Salinity', title='Salinity Trend')
    fig_salinity.add_scatter(x=df['Date'][df['Salinity'] > df['Salinity'].mean() + df['Salinity'].std()],
                             y=df['Salinity'][df['Salinity'] > df['Salinity'].mean() + df['Salinity'].std()],
                             mode='markers', marker=dict(color='red'), name='Anomaly')
    fig_salinity.update_layout(xaxis_title='Date', yaxis_title='Salinity')

    # Display line charts
    st.plotly_chart(fig_temperature)
    st.plotly_chart(fig_pH)
    st.plotly_chart(fig_ammonia)
    st.plotly_chart(fig_DO)
    st.plotly_chart(fig_salinity)