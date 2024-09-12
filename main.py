import pandas as pd
from datetime import datetime
import logging
from alpha_vantage.timeseries import TimeSeries
from sqlalchemy import create_engine


API_KEY = "LVP0FSZDXOBA30HT"    # Replace with own
ts = TimeSeries(key = API_KEY, output_format="pandas")
engine = create_engine('mssql+pyodbc://admin:Logon123@MEGAPC/StockMarket?driver=ODBC+Driver+17+for+SQL+Server')

logging = logging.getLogger()
logging.basicConfig(filename="logfile.log", 
                            filemode='w',
                            level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s'
                            )
logging.info("Main script executing..")


