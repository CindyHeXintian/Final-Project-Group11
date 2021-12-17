import pandas as pd
import pymongo
import requests


mongoClient = pymongo.MongoClient("mongodb+srv://Arjun:Arjun123456@bitcoin.kgktc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
cryptoDB = mongoClient.cryptoDB


def get_dataframe(crypto: str):
    """Return the dataframe for the crypto sympol"""
    cryptoFound = cryptoDB.get_collection(crypto)
    x = cryptoFound.find().next()

    df = pd.DataFrame(x)

    df.drop(["_id"],axis = 1, inplace = True)

    df = df.T
    df.drop(['1a. open (CNY)', '2a. high (CNY)','3a. low (CNY)','4a. close (CNY)','5. volume','6. market cap (USD)'], axis=1, inplace=True)

    df.rename(columns = {'1b. open (USD)':'Open','2b. high (USD)':'High','3b. low (USD)':'Low','4b. close (USD)':'Close'}, inplace = True)
    df.index.name="Month"
    df['Open'] = df['Open'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df.head()

    return df.to_dict()
