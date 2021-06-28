import json
import pandas as pd

df = pd.read_csv('csv/db_hydrocarbons.csv')
df = df.set_index('fecha')

new_df = df[['pemexMagna','marinaSuroeste','propileno']]
result = new_df.corr().to_json(orient="split")
parsed = json.loads(result)
print(parsed)