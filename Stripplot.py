import matplotlib.pyplot as plt 
import seaborn as sns 
data=sns.load_dataset("iris")
sns.stripplot(data=data,x="sepal_length",y="sepal_width",hue="species",dodge=True,jitter=0.6) #dodge is used to separate the data of the hue 
plt.xlabel("sepal_length",fontsize=2)
plt.show() #jitter is used to separate the data