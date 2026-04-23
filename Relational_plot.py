import seaborn as sns 
import matplotlib.pyplot as plt 
data=sns.load_dataset("tips")
sns.relplot(data=data,x="total_bill",y="tip",kind="line",col="sex",height=2,size="smoker")
plt.show()