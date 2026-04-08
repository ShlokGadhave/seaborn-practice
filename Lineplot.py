import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
data={"Days":[1,2,3,4,5],"NOP":[20,30,50,70,80]}
df=pd.DataFrame(data)
print(df)
sns.lineplot(data=data,x="Days",y="NOP")
plt.show()