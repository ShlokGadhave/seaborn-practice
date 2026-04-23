import matplotlib.pyplot as plt
import seaborn as sns 
data=sns.load_dataset("tips")
sns.swarmplot(data=data,x="total_bill",y="tip")
plt.show() # swarm plot data does not get overlap whereas in strip plot it gets overlap 