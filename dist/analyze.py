import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("./dist/chansey.csv")["HP"]
# df = df.drop(df.columns[:1],axis=1)
arr = df.values.flatten()
print(sum([1 for i in arr if i>=25])/len(arr))
plt.hist(arr,bins=31,density=True)
plt.show()