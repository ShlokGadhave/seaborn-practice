import seaborn as sns 
import matplotlib.pyplot as plt 
data=sns.load_dataset("tips")
sns.catplot(data=data,x="sex",y="tip",kind="violin",hue="time")
plt.show() #catplot stands for categorical plot 