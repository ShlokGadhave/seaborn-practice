import matplotlib.pyplot as plt 
import seaborn as sns 
data=sns.load_dataset("tips")
sns.violinplot(data=data,x="total_bill")
plt.show()