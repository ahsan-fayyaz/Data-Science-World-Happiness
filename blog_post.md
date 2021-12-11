# World Happiness

Happiness is an emotional state characterized by feelings of joy, satisfaction, contentment, and fulfillment. Majority refer to their happiness to how they feel in the present moment, or a more general sense of how they feel about life overall. 

![happiness](https://user-images.githubusercontent.com/54913677/145660104-53800121-c7de-4312-be05-0a3e310d96b8.png)

Happiness is a broadly defined term without a fixed answer and standard. But the World Happiness Report tells us that there are standards for happiness. 

The World Happiness Report is an international survey report published by the United Nations to measure the sustainable development of happiness. The report ranks 156 countries based on the data from Gallup World Poll survey and results of six major factors such as GDP per capita, family, life expectancy, freedom, generosity, and trust in government corruption. 

The data from Gallup World Poll surveys are based on answers to a simple subjective question to over 1,000 people in each 156 countries to rate their current lives on the scale of 0 to 10 with the best possible life for them being a 10, and the worst possible life being a 0.

By analyzing the correlations between the six factors and happiness score. We will answer the questions:

* Which countries rank the highest and lowest on the overall happiness score?
* Which factors have the greatest impact on people's happiness around the world?

In addition, we will add in new factors such as COVID cases, crude suicide rates, drinking water services and medical doctors as new comparison sets. 


### Data

The world happiness dataset was provided by the [World Happiness Report (WHR)](https://worldhappiness.report/). The WHR is a publication of the Sustainable Development Solutions Network, powered by data from the Gallup World Poll and Lloyd’s Register Foundation. The world happiness dataset is acted as our main dataset that we will be comparing to with other factors in correlation to the happiness score. Furthermore, the datasets on COVID cases, crude suicide rates, drinking water services and medical doctors are collected from [Kaggle](https://www.kaggle.com/datasets) and the [World Health Organization (WHO)](https://covid19.who.int/info/). We chose these datasets because we strongly believe that these variables have some sort of correlation with the happiness score. Additionally, we believe that if we have the data of all the above factors we can determine the happiness score of that country without the need to survey individuals living in the country. 

We have multiple datasets from different sources, which makes it harder for us to clean and combine these datasets together. Especially, dealing with the grouping of our main world happiness dataset was provided by the [World Happiness Report (WHR)](https://worldhappiness.report/). The world happiness dataset includes data from various different years with many missing datas. This leads to a lot of inconsistencies in the data, and even if we want, we cannot sort the data by each individual year.

To clean the datasets, we will run [data_cleaning.py](data_cleaning.py) script in [exploratory_data_analysis.ipynb](exploratory_data_analysis.ipynb).

All the raw datasets from [/Datasets/Raw_Datasets](/Datasets/Raw_Datasets) will:

* Drop all unnecessary columns and null values
* Rename columns
* Group all data in the world happiness dataset by 'country' column by taking the mean values of each column for each individual country.

After running `data_cleaning.py` for all the raw datasets, we combined `cleaned_drinking_water_services.csv`, `cleaned_crude_suicide_rates.csv`, and `cleaned_medical_doctors.csv` as features into the `cleaned_world_happiness.csv` as new file called [`full_dataset.csv`](/Datasets/Cleaned_Datasets/full_dataset.csv).

<sup>Note: all cleaned dataset can be found in [./Datasets/Cleaned_Datasets](/Datasets/Cleaned_Datasets)</sup>

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

Most of the datas we are dealing with in `full_dataset.csv` are continuous values. Therefore, regression analysis is the best fit to use for predicting continuous dependent variables. To determine the regression model that fits our data the most, here is the list of all the different types of Machine Learning Regression models that we build:

* Linear Regression
* ElasticNet Regression
* Ridge Regression
* Lasso Regression
* Bayesian Ridge Regression

We will build each of these models to determine the best fitted model by checking its score for accuracy.


### Evaluation

#### Linear Regression

We found that the `Linear Regression model` performed the best with the score of 86.1% accuracy. That makes sense because linear regression is a long-established statistical procedure, the properties of linear-regression models are well understood and can be trained very quickly. With our hopes to increase our model's accuracy, we performed a k-fold (10 folds) `Cross Validation`. **Cross validation** here split the dataset into 10 folds/groups. This essentially took the first fold as a test set and fit the model on the remaining 9 folds. Then it predicted on the test set. This repeats for a total of 10 times. However, the score went down. So cross-validation did not help improve our model's accuracy at all.

#### ElasticNet Regression

ENet is an extension of linear regression that adds regularization penalties to the loss function during training. Elastic Net gives us two main benefits:

* The order of importance of each variable
* Given a criterion (AIC, BIC, cross-validation R2 ), it can be used to automatically choose the best model very quickly (only comparing p models, where p is the number of variables, as opposed to 2p models).

Again, `ElasticNet Regression` performed as good as Linear Regression Model with 86.1% accuracy.

#### Ridge Regression

Since we knew that Ridge Regression is a better predictor than least squares regression when the predictor variables are more than the observations. Ridge regression works with the advantage of not requiring unbiased estimators – rather, it adds bias to estimators to reduce the standard error. With Ridge regression our score dropped to 65.9% and we found it not be particularly useful for our data.

#### Lasso Regression

The goal of lasso regression is to obtain the subset of predictors that minimizes prediction error for a quantitative response variable. The lasso does this by imposing a constraint on the model parameters that causes regression coefficients for some variables to shrink toward zero. Lasso regression model performed with the score of 61.9% accuracy. In our case, similar to ridge regression it did not perform so well as `Linear Regression` and `ENet`.

#### Bayesian Ridge Regression

Bayesian regression allows a natural mechanism to survive insufficient data or poorly distributed data by formulating linear regression using probability distributors rather than point estimates. The output or response 'y' is assumed to be drawn from a probability distribution rather than estimated as a single value. This model performed very well in our situation, almost as good as Linear Regression and ENet.

Since `Linear Regression` gave us the highest accuracy, let's compare the relationship of all the factors with the happiness score.

#### GDP per capita vs Happiness Score

![GDP_capita](https://user-images.githubusercontent.com/54913677/145665781-aa0d32a5-7ec2-4ace-9900-d7f332052a58.png)
> A positive linear relationship is observed between World Happiness and GDP per capita. The slope tells us that for every one unit increase in GDP, there is an increase of 0.770 in the happiness score.

#### Social Support vs Happiness Score

![social_support](https://user-images.githubusercontent.com/54913677/145665988-403de8cb-dc3d-43ee-a0bf-7712fd224b67.png)
> A positive linear relationship is observed between World Happiness and social support. The slope tells us that for every one unit increase in social support, there is an increase of 7.309 in the happiness score.

#### Life Expectancy vs Happiness Score

![life_expectancy](https://user-images.githubusercontent.com/54913677/145665989-798cc833-6fb1-4aa7-9eef-911a1fc57d54.png)
> A positive linear relationship is observed between World Happiness and life expectancy. The slope tells us that for every one unit increase in life expectancy, there is an increase of 0.119 in the happiness score.

#### Clean Water vs Happiness Score

![clean_water](https://user-images.githubusercontent.com/54913677/145665993-17eb1313-9cf7-4156-a7f4-d5715c192f2d.png)
> A positive linear relationship is observed between World Happiness and clean water. The slope tells us that for every one unit increase in clean water, there is an increase of 0.034 in the happiness score.

#### Doctor per 10,000 people vs Happiness Score

![doc_per_10k](https://user-images.githubusercontent.com/54913677/145665995-e95c277e-63c6-4a92-80a5-d7076dec3757.png)
> A positive linear relationship is observed between World Happiness and medical doctor per 10,000 people. The slope tells us that for every one unit increase in medical doctor, there is an increase of 0.056 in the happiness score.


Through all the figures above, we can see that all the factors have a strong positive linear relationship with the happiness score. This means they are all directly related to happiness. If one of those factors declines, happiness also goes down. However, the one with the strongest relationship with happiness is `social support`. Because by definition, the larger the size of the correlation coefficient, the steeper the slope. It makes sense that we need social support to be happy. The one with the weakest relationship with happiness is `clean water`.


![heatmap](https://user-images.githubusercontent.com/54913677/145666441-2b1d2daa-d6c8-4316-adc5-8cb4461b308c.png)
>The correlation map above visualizes the correlation values between happiness scores and various evaluation factors that contribute to happiness score. It demonstrates a direct positive correlation between the Happiness Score of a country and economy, family, and health/ life expectancy.


### Future Work

During our data cleaning process, we grouped all data in the world happiness dataset by 'country' column by taking the mean values of each column for each individual country. Therefore, we do not have the data for each individual year in each country. The new COVID19 epidemic began in December 2019. There were a lot of countries with missing data for the years 2019 and on. For the future, if there is more data available, we want to do an individual analysis on COVID19 in correlation to the country's happiness. We want to determine the impact of COVID19 epidemic on the country's happiness. 



