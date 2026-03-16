import os
import shutil
import requests
import pandas as pd

def download_and_print_unemployment_df():
    url = "https://www.ons.gov.uk/generator?format=xls&uri=/employmentandlabourmarket/peoplenotinwork/unemployment/timeseries/mgsx/lms"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        with open('downloaded_file.xls', 'wb') as f:
            f.write(response.content)
        
        df = pd.read_excel('downloaded_file.xls')
        print(df)
        return df
    else:
        print("Failed to download the file")
        return None

if __name__ == "__main__":
    download_and_print_unemployment_df()


"""

python ons.py


"""