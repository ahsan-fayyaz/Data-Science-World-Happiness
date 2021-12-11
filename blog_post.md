# World Happiness

### MOTIVATION

Happiness is an emotional state characterized by feelings of joy, satisfaction, contentment, and fulfillment. Majority refer to their happiness to how they feel in the present moment, or a more general sense of how they feel about life overall. 

![happiness](https://user-images.githubusercontent.com/54913677/145660104-53800121-c7de-4312-be05-0a3e310d96b8.png)

Happiness is a broadly defined term without a fixed answer and standard. But the World Happiness Report tells us that there are standards for happiness. 

The World Happiness Report is an international survey report published by the United Nations to measure the sustainable development of happiness. The report ranks 156 countries based on the data from Gallup World Poll survey and results of six major factors such as GDP per capita, family, life expectancy, freedom, generosity, and trust in government corruption. 

The data from Gallup World Poll surveys are based on answers to a simple subjective question to over 1,000 people in each 156 countries to rate their current lives on the scale of 0 to 10 with the best possible life for them being a 10, and the worst possible life being a 0.

By analyzing the correlations between the six factors and happiness score. We will answer the questions:

* Which countries rank the highest and lowest on the overall happiness score?
* Which factors have the greatest impact on people's happiness around the world?

In addition, we will add in new factors such as COVID cases, crude suicide rates, drinking water services and medical doctors as new comparison sets. 


### DATA

Describe your data. Why did you choose it? What are its limitations?

The world happiness dataset was provided by the [World Happiness Report (WHR)](https://worldhappiness.report/). The WHR is a publication of the Sustainable Development Solutions Network, powered by data from the Gallup World Poll and Lloyd’s Register Foundation. The world happiness dataset is acted as our main dataset that we will be comparing to with other factors in correlation to the happiness score. Furthermore, the datasets on COVID cases, crude suicide rates, drinking water services and medical doctors are collected from [Kaggle](https://www.kaggle.com/datasets) and the [World Health Organization (WHO)](https://covid19.who.int/info/). We chose these datasets because we strongly believe that these variables have some sort of correlation with the happiness score. Additionally, we believe that if we have the data of all the above factors we can determine the happiness score of that country without the need to survey individuals living in the country. 

We have multiple datasets from different sources, which makes it harder for us to clean and combine these datasets together. Especially, dealing with the grouping of our main world happiness dataset was provided by the [World Happiness Report (WHR)](https://worldhappiness.report/). The world happiness dataset includes data from various different years with many missing datas. This leads to a lot of inconsistencies in the data, and even if we want, we cannot sort the data by each individual year.

To clean the datasets, we will run [`data_cleaning.py`](data_cleaning.py) script in [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb).

All the raw datasets from [/Datasets/Raw_Datasets](/Datasets/Raw_Datasets) will:

* Drop all unneccessary columns and null values
* Rename columns
* Group all data in the world happiness dataset by 'country' column by taking the mean values of each column for each individual country.

After running [`data_cleaning.py`](data_cleaning.py) for all the raw datasets, we combined 
* [`cleaned_drinking_water_services.csv`](/Datasets/Cleaned_Datasets/cleaned_drinking_water_services.csv), 
* [`cleaned_crude_suicide_rates.csv`](/Datasets/Cleaned_Datasets/cleaned_crude_suicide_rates.csv), and 
* [`cleaned_medical_doctors.csv`](/Datasets/Cleaned_Datasets/cleaned_medical_doctors.csv) 

as features into the [`cleaned_world_happiness.csv`](/Datasets/Cleaned_Datasets/cleaned_world_happiness.csv) as new file called [`full_dataset.csv`](/Datasets/Cleaned_Datasets/full_dataset.csv).

#### Data Dictionary for [`full_dataset.csv`](/Datasets/Cleaned_Datasets/full_dataset.csv):
| Field Name | Description | Data Type | Example |
| ---: | :--- | ---: | :--- |
| country | Name of the country | String | Afghanistan |
| happiness_score | Happiness score in the scale of 0 to 10 for each country | float | 3.594628175 |
| gdp_per_capita | GDP per capita of each country | float | 7.650843461 |
| social_support | Social support | float | 0.508245361 |
| life_expectancy | Healthy life expectancy | float | 52.26666673 |
| freedom | Freedom to make choices in life | float | 0.518011677 |
| corruption | Perception of corruption | float | 0.070040733 |
| clean_water_per_100_people | Clear water per 100 people | float | 37.755 |
| suicide_rate_per_100000_people | Suicide rate per 100,000 people | float |4.3 |
| doctors_per_10000_people: | Doctors per 10,000 people | float | 2.3225 |

#### Data Dictionary for [`cleaned_covid.csv`](/Datasets/Cleaned_Datasets/cleaned_covid.csv):
| Field Name | Description | Data Type | Example |
| ---: | :--- | ---: | :--- |
| Country | Name of the country or region the country belongs to | String | Afghanistan |
| total_confirmed | The total number of COVID19 confirmed cases | integer | 36362 |
| total_deaths | The total number of COVID19 deaths reported | integer  | 1269 | 
| total_recovered | The total number of COVID19 recovered cases | integer  | 25198 | 
| deaths_per_100 | The total number of COVID19 deaths per 100 person | float | 3.5 | 
| recovered_per_100 | The total number of COVID19 recovered cases per 100 person | float | 69.49 | 
| region | Region of the country | String | Eastern Mediterranean | 


### Model

What did you build? Why?

To determine the accuracy of our


### Evaluation

Evaluate your model. Do you feel confident about its performance?

### Future Work

Describe what work you would do in the future. This can include work to improve your model, building related models, and/or sourcing different datasets. Are there any other interesting questions you uncovered while you were working on your model?



**Questions to answer:**
  - The new COVID19 epidemic began in December 2019. Combining the data changes on 19, 20, and 21, check the impact of COVID19 epidemic on the country's happiness. 




