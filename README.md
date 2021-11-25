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

- `cleaned data` (Data stored in ./Datasets/Cleaned_Datasets directory after running data_cleaning.py script)
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
We have 5 datasets which are stored in Raw_Datasets directory under /Datasets. 

### Challenges
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

### Future Work
Describe what work you are planning to complete for the final analysis.

### Contributions
Describe the contributions that each group member made.

