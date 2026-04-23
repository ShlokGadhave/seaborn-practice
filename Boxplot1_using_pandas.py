import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
print(data)
sns.boxplot(data=data,x='Category',y='Amount',orient='vertical',fliersize=2) #filers ae the small dots autside the box 
plt.show() #box plot works only with vairables 