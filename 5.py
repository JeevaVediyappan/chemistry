import seaborn as sns 
from bokeh.palettes import GnBu5
from bokeh.plotting import figure, show,output_file
import pandas as pd
import numpy as np
from bokeh.palettes import Spectral7
from bokeh.models import Title
from bokeh.transform import linear_cmap
from bokeh.models import ColorBar, ColumnDataSource
from bokeh.palettes import Spectral6


df = sns.load_dataset('diamonds')
data = df.sample(53940, random_state=34500)

#data plotting bubble chat

y = list(data.price.values)
x = list(data.carat.values)
mapper=linear_cmap(field_name="y",palette=Spectral6,low=min(y),high=max(y))
source = ColumnDataSource(dict(x=x,y=y))
p = figure(width=800, height=400)
p.circle(x='x', y='y', line_color=mapper, color=mapper, fill_alpha=1, size=12, 
source=source)

color_bar = ColorBar(color_mapper=mapper['transform'], height=300, width=10)
p.add_layout(color_bar, 'right')
output_file('bohakbubble.html')

# data plotting barchat
from bokeh.palettes import Spectral7
from bokeh.models import Title

# prepare the colors and their value counts
colors = sorted(list(data.color.unique()))
counts = [i for i in data.color.value_counts().sort_index()]

p = figure(x_range=colors, width=800, height=400)
p.vbar(x=colors, top=counts, width=0.9, color=Spectral7)
p.y_range.start = 0
p.add_layout(Title(text="Colors", align="center"), "below")
p.add_layout(Title(text="Color counts", align="center"), "left")
output_file('bohakcolorbar.html')

# interactive bar chat
colors = list(data.color.unique()) 

ideal = [data[(data.cut == "Ideal") & (data.color == colors[i])].shape[0] for i in range(len(colors))]
very_good = [data[(data.cut == "Very Good") & (data.color == colors[i])].shape[0] for i in range(len(colors))]
premium = [data[(data.cut == "Premium") & (data.color == colors[i])].shape[0] for i in range(len(colors))]
good = [data[(data.cut == "Good") & (data.color == colors[i])].shape[0] for i in range(len(colors))]
fair = [data[(data.cut == "Fair") & (data.color == colors[i])].shape[0] for i in range(len(colors))]

cut = list(data.cut.unique())

data_stacked = {'colors': colors,
                'Ideal': ideal,
                'Very Good': very_good,
                'Premium': premium, 
                'Good': good, 
                'Fair': fair}

p = figure(x_range=colors, width=800, height=400, title="colors counts by cut",
           toolbar_location=None, tools="hover")

p.vbar_stack(cut, x='colors', width=0.9, color=GnBu5, source=data_stacked,
             legend_label=cut)
p.y_range.start = 0
p.y_range.end = 1000
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
p.legend.click_policy="hide"
output_file('interactivebar.html')
show(p)
 
