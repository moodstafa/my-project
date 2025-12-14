import pandas as pd



data = {
    "Name": ["Ali", "Sara", "John"],
    "Age": [25, 30, 28],
    "City": ["Lahore", "Karachi", "New York"]
}



df = pd.DataFrame(data)

print(df)