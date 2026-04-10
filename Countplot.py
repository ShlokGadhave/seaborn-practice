import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
data=sns.load_dataset("tips")
print(data)
sns.countplot(data=data,x="day",palette="spring")
plt.show()