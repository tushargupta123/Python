import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("Book1.csv")
print(data)
df=pd.DataFrame(data)
df.plot(kind="line",color=["red","yellow"],x="name")
plt.show()

