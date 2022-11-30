

import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")
tips= sns.load_dataset("tips")
iris = sns.load_dataset("iris")
fmri = sns.load_dataset("fmri")

# boxplot
sns.boxplot(y = mpg["mpg"]) 
plt.savefig("seabornbox.png")

# scatterplot
sns.scatterplot(x = "sepal_length", y = "petal_length", data = iris) 
plt.savefig("seabornscatter.png")

# trend line
sns.lmplot(x = "sepal_length", y = "petal_length", data = iris, scatter = False)
plt.savefig("seaborntrend.png")

# bar chart
sns.barplot(x = "day", y = "total_bill", data = tips)
plt.savefig("seabornbar.png")

# line chart/time series
sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri)
plt.savefig("seabornline.png")
 
