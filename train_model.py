import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv("data/route_data.csv",encoding="latin1")

X = data[["distance","duration"]]

y = data["adjusted_time"]

model = RandomForestRegressor()

model.fit(X,y)

pickle.dump(model, open("models/model.pkl","wb"))

print("Model trained successfully")