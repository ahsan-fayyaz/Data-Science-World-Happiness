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
  - `data_dictionary.csv`: The data dictionary for cleaned.  
 
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

**Cleaning:**
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

[cleaned_world_happiness.csv](/Datasets/Cleaned_Datasets/cleaned_world_happiness.csv)
```python
cleaned_world_happiness_df = pd.read_csv("./Datasets/Cleaned_Datasets/cleaned_world_happiness.csv", header=0)
cleaned_world_happiness_df.head()
```
![world_happiness_table](https://user-images.githubusercontent.com/54913677/143495535-88cfaa24-c092-40b5-a416-385949059311.png)

```python
sns.heatmap(cleaned_world_happiness_df.corr(), annot=True)
```
![world_happiness_heatmap](https://user-images.githubusercontent.com/54913677/143495463-0101e86a-89fc-445d-978f-603419e61a06.png)

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

### Contributions
Describe the contributions that each group member made.
- Ahsan Fayyaz 
  - Wrote data_cleaning.py script to clean data
  -    
- Rezwana Kabita
- Shanshan Li
  - Collect all raw datasets
