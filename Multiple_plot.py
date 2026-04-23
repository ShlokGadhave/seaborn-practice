import matplotlib.pyplot as plt 
import seaborn as sns 
data=sns.load_dataset("tips")
a=sns.FacetGrid(data,col="time",height=5)
a.map(sns.barplot,"day","tip")
plt.show()