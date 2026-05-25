import os
import requests
import pandas as pd
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)


def output_unemployment():
    url = "https://www.ons.gov.uk/generator?format=xls&uri=/employmentandlabourmarket/peoplenotinwork/unemployment/timeseries/mgsx/lms"
    response = requests.get(url)
    if response.status_code == 200:
        with open('downloaded_file.xls', 'wb') as f:
            f.write(response.content)
        df = pd.read_excel('downloaded_file.xls', skiprows=8)
        df.columns = ['date', 'value']
        output_path = os.path.join(OUTPUTS_DIR, "unemployment.csv")
        df.to_csv(output_path, index=False)
        print(f"Saved unemployment table to: {output_path}")
        print(df.head(5))
        return df
    return None


def output_gdp_growth():
    url = "https://www.ons.gov.uk/generator?format=xls&uri=/economy/grossdomesticproductgdp/timeseries/ihyq/pn2"
    response = requests.get(url)
    if response.status_code == 200:
        with open('downloaded_file.xls', 'wb') as f:
            f.write(response.content)
        df = pd.read_excel('downloaded_file.xls', skiprows=8)
        df.columns = ['date', 'value']
        output_path = os.path.join(OUTPUTS_DIR, "gdp_growth.csv")
        df.to_csv(output_path, index=False)
        print(f"Saved gdp_growth table to: {output_path}")
        print(df)
        return df
    return None


def output_all():
    output_unemployment()
    output_gdp_growth()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "unemployment":
            output_unemployment()
        elif arg == "gdp":
            output_gdp_growth()
        elif arg == "both":
            output_all()
        else:
            print(f"Usage: python ons.py [unemployment|gdp|both]")
    else:
        output_all()



"""

python ons.py unemployment

python ons.py gdp

python ons.py both


"""