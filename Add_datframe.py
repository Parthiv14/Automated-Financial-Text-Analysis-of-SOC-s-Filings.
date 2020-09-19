import pandas as pd

df = pd.read_excel ('C:/Users/pares/Desktop/blackcoffer/Output Data Structure.xlsx')


df = 'https://www.sec.gov/Archives/' + df['SECFNAME'].astype(str,int)
#print(df)



df.to_excel('sheet1.xlsx')
