# Project Title

### Group Members
- Ahsan Fayyaz 
- Rezwana Kabita
- Shanshan Li

### Repository Structure
List each file and what it's purpose it. Make sure you indicate where your data cleaning code and data dictionary are! 

- `raw data`
  - `raw_world_happiness.xls`: Raw data from the [World Happiness Report](https://worldhappiness.report/)
  - `raw_covid.csv`: Raw data from the [World Health Organization (WHO)](https://covid19.who.int/info/)
  - `raw_drinking_water_services.csv`: Raw data from the [Kaggle](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)
  - `raw_crude_suicide_rates.csv`: Raw data from [Kaggle](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)
  - `raw_medical_doctors.csv`: Raw data from [Kaggle](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)

- `cleaned data` *Data stored in ./Datasets/Cleaned_Datasets directory after running data_cleaning.py script)*
  - `cleaned_world_happiness.csv`
  - `cleaned_covid.csv`
  - `cleaned_drinking_water_services.csv`
  - `cleaned_crude_suicide_rates.csv`
  - `cleaned_medical_doctors.csv`
  - `data_dictionary.csv`: The data dictionary for cleaned.  
 
- `code`
  - `exploratory_data_analysis.ipynb`: 
    - Includes descriptive stats of raw datasets. 
    - It calls our data_cleaning.py script. 
    - Includes descriptive stats of cleaned datasets
    - Visualizes our cleaned datasets to give an overview of cleaned data
 
  - `data_cleaning.py`: Cleans the following datasets:
    - `raw_world_happiness.xls` 
    - `raw_covid.csv`        
    - `raw_drinking_water_services.csv` 
    - `raw_crude_suicide_rates.csv` 
    - `raw_medical_doctors.csv` 
    - `data_dictionary.csv`

### Exploratory Analysis
Let's start with our Jupyter notebook `exploratory_data_analysis.ipynb`. We have 5 datasets which are stored in `/Datasets/Raw_Datasets` directory. In our notebook, we read all these raw datasets to get some initial stats and condition of our data. We go over each dataset and summarize it, as well as look at what needs cleaning. Then in our notebook, we run our `data_cleaning_py` script. This Python script includes all the data cleaning code. It removes all the duplicate rows from each dataset. It contains a data cleaning function for reach dataset. For `raw_world_happiness.xls` we drop unnecessary columns, rename the remaining columns, and group the data by 'country' column, then take an average of values since we had multiple rows for each country. Then it drops the remaining null values. Next, this script cleans `raw_covid.csv` dropping, renaming, removing nulls. Similarly, `raw_drinking_water_services.csv`, `raw_crude_suicide_rates.csv`, and `raw_medical_doctors.csv` are cleaned by dropping, renaming, grouping data by country and averaging all the rows with same country. In the end, the cleaned dataframes are stored into their respective csv files under `/Datasets/Cleaned_Datasets` directory. Next, we  use Pandas to read the cleaned data within our `exploratory_data_analysis.ipynb` notebook.

### Challenges
The main challenge so far was with how to group the `raw_world_happiness.xls`. Each country had multiple rows with different years. However, not every country had the same years of data. This lead to a lot of inconsistency and even if we wanted, we could not sort the data by year. It was a bit challenging to come up with an effective way to clean this data and we ended up solving the problem by grouping data by 'country' and averaging it. We also dropped the 'years' column.

### Future Work
Now that we have cleaned data to work with, we will use this data to build models that predict which variables are most important to determine happiness index around the world. We will use Linear Regression, Logistic Regression, K-means Clustering and various other ML algorithms to predict world happiness around the world.

### Contributions
Describe the contributions that each group member made.
- Ahsan Fayyaz 
  - Wrote data_cleaning.py script to clean data
  -    
- Rezwana Kabita
- Shanshan Li
