import os
import pandas as pd
import random

def fake_data():
    fake = {
        "X": [random.randint(118,2000) for i in range(2000)],
        "Y": [round(random.uniform(0,15000),2) for i in range(2000)],
    }

    return fake


    # df = pd.DataFrame(fake_data)
    # df.to_csv()
# print(df)

if __name__ == '__main__':

    for r,d,f in os.walk('./temp'):
        
        if r != './temp':
            for dir in d:
                for i in range(4):
                    df = pd.DataFrame(fake_data())
                    df.to_csv(f"{os.path.join(r,dir)}/{dir[-5:]}-{i+1}.csv")
