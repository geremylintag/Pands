import pandas as pd
a = pd.read_csv('cars.csv')
b = a.head()
c = a.tail()
d = b.append(c)
print(d)