import matplotlib.pyplot as plt 
import seaborn as sns 
data=sns.load_dataset("tips")
sns.histplot(data=data,x="total_bill",hue="tip",kde="True",discrete="True")
plt.show()