import pandas as pd


xlsx= pd.ExcelFile('prueba1.xlsx')
print(xlsx.sheet_names) 
df  = xlsx.parse('Sheet')
print(df)





