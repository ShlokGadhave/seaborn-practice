import matplotlib.pyplot as plt 
import seaborn as sns 
data=sns.load_dataset("tips")
sns.kdeplot(data=data,x="total_bill",hue="day",multiple="fill") #mutiple:stack
plt.show()