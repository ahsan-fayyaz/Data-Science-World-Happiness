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
    
    print("Removing Duplicates rows from each dataset....\n")




###--------------DATA CLEANING FUNCTIONS FOR EACH DATASET------------###

#-------World Happiness Data-------#
def clean_world_happiness_data(df):
    #drop columns not needed
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
    #groupby country name
    df = df.groupby(['country'], as_index=False).mean()
    #drop null rows
    df = df.dropna()
    
    #Export this dataframe as csv into Clean_Dataset directory after cleaning
    df.to_csv('./Datasets/Cleaned_Datasets/cleaned_world_happiness.csv', index = False)
    print("Cleaned `World Happiness Data` and exported as a new csv file....")


#-------Covid Data-------#
def clean_covid_data(df):
    #drop unwanted columns
    df = df.drop(['1 week % increase', '1 week change', 'Confirmed last week', 'New recovered', 
                          'Deaths / 100 Recovered', 'New recovered', 'New deaths', 'New cases', 'Active'
                         ], axis=1)
    df = df.rename(columns={'Country/Region': 'country',
                        'Confirmed': 'total_confirmed',
                        'Deaths': 'total_deaths',
                        'Recovered': 'total_recovered',
                        'Deaths / 100 Cases': 'deaths_per_100',
                        'Recovered / 100 Cases': 'recovered_per_100',
                        'WHO Region': 'region'},
                        )
    #drop null rows
    df = df.dropna()
    
    #Export this dataframe as csv into Clean_Dataset directory after cleaning
    df.to_csv('./Datasets/Cleaned_Datasets/cleaned_covid.csv', index = False)
    print("Cleaned `Covid Data` and exported as a new csv file....")



#-------Clean Drinking Water Data-------#
def clean_drinking_water_data(df):
    
    #drop columns
    df = df.drop(['Indicator', 'Period'], axis=1)
    #rename the columns
    df = df.rename(columns={'Location': 'country',
                        'First Tooltip': 'clean_water_per_100_people'})
    
    #drop null rows
    df = df.dropna()
    df = df.groupby(['country'], as_index=False).mean()
    
    #Export this dataframe as csv into Clean_Dataset directory after cleaning
    df.to_csv('./Datasets/Cleaned_Datasets/cleaned_drinking_water_services.csv', index = False)
    print("Cleaned `Clean Drinking Water Data` and exported as a new csv file....")
                        

#-------Crude Suicide Rates Data-------#
def clean_crude_suicide_rates_data(df):
    df = df.drop([ 'Indicator', 'Dim1', 'Period'], axis=1)
    #rename the columns
    df = df.rename(columns={'Location': 'country',
                            'First Tooltip': 'suicide_rate_per_100000_people'})
    df = df.groupby(['country'], as_index=False).mean()
    df = df.dropna()
    
    #Export this dataframe as csv into Clean_Dataset directory after cleaning
    df.to_csv('./Datasets/Cleaned_Datasets/cleaned_crude_suicide_rates.csv', index = False)
    print("Cleaned `Crude Suicide Rates Data` and exported as a new csv file....")


#-------Medical Doctors Data-------#
def clean_medical_doctors_data(df):
    df = df.drop([ 'Indicator', 'Period'], axis=1)
    #rename the columns
    df = df.rename(columns={'Location': 'country',
                            'First Tooltip': 'doctors_per_10000_people'})
    df = df.groupby(['country'], as_index=False).mean()
    df = df.dropna()
    
    #Export this dataframe as csv into Clean_Dataset directory after cleaning
    df.to_csv('./Datasets/Cleaned_Datasets/cleaned_medical_doctors.csv', index = False)
    print("Cleaned `Medical Doctors Data` and exported as a new csv file....")


###-----------MAIN-----------###
def main():
    
    print("Running the Python Script to clean data.....\n")
    #Call the function to clear any existing files in Cleaned_Dataset directory
    clear_cleaned_dataset_dir()
    #Call the function to remove duplicates from each dataset
    drop_duplicates_from_all_datasets(raw_datasets)
    
    #call data cleaniing functiton for each dataset
    clean_world_happiness_data(raw_world_happiness_df)
    clean_covid_data(raw_covid_df)
    clean_drinking_water_data(raw_drinking_water_services_df)
    clean_crude_suicide_rates_data(raw_crude_suicide_rates_df)
    clean_medical_doctors_data(raw_medical_doctors_df)
    print("\n\nSUCCESS\n\nData Cleaning Done.\nCheck `Datasets/Cleaned_Datasets` directory to view new csv files with cleaned data")



if __name__ == "__main__":
    main()
