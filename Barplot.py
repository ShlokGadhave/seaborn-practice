import seaborn as sns 
import matplotlib.pyplot as plt 
data=sns.load_dataset("titanic")
print(data)
sns.barplot(data=data,x="class",y="sex",color="black",hue="sex",errorbar=("ci",0))
plt.show()