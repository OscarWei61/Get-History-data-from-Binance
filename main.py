from binance import Client
from tqdm import tqdm
import pandas as pd
import datetime

def example_get_historical_klines(client):

    # Example:
    # Fetch 1 minute klines for the last day up until now
    history_data = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

    # Fetch 30 minute klines for the last month of 2017
    history_data = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

    # Fetch weekly klines since it listed
    history_data = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

def main():
    
    start_time = datetime.datetime.now()

    # Fetching history data do not actually need your api key 
    API_key = "xxx"
    API_Secret_key = "xxx"
    client = Client(API_key, API_Secret_key)

    Time_spot = []
    Open = []
    High = []
    Low = []
    Close = []
    Volume = []

    # Get 1h data from 1 Dec, 2023 to 2 Dec, 2023
    history_data = client.get_historical_klines("BTCUSDT", '1h', "1 Dec, 2023", "2 Dec, 2023")
    # Symbol option: BTCUSDT, BNBBTC, NEOUSDT, ETHBTC
    # Interval option: 1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M

    # Analysis response history information
    for num in tqdm(range(0, len(history_data))):
        Time_spot.append(history_data[num][0])
        Open.append(history_data[num][1])
        High.append(history_data[num][2])
        Low.append(history_data[num][3])
        Close.append(history_data[num][4])
        Volume.append(history_data[num][5])

    df = pd.DataFrame({

        'Timespot': Time_spot,
        'Open': Open,
        'High': High,
        'Low': Low,
        'Close': Close,
        'Volume': Volume

    })

    df.to_csv("./history_data.csv", index=False)
    # Store history data to this path: "./history_data.csv"

    print("Run time : ", datetime.datetime.now() - start_time)

main()