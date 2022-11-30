import PySimpleGUI as sg
import seaborn as sns

mpg=sns.load_dataset("mpg")
tips=sns.load_dataset("tips")
bar_chart=sns.barplot(x='day',y='total_bill',data=tips)
bar_chartfig=bar_chart.get_figure()
bar_chartfig.savefig('pusimpleguibarfig.png')

line_chart=sns.boxplot(y=mpg["mpg"])
line_chartfig=line_chart.get_figure()
line_chartfig.savefig('pusimpleguilinefig.png')

barfig_column=[[sg.Image("pusimpleguibarfig.png")]]
linefig_column=[[sg.Image("pusimpleguilinefig.png")]]
layout=[
    [sg.Column(barfig_column),
     sg.VSeperator(),
     sg.Column(linefig_column),
     ]
]
sg.Window(title='MyWindow',layout=layout).read()
 
