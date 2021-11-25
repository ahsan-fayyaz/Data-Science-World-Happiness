# Project Title

### Group Members
- Ahsan Fayyaz 
- Rezwana Kabita
- Shanshan Li

### Repository Structure
List each file and what it's purpose it. Make sure you indicate where your data cleaning code and data dictionary are! 

- `raw data` *Data stored in [/Datasets/Raw_Datasets](/Datasets/Raw_Datasets)
  - `raw_world_happiness.xls`: Raw data from the [World Happiness Report](https://worldhappiness.report/)
  - `raw_covid.csv`: Raw data from the [World Health Organization (WHO)](https://covid19.who.int/info/)
  - `raw_drinking_water_services.csv`: Raw data from the [Kaggle](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)
  - `raw_crude_suicide_rates.csv`: Raw data from [Kaggle](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)
  - `raw_medical_doctors.csv`: Raw data from [Kaggle](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)

- `cleaned data` *Data stored in [./Datasets/Cleaned_Datasets](/Datasets/Cleaned_Datasets) directory after running data_cleaning.py script)*
  - `cleaned_world_happiness.csv`: The cleaned dataset for `raw_world_happiness.xlx` 
  - `cleaned_covid.csv`: The cleaned dataset for `raw_covid.csv`
  - `cleaned_drinking_water_services.csv`: The cleaned dataset for `raw_drinking_water_services.csv`
  - `cleaned_crude_suicide_rates.csv`: The cleaned dataset for `raw_crude_suicide_rates.csv`
  - `cleaned_medical_doctors.csv`: The cleaned dataset for `raw_medical_doctors.csv`
  - `data_dictionary.csv`: The data dictionary for all the cleaned data(csv files).
 
- `code`
  - [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb): 
    - Includes descriptive stats of raw datasets. 
    - It calls our data_cleaning.py script. 
    - Includes descriptive stats of cleaned datasets
    - Visualizes our cleaned datasets to give an overview of cleaned data
 
  - [`data_cleaning.py`](data_cleaning.py): Cleans the following datasets:
    - `raw_world_happiness.xls` 
    - `raw_covid.csv`        
    - `raw_drinking_water_services.csv` 
    - `raw_crude_suicide_rates.csv` 
    - `raw_medical_doctors.csv` 
    - `data_dictionary.csv`

### Exploratory Analysis

To begin cleaning the raw dataset we obtained, we read all the raw datasets in [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb) to check for errors and special cases, and prepare data for analysis. To do so, we went over each dataset and summarize it, analysising the information and count of null values for each column.

Example:
```python
display(world_happiness_df.describe())
display(world_happiness_df.info())
display(world_happiness_df.isnull().sum(axis = 0))
```

To clean the datasets. We will run [`data_cleaning.py`](data_cleaning.py) script in [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb).
```python
%run data_cleaning.py
```

[`data_cleaning.py`](data_cleaning.py) will take and cleans all the raw datasets from [/Datasets/Raw_Datasets](/Datasets/Raw_Datasets), and stores the cleaned datasets into [./Datasets/Cleaned_Datasets](/Datasets/Cleaned_Datasets) as new files. 

#### Analysis: World Happiness Dataset

Cleaning:
  * All unneccessary columns are dropped.
  * Renamed the remaining columns
  * Group the data by 'country' column
  * Take the mean values of each column for each individual country.
  * All remaining null values are dropped

```python
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
```

After running [`data_cleaning.py`](data_cleaning.py) for the raw dataset `raw_world_happiness.xlx`. We have [cleaned_world_happiness.csv](/Datasets/Cleaned_Datasets/cleaned_world_happiness.csv). 

Let's look at some visualization for the analysis of `cleaned_world_happiness.csv` 

```python
cleaned_world_happiness_df = pd.read_csv("./Datasets/Cleaned_Datasets/cleaned_world_happiness.csv", header=0)
cleaned_world_happiness_df.head()
```
![world_happiness_table](https://user-images.githubusercontent.com/54913677/143495535-88cfaa24-c092-40b5-a416-385949059311.png)

```python
sns.heatmap(cleaned_world_happiness_df.corr(), annot=True)
```
![world_happiness_heatmap](https://user-images.githubusercontent.com/54913677/143495463-0101e86a-89fc-445d-978f-603419e61a06.png)
> The correlation map above visualizes the correlation values between happiness scores and various evaluation factors that contribute to happiness score. It demonstrates a direct positive correlation between the Happiness Score of a country and economy, family, and health/ life expectancy.
> 
#### Analysis: Covid Dataset

Cleaning:
  * Dropping, renaming, removing nulls.

```python
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
```

[cleaned_covid.csv](/Datasets/Cleaned_Datasets/cleaned_covid.csv)

```python
cleaned_covid_df = pd.read_csv("./Datasets/Cleaned_Datasets/cleaned_covid.csv", header=0)
cleaned_covid_df.head()
```
![covid_table](https://user-images.githubusercontent.com/54913677/143498106-812f4877-c5d7-444c-80b1-149b9372df9e.png)

```python
sort_by_region = cleaned_covid_df.groupby(['region'], as_index=False).sum()
sort_by_region.head()
```
![covid_death_table](https://user-images.githubusercontent.com/54913677/143498268-767b7f9c-7b39-4e12-903f-dbde76f28417.png)
> Taking a look at the total number of confirmed COVID19 cases (total_confirmed), total number of deaths due to COVID19 (total_deaths), and total number of people recovered from COVID19 (total_recovered) in each region.
> 
```python
  # Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(sort_by_region['total_deaths'],
        labels=sort_by_region['region'],
       autopct='%1.1f%%',
       shadow=True, startangle=40)
plt.axis('equal')
# show plot
plt.show()
```
![covid_pie_diagram](https://user-images.githubusercontent.com/54913677/143498414-e74f4a32-f857-49ad-9377-35181f809e3a.png)
> The pie graph above demonstrates the distribution of deaths due to COVID19 cases in each region.
> 
#### Analysis: Clean Drinking Water Dataset

Cleaning:
  * Dropping, renaming, grouping data by country and averaging all the rows with same country. 

```python
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
```

[cleaned_drinking_water_services.csv](/Datasets/Cleaned_Datasets/cleaned_drinking_water_services.csv)

```python
cleaned_clean_drinking_water_df = pd.read_csv("./Datasets/Cleaned_Datasets/cleaned_drinking_water_services.csv", header=0)
cleaned_clean_drinking_water_df.head()
```
![clean_drinking_water_table](https://user-images.githubusercontent.com/54913677/143498620-40f39165-7998-4906-a8cc-34774e72cede.png)

#### Analysis: Crude Suicide Rates Dataset

Cleaning:
  * Dropping, renaming, grouping data by country and averaging all the rows with same country. 

```python
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
```

[cleaned_crude_suicide_rates.csv](/Datasets/Cleaned_Datasets/cleaned_crude_suicide_rates.csv)

```python
cleaned_crude_suicide_rates_df = pd.read_csv("./Datasets/Cleaned_Datasets/cleaned_crude_suicide_rates.csv", header=0)
cleaned_crude_suicide_rates_df.head()
```
![crude_suicide_rate_table](https://user-images.githubusercontent.com/54913677/143498891-9837b004-047d-4e82-9d0f-668976fbd574.png)

#### Analysis: Medical Doctors Dataset

Cleaning:
  * Dropping, renaming, grouping data by country and averaging all the rows with same country. 

```python
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
```

[cleaned_medical_doctors.csv](/Datasets/Cleaned_Datasets/cleaned_medical_doctors.csv)

```python
cleaned_medical_doctors_df = pd.read_csv("./Datasets/Cleaned_Datasets/cleaned_medical_doctors.csv", header=0)
cleaned_medical_doctors_df.head()
```
![medical_doctor_table](https://user-images.githubusercontent.com/54913677/143498907-69c87ee3-fbbf-4de1-8fbd-f7b970435bea.png)


### Challenges
We have multiple datasets from different sources, which made it harder for us to clean and combine these datasets together. Especially, dealing with the grouping of `raw_world_happiness.xls`. 
- **Challenges in grouping `raw_world_happiness.xls` includes:**
  - Each country contains datas from different years.
  - Many countries have missing datas for various years.

This leads to a lot of inconsistencies in the data, and even if we want, we cannot sort the data by year. 
</br>
To clean `raw_world_happiness.xls` effectively, we solved the problem by grouping data by 'country' and averaging it. We also dropped the 'years' column.

### Future Work
Now that we have cleaned data to work with, we will use this data to build models that predict which variables are most important to determine happiness index around the world. We will use Linear Regression, Logistic Regression, K-means Clustering and various other ML algorithms to predict world happiness around the world.

**Questions to answer:**
  - Which are the happiest countries? How does the happiness level differe around the world? (Create an interactive global map, displaying ever country's happiness rank.)
  - The new COVID19 epidemic began in December 2019. Combining the data changes on 19, 20, and 21, check the impact of COVID19 epidemic on the country's happiness. 
  - Correlation between each individual evaluation factors. (e.g. What are the factors effects the GDP per capita? )
  - What is the difference between the happiest country in the world and the rest of the world?
    - Which evaluation factor has the strongest correlations to the happiest country?

### Contributions
Describe the contributions that each group member made.
- Ahsan Fayyaz 
  - Wrote data_cleaning.py script to clean data   
- Rezwana Kabita
  - Helped Clean the datasets and wrote scripts to visualize and understand the data better.  
- Shanshan Li
  - Collected all raw datasets.
