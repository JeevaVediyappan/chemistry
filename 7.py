from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()  # load dataset

# scatter plots
x_iris = iris.data[:, :2]  # only take the first two features
y_iris = iris.target
n_classes = 3
for i in range(n_classes):
    index = np.where(y_iris == i)
    plt.scatter(x_iris[index, 0], x_iris[index, 1],  
    label=iris.target_names[i])
plt.legend()
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('scatter chart Iris average')
plt.show
plt.savefig('matscatter.png')

# bar chart
X_iris = iris.data
Y_iris = iris.target
n_classes = 3
averages = [X_iris[Y_iris == i].mean(axis=0) for i in range(n_classes)]
x = np.arange(len(iris.feature_names))

fig = plt.figure()
ax = fig.add_subplot()
bar1 = ax.bar(x - 0.25, averages[0], 0.25, label=iris.target_names[0])
bar2 = ax.bar(x, averages[1], 0.25, label=iris.target_names[1])
bar3 = ax.bar(x + 0.25, averages[2], 0.25, label=iris.target_names[2])
ax.set_xticks(x)
ax.set_xticklabels(iris.feature_names)

plt.legend()
plt.title("Bar Chart Iris Averages")
plt.ylabel("Average")
plt.show
plt.savefig('matbarchart.png')

#Histogram
fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(X_iris[:, 0])
axs[0, 1].hist(X_iris[:, 1], color='orange')
axs[1, 0].hist(X_iris[:, 2], color='green')
axs[1, 1].hist(X_iris[:, 3], color='red')

i = 0
for ax in axs.flat:
  ax.set(xlabel=iris.feature_names[i], ylabel='Frequency')
  i += 1
fig.suptitle("Iris Histograms")
fig.savefig('mathisto.png')

#box plot
plt.boxplot(X_iris, labels=[iris.feature_names[0], iris.feature_names[1], 
iris.feature_names[2], iris.feature_names[3]])
plt.title("Boxplots Iris features")
plt.ylabel("cm")
plt.show
plt.savefig('matboxplot.png') 
