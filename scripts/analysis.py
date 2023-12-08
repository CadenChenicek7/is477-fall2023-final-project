import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

columns=['sepal_len', 'sepal_width', 'petal_len', 'petal_width', 'class']
df_iris = pd.read_csv('data/iris/iris.data',header=None,names=columns)

sns.set(style='whitegrid')

plot = sns.FacetGrid(df_iris, hue='class', height=6).map(plt.scatter, 'sepal_len', 'petal_len').add_legend()

file = 'results/iris_vis.png'

plot.savefig(file)


