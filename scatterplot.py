import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd 
data=sns.load_dataset("tips")
print(data)
sns.scatterplot(data=data,x="total_bill",y="tip",hue="day",size="size",marker='o',palette="GnBu")
plt.show()