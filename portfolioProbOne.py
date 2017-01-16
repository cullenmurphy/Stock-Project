import pandas as pd



data = pd.read_excel('portfolioInfo.xlsx')

ShareCol = data['Shares']
PriceCol = data['Price']

sumA = 0
for i in range(0, len(ShareCol)):
    sumA+=(PriceCol[i]*ShareCol[i])
    
print(sumA)
