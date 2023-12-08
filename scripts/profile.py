import pandas as pd
from ydata_profiling import ProfileReport

columns=['sepal_len', 'sepal_width', 'petal_len', 'petal_width', 'class']

df_iris = pd.read_csv('data/iris/iris.data',header=None,names=columns)

profile = ProfileReport(df_iris, title='Iris Profiling Report')
profile.to_file('profiling/iris_report.html')