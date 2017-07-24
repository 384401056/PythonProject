# import pandas as pd
# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# %matplotlib inline
# import numpy as np
#
# df = pd.read_csv('iris.data', names=['sepal lenght','sepal width','petal length','petal width','class'])
#
# fig, ax = plt.subplots(2,2, figsize=(6, 4))
#
# ax[0][0].hist(df['sepal lenght'], color='green')
# ax[0][0].set_ylabel('Count', fontsize = 12)
# ax[0][0].set_xlabel('Width', fontsize = 12)
# ax[0][0].set_title('Iris sepal Lenght', fontsize = 14, y = 1.01)
#
# ax[0][1].hist(df['sepal width'], color='red')
# ax[0][1].set_ylabel('Count', fontsize = 12)
# ax[0][1].set_xlabel('Width', fontsize = 12)
# ax[0][1].set_title('Iris sepal width', fontsize = 14, y = 1.01)
#
# ax[1][0].hist(df['petal lenght'], color='blue')
# ax[1][0].set_ylabel('Count', fontsize = 12)
# ax[1][0].set_xlabel('Width', fontsize = 12)
# ax[1][0].set_title('Iris Petal Lenght', fontsize = 14, y = 1.01)
#
# ax[1][1].hist(df['petal width'], color='black')
# ax[1][1].set_ylabel('Count', fontsize = 12)
# ax[1][1].set_xlabel('Width', fontsize = 12)
# ax[1][1].set_title('Iris Petal Width', fontsize = 14, y = 1.01)
#
# plt.tight_layout()
