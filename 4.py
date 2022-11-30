import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
df = sns.load_dataset('mpg') #importing dataset  
df.shape
df.keys()

#Scatter chart
chart1=alt.Chart(df).mark_point().encode(alt.Y('mpg'),alt.X('horsepower'),alt.Color('origin'),alt.OpacityValue(0.7),size='displacement')
chart1.save('altairchart1.html')

#Bubble chart
chart4=alt.Chart(df).mark_point(filled=True).encode(x='horsepower',y='mpg',  size='displacement',color='origin')
chart4.save('altairchart4.html')

#Line chart
chart2=alt.Chart(df).mark_line().encode(alt.X('horsepower'),alt.Y('acceleration'), alt.Color('origin'))
chart2.save('altairchart2.html')

#bar chart
plot=alt.Chart(df).mark_bar(size=40).encode(alt.X('cylinders'),alt.Y('mpg'),
    alt.Color('origin'))
plot.properties(title='cylinders vs mpg')
plot.save('altairchart4.html')

#Strip plots
chart3=alt.Chart(df).mark_tick(filled=True).encode(x='horsepower:Q',y='cylinders:O',
    color='origin')
chart3.save('altairchart3.html') 
