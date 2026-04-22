import pandas as pd

data = {
    "distance": [10.8, 9.7, 12.4, 7.2, 14.1, 8.4, 11.6, 6.9, 9.3, 13.2],
    "duration": [21, 24, 20, 15, 30, 18, 23, 14, 19, 28],
    "adjusted_time": [25, 28, 23, 17, 36, 20, 27, 16, 22, 33]
}

df = pd.DataFrame(data)

df.to_csv("data/route_data.csv", index=False)

print("Dataset created successfully")