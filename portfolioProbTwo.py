import pandas as pd

data = pd.read_excel('portfolioInfo.xlsx')

dvd = data['Notes']
ShareCol = data['Shares']
PriceCol = data['Price']

sum = 0
for i in range(0, len(dvd)):
    if dvd[i]!='dvd':
        sum+= (ShareCol[i]*PriceCol[i])
print(sum)
    