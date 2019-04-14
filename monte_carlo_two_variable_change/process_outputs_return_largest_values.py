import pandas as pd 
def read_csv_to_panda(csv):
    df = pd.read_csv('csv')
    hundred_day =df['Region'].unique().tolist()