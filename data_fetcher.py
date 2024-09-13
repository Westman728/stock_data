from typechecker import type_checker
from main import engine
from main import logging
from main import ts

data_list = ("MSFT", "AAPL", "DIS", "NFLX")
ticker_data = {}


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
    ticker_data[ticker].to_sql("stock_data", con=engine, if_exists="append", index=False)
    logging.info(f"Data-fetch for iteration: {idx}:{ticker} complete.")