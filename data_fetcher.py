""" A loop that fetches, transforms and sends the data to a SQL server via Pandas to_sql command. Add tickers to data_list to extend the data fetched.
Fetches data from the previous 5 months by default."""
from typechecker import type_checker
from main import engine
from main import logging
from main import ts
from main import datetime, date

data_list = ("MSFT", "AAPL", "DIS", "NFLX")
ticker_data = {}

# Added "id" column for possibility to separate stock tickers (could also insert the ticker itself). Use replace or append when feeding the SQL server, whichever is appropriate
for idx, ticker in enumerate(data_list, start=1):
    logging.info(f"Starting data-fetching process iteration: {idx}:{ticker}.")
    data = ts.get_daily(ticker)
    df = data[0]
    df = df.rename(columns={"1. open":"open", 
                            "2. high":"high", 
                            "3. low":"low", 
                            "4. close":"close", 
                            "5. volume":"volume"
                            })
    df = df.reset_index()
    df["id"] = idx
    df["date"] = df["date"].dt.date
    df["volume"] = df["volume"].astype(int)
    for entry in df["date"]:
        type_checker.check_date(entry)
    for column in ["open", "high", "low", "close"]:
        df[column] = df[column].apply(type_checker.check_float)
    for entry in df["volume"]:
        type_checker.check_int(entry)
    ticker_data[ticker] = df
    ticker_data[ticker].to_sql("stock_data", con=engine, if_exists="replace", index=False)
    logging.info(f"Data-fetch for iteration: {idx}:{ticker} complete.")