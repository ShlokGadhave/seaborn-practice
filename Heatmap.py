import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
data=sns.load_dataset("tips")
print(data)
group=data.groupby("total_bill").agg({"tip":"mean"})
sns.heatmap(group)
plt.show()