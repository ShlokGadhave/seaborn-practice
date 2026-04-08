import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
color=sns.color_palette("GnBu")
sns.lineplot(data=data,x="Amount",y="Payment Mode",hue="Category",palette=color)
plt.show() #hue is basically used to compare the multiple categories 