import pandas as pd
import requests

class DataHandler:
    def fetch_data(self):
        response = requests.get("https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json")
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv('instruments.csv', index=False)
        
    def get_info_by_symbol(self, symbol):
        df = pd.read_csv('instruments.csv')
        filtered_df = df[df['symbol'] == symbol]
        if not filtered_df.empty:
            return filtered_df.iloc[0]
        return None
