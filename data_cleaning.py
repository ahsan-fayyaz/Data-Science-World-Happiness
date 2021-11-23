import pandas as pd
import os

#Store the datasets into a dictionary
raw_datasets = {}


def load_dataframes():
    #--------------IMPORT ALL THE DATASETS------------#
    world_happiness_df = pd.read_excel("./Datasets/Raw_Datasets/world_happiness/DataPanelWHR2021C2_1.xls", header=0)
    raw_datasets["World Happiness Dataset"] = world_happiness_df

    covid_df = pd.read_csv('./Datasets/Raw_Datasets/covid/country_wise_latest.csv',header=0)
    raw_datasets["Covid Dataset"] = covid_df

    drinking_water_services_df = pd.read_csv('./Datasets/Raw_Datasets/other_metrics/basicDrinkingWaterServices.csv',header=0)
    raw_datasets["Drinking Water Services Dataset"] = drinking_water_services_df

    crude_suicide_rates_df = pd.read_csv('./Datasets/Raw_Datasets/other_metrics/crudeSuicideRates.csv',header=0)
    raw_datasets["Crude Suicide Rates Dataset"] = crude_suicide_rates_df

    life_expectancy_df = pd.read_csv('./Datasets/Raw_Datasets/other_metrics/lifeExpectancyAtBirth.csv',header=0)
    raw_datasets["Life Expectancy Dataset"] = life_expectancy_df



# Drop duplicates
def drop_duplicates_from_all_datasets(datasets):
    for name, df in datasets.items():
        df = df.drop_duplicates(inplace=True)
        print("Duplicates dropped from ", name)

# world_happiness_df = world_happiness_df.dropna()
# world_happiness_df.isnull().sum(axis = 0)

















def main():
    load_dataframes()
    drop_duplicates_from_all_datasets(raw_datasets)

if __name__ == "__main__":
    main()
