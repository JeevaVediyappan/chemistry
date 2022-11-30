import numpy as np 
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import statsmodels.api as sm

df = sns.load_dataset('iris')

fig = px.scatter(df, x="sepal_width", y="sepal_length", color='species')
fig.show()
fig.write_html("plotlyscater1.html")

fig = px.scatter(df, y="petal_length", x="petal_width", color="species", symbol="species")
fig.update_traces(marker_size=10)
fig.write_html("plotlyscater2.html")
#scatter plot
tips = sns.load_dataset('tips')
fig = px.scatter(tips, x="total_bill", y="tip", trendline="ols")
fig.show()
fig.write_html("plotlyscater3.html")
#line chart
stk = sns.load_dataset('stock')
fig = px.line(stk, x='date', y=["MSFT","GOOG",'FB',"AMZN"])
fig.show()
fig.write_html("plotlyline1.html")

# Line plot
gm = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(gm, x='year', y='pop', color='country',markers=True)
fig.show()
fig.write_html("plotlyline2.html")

#combined plots
N=100
random_x = np.linspace(0, 5, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='lines',
                    name='lines'))
fig.show()
fig.write_html("plotlyinteraction.html")
