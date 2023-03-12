import pandas as pd 
import numpy as np

fileName = '/users/sarbinowskiw/Desktop/Prospdata.csv'

def read_market_data(fileName):
    df = pd.read_csv(fileName).fillna("")
    cols = df.columns.tolist()[0].split(';')
    fin = pd.DataFrame(df.iloc[:,0].apply(lambda x: x.split(';')).values.tolist(),columns= cols)
    to_float_cols = ['day','timestamp','bid_price_1','bid_volume_1','bid_price_2','bid_volume_2','bid_price_3','bid_volume_3','ask_price_1','ask_volume_1','ask_price_2','ask_volume_2','ask_price_3','ask_volume_3','mid_price','profit_and_loss']
    fin[to_float_cols] =  fin[to_float_cols].applymap(lambda x: float(x) if x != '' else '')
    return fin

def split_data_by_product(df):
    markets = dict()
    products  = df['product'].unique().tolist()
    for prod in products:
        markets[prod]= df[df['product']==prod]
    return markets
df = read_market_data(fileName)
markets = split_data_by_product(df)
