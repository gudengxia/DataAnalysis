import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set()
#plt.figure()
#sb.set_style('white') 
#sb.barplot(x=x,y=y,data=dataset)
#plt.savefig('test.png')

#df = pd.read_csv('akcn.csv') 
df = pd.read_csv('output.csv')
#df = pd.concat([df1, df2], ignore_index=True)
#print(df)
xx = [i for i in range(21)]
#g = sns.relplot(x=xx, y='mean', kind='line', data=df[3,7])
#g.fig.autofmt_xdate()
ax = sns.lineplot(data=[df['mean-1'], df['mean-2']])
plt.show()
