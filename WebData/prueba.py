import re

x="dfsdf d4 dsdas543  ds 543 dsa 23345dfs "

y=re.findall("[a-z0-9]",x)

print(y)
