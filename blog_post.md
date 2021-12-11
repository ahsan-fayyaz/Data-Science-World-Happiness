# World Happiness

### MOTIVATION

Happiness is an emotional state characterized by feelings of joy, satisfaction, contentment, and fulfillment. Majority refer their happiness to how they feel in the present moment, or a more general sense of how they feel about life overall. Happiness is a boardly defined term without a fixed answer and standard. But the World Happiness Report tell us that there are standards for happiness. 

The World Happiness Report is an international survey report published by the United Nations to measure the sustainable development of happiness. The report ranks 156 countries based on the data from Gallup World Poll survey and results of six major factors such as GDP per capita, family, life expectancy, freedom, generosity, and trust in government corruption. 

The data from Gallup World Poll surveys are based on answers to a simple subjective question to over 1,000 people in each 156 countries to rate their current lives on the scale of 0 to 10 with the best possible life for them being a 10, and the worst possible life being a 0.

By analyzing the correlations between the six factors and happiness score. We will answer the questions:

* Which countries rank the highest and lowest on the overall happiness score?
* Which factors have the greatest impact on people's happiness around the world?

In addition, we will add in new factors such as COVID cases, crude suicide rates, drinking water services and medical doctors as new comparison sets. 


### DATA

Describe your data. Why did you choose it? What are its limitations?

We have multiple datasets from different sources, which made it harder for us to clean and combine these datasets together. Especially, dealing with the grouping of our main world happiness dataset was provided by the [World Happiness Report (WHR)](https://worldhappiness.report/). The WHR is a publication of the Sustainable Development Solutions Network, powered by data from the Gallup World Poll and Lloyd’s Register Foundation. The world happiness dataset includes data from various different years with many missing datas. This leads to a lot of inconsistencies in the data, and even if we want, we cannot sort the data by each individual year. 

Furthermore, the datasets on COVID cases, crude suicide rates, drinking water services and medical doctors are collected from [Kaggle](https://www.kaggle.com/datasets) and the [World Health Organization (WHO)](https://covid19.who.int/info/). We chose these datasets because we strongly believe that these variables have some sort of relationship with the happiness index. 

#### Data Dictionary for `full_dataset.csv`:
* Country: Name of the country or region the country belongs to, String;
* happiness_score: Happiness Score in the scale of 0 - 10 for each country, float;
* gdp_per_capita: GDP per capita of each country, float;
* social_support: Social support of, float;
* life_expectancy: Healthy life expectancy, float;
* freedom:  Freedom to make choices in life, float;
* corruption: Perception of corruption, float;
* clean_water_per_100_people: Clear water per 100 people, float;
* suicide_rate_per_100000_people: Suicide rate per 100,000 people, float;
* doctors_per_10000_people: Doctors per 10,000 people, float;

#### Data Dictionary for `cleaned_covid.csv`:
* Country: Name of the country or region the country belongs to，String;
* total_confirmed: The total number of COVID19 confirmed cases, integer;
* total_deaths: The total number of COVID19 deaths reported, integer;
* total_recovered: The total number of COVID19 recovered cases, integer;
* deaths_per_100: The total number of COVID19 deaths per 100 person, float;
* recovered_per_100: The total number of COVID19 recovered cases per 100 person, float;
* region: Region of the country, String;


### Model

What did you build? Why?


### Evaluation

Evaluate your model. Do you feel confident about its performance?

### Future Work

Describe what work you would do in the future. This can include work to improve your model, building related models, and/or sourcing different datasets. Are there any other interesting questions you uncovered while you were working on your model?

**Questions to answer:**
  - The new COVID19 epidemic began in December 2019. Combining the data changes on 19, 20, and 21, check the impact of COVID19 epidemic on the country's happiness. 
  - Correlation between each individual evaluation factors. (e.g. What are the factors effects the GDP per capita? )
  - What is the difference between the happiest country in the world and the rest of the world?
    - Which evaluation factor has the strongest correlations to the happiest country?

