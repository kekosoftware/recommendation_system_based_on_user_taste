import pandas as pd

df = pd.read_excel('Spotify_data.xlsx')

df.to_csv('Spotify_data_convert.csv', index=False)