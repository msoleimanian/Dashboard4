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
        <td>7.45</td>
    </tr>
    <tr>
        <td>2</td>
        <td>9.59</td>
    </tr>
    <tr>
        <td>3</td>
        <td>8.59</td>
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