import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('First Streamlit Homework')

st.markdown(
"**QUESTION 1**: I created a sequence of numbers from 0 to 99 with 1 as the common difference from numpy's arrange() function.\n"
"Then I generated some values using numpy's random().rand function.\n"
"I created a dictionary using the two arrays and then passed the dictionary to a dataframe.\n"
"Here is the printout of the dataframe"
)

#st.code(

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(x_limit)

# Create a random array of data that we will use for our y values
y_data = np.random.rand(100)
d={'x': x_axis,'y': y_data}
df = pd.DataFrame(d)
st.write(df)


#st.markdown(
"**QUESTION 2**: With the dataframe above I generated a basic scatterplot of marks as shown below.\n"
#)

#st.code(

scatter = alt.Chart(df).mark_point().encode(x='x',y='y')

st.altair_chart(scatter, use_container_width=True)
#''',language='python')


st.markdown(
"**QUESTION 3**Playing with st.markdown.\n"
"First I made some changes to the plot and then listed them using st.markdown"
)
scatter = alt.Chart(df,title="Some Random Circles").mark_circle().encode(x='x',y='y',size='y',tooltip=['x', 'y']).configure_mark(
    opacity=0.5,
    color='green'
)

st.altair_chart(scatter, use_container_width=True)

st.markdown("I made some Five Changes to the scatter plot of marks as you can see above")
st.markdown("""
The 5 changes I made were:
- I changed the marks to cicles
- I added a size property to the circles
- I coloured the circles green
- I added a title
- I added a tooltip
""")



st.markdown(
"**QUESTION 4**: The following visual is a simple bar chart from https://altair-viz.github.io/gallery/index.html.\n "
"I made two changes to it \n"
)
source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

barchart = alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)
st.altair_chart(barchart, use_container_width=True)

st.markdown("Below is the plot after my changes")
barchart = alt.Chart(source).mark_bar().encode(
    x='b',
    y=alt.Y('a',sort='-x'),
    tooltip =['b']
)
st.altair_chart(barchart, use_container_width=True)

st.markdown("""
The 2 changes I made are:
- I changed the orientation of the bars to horizontal by switching the axis and then sorted the bars
- I added a tooltip to the bars
"""
)
