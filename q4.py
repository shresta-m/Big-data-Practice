import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_set = pd.read_csv("Iris_dataset.csv")
data_x = data_set[data_set['petal.length'] != 1 or 51 or 101]
print(data_x)
# sns.scatterplot(data = data_set , x= 'petal.length',y = 'petal.width' , hue ='variety' )
# plt.show()