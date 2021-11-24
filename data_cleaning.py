import pandas as pd
import os

#--------------GLOBAL VARIABLES------------#


#Store the datasets into a dictionary
raw_datasets = {}

###--------------IMPORT ALL THE DATASETS------------###
raw_world_happiness_df = pd.read_excel("./Datasets/Raw_Datasets/raw_world_happiness.xls", header=0)
raw_datasets["World Happiness Dataset"] = raw_world_happiness_df

raw_covid_df = pd.read_csv('./Datasets/Raw_Datasets/raw_covid.csv',header=0)
raw_datasets["Covid Dataset"] = raw_covid_df

raw_drinking_water_services_df = pd.read_csv('./Datasets/Raw_Datasets/raw_drinking_water_services.csv',header=0)
raw_datasets["Drinking Water Services Dataset"] = raw_drinking_water_services_df

raw_crude_suicide_rates_df = pd.read_csv('./Datasets/Raw_Datasets/raw_crude_suicide_rates.csv',header=0)
raw_datasets["Crude Suicide Rates Dataset"] = raw_crude_suicide_rates_df

raw_medical_doctors_df = pd.read_csv('./Datasets/Raw_Datasets/raw_medical_doctors.csv',header=0)
raw_datasets["Medical Doctors Dataset"] = raw_medical_doctors_df


###--------------HELPER FUNCTIONS------------###

#-------clear the Clean_datasets_directory-------#
def clear_cleaned_dataset_dir():
    dir = './Datasets/Cleaned_Datasets/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        
        
#-------Drop duplicates-------#
def drop_duplicates_from_all_datasets(datasets):
    for name, df in datasets.items():
        df = df.drop_duplicates(inplace=True)
        print("Duplicates removed from {} dataset", name)




###--------------DATA CLEANING FUNCTIONS FOR EACH DATASET------------###

#-------World Happiness Data-------#
def clean_world_happiness_data(df):
    #drop unwanted columns
    df = df.drop(['Positive affect', 'Negative affect', 'year'], axis=1)
    
    #rename the columns
    df = df.rename(columns={'Country name': 'country',
                        'Life Ladder': 'life_ladder',
                        'Log GDP per capita': 'gdp_per_capita',
                        'Social support': 'social_support',
                        'Healthy life expectancy at birth': 'life_expectancy',
                        'oldName1': 'newName1',
                        'Freedom to make life choices': 'freedom_to_make_life_choices',
                        'Generosity':'generosity',
                        'Perceptions of corruption': 'perceptions_of_corruption'},
                        )
    #group by country name
    df = df.groupby(['country'], as_index=False).mean()
    #drop null rows
    df = df.dropna()
    df = clean_world_happiness_data(raw_world_happiness_df)
    # df.to_csv('./Datasets/Cleaned_Datasets/cleaned_world_happiness.csv')

#World Happiness Data







###-----------MAIN-----------###
def main():
    clear_cleaned_dataset_dir()
    drop_duplicates_from_all_datasets(raw_datasets)
    clean_world_happiness_data(raw_world_happiness_df)
    

if __name__ == "__main__":
    main()
