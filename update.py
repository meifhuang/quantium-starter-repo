import csv
import pandas as pd


df_sale_0 = pd.read_csv('./data/daily_sales_data_0.csv')
df_sale_1 = pd.read_csv('./data/daily_sales_data_1.csv')
df_sale_2 = pd.read_csv('./data/daily_sales_data_2.csv')

dfs = [df_sale_0, df_sale_1, df_sale_2]

# df_0 = df_sale_0.query('product == "pink morsel"')
# df_1 = df_sale_1.query('product == "pink morsel"')
# df_2 = df_sale_2.query('product == "pink morsel"')


for x in range(3):
    df = pd.read_csv(f"./data/daily_sales_data_{x}.csv")
    pink_morsel = df.query('product == "pink morsel"')
    price = pink_morsel['price'].str.replace('$','').apply(float)
    pink_morsel['sale'] = price * pink_morsel["quantity"]
    print(pink_morsel, x, pink_morsel.shape)
    pink_morsel.drop(columns=['price','quantity'])
    pink_morsel.to_csv('updated_data.csv',mode='a', index=False, header=False)
    print(f'round {x}: {pink_morsel.shape}')


