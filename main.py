import pandas as pd
from datetime import datetime
import logging
from alpha_vantage.timeseries import TimeSeries
from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config.get('API', 'KEY') 
ts = TimeSeries(key = API_KEY, output_format="pandas")
engine = config.get('ENGINE_CON', 'engine_str')
engine = create_engine(engine)

logging.basicConfig(filename="logfile.log", 
                            filemode='w',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s'
                            )
logger = logging.getLogger()