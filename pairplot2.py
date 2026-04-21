import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
data=sns.load_dataset("iris")
sns.pairplot(data=data,hue="species",palette="GnBu")
plt.show()