import pandas as pd
import os


path = os.getcwd()
print(path)
df = pd.read_excel("./Datasets/Raw_Datasets/world_happiness/DataPanelWHR2021C2_1.xls")

print(df.head(5))