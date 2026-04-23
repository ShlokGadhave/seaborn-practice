import matplotlib.pyplot as plt
import seaborn as sns 
data=sns.load_dataset("tips")
a=sns.FacetGrid(data,col="sex",height=5)
a.map_dataframe(sns.histplot,x="total_bill")
plt.show()