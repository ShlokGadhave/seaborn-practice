import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
data=sns.load_dataset("tips")
sns.boxplot(data=data)
plt.show()
