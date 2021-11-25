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
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

### Future Work
Describe what work you are planning to complete for the final analysis.

### Contributions
Describe the contributions that each group member made.

