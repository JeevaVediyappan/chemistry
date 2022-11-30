import pygal
import seaborn as sns # this library for load dataset
df = sns.load_dataset('tips')
#Bar chart
bar_chart = pygal.Bar() 
bar_chart.add('Tip', df['tip']) 
bar_chart.render_to_file('bar_chart1.svg')

#double Bar chart
bar_chart.add('Tip', df['tip'][:10])
bar_chart.add('Total Bill', df['total_bill'][:10])
bar_chart.render_to_file('bar_chart2.svg')

#line chart
line_chart = pygal.Line()
line_chart.add('Total Bill', df['total_bill'][:15])
line_chart.render_to_file('line1.svg')

#double line chart
line_chart.add('Total Bill', df['total_bill'][:15])
line_chart.add('Tips', df['tip'][:15])
line_chart.render_to_file('line2.svg')

#Box plot chart
box_plot = pygal.Box()
box_plot.title = 'Tips Dataset'
box_plot.add('Tips', df['tip'])
box_plot.render_to_file('box1.svg')

#Funnel chart
funnel_chart = pygal.Funnel()
funnel_chart.title = 'Total Bill'
funnel_chart.add('Total Bill', df['total_bill'][:15])
funnel_chart.add('Tip', df['tip'][:15])
         funnel_chart.render_to_file('funnel1.svg')
