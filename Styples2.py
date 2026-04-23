import seaborn as sns 
import matplotlib.pyplot as plt 
data=sns.load_dataset("exercise")
sns.set_style(style="ticks")
sns.barplot(data=data,x='diet',y='pulse')
plt.show()