# ADA made me famous!

## Abstract
### “Shoot for the moon. Even if you miss, you'll land among the stars.” Norman Vincent Peale

Did you ever dream of your words like the ones of Shakespeare, Einstein or Trump remaining forever etched in the memory of humanity?  Would you like to be famous? Then this project might help you!

We decided to explore what makes a famous quote. Is it its length? It’s topic? Or something only a proper EDA could reveal? The idea is to study a maximum number of features of quotes evaluated as ‘famous’ in order to try to characterize the perfect quote. Maybe this study will reveal some hidden patterns about them. Combined with ML and NLP, we could create a perfect quote generator and try to become famous thanks to ADA!

The main findings about this project can be find on the following website: https://manoui.github.io/website/

## Methods
You can find all the steps and methods detailed on the M3 notebook, if you are only interested in a specific part, use the index.

### Preprocessing and filtering
The notebook contains the performed preprocessing steps to obtain an exploitable and trustworthy dataset. Univariate analysis was carried out for each covariate to get a better understanding of the data. Then, multivariate data analysis will follow to understand the relation between the different covariates associated with a quote. 

### Exploratory Data Analysis
Once the dataset filtered and extended, we started to perform an univariate data analysis with summary statistics and graphical information on distribution of each covariate in order to get a better understanding of the data and design a more complex data analysis.

Then, multivariate data analysis will follow to understand the relation between the different covariates associated with a quote. We will use scatterplots in order to understand the correlation between the different variables and linear regression to have a more complete insight on their relation.


### Dataset enrichment
In order to enrich our dataset with new features, we needed to compute them using available methods. The first thing we extracted was the number of words and characters in a quote. Then, some NLP methods allowed us to extract for instance the polarity and subjectivity of a quote, that is to say its sentiment. We also computed the complexity of a sentence using the Gunning Fog score. Using Spacy, we identified the grammatical content of a sentence, that is to say the number of NOUNS, VERBS, ADJECTIVES etc. Entities present in the quote such as PERSON, PLACE, ORGANIZATION were also counted.

Info about the speakers:

We tried to retrieve the topic of a quote in order to see if a specific theme is more plebiscite than others. The most promising way to do so is by using topic modelling. The most popular topic modelling technique is called LDA which allows you to retrieve hidden themes in a text. It’s an unsupervised learning method that can be implemented in python.

It allows us to generate new features to complete our dataset and better characterize the quotes we are interested in, and that we hope will help with supervised learning methods and downstream analysis.



### Supervised Learning
We wanted to try different supervised learning ML models on the dataset, like random forest, CNN or logistic regression to predict using the available features if a given quote is famous or not. The idea would be to test different models and assess their performance using adequate metrics like accuracy or F1 score. Before training our models on the dataset, we wanted to explore how to enrich the features with more covariates since some models perform better with more variables.

Libraries to use: Sklearn (random forest and logistic regression), Keras (CNN)

### Unsupervised Learning
We tried different methods on unsupervised learning like:... But the results weren't conclusive so we didn't continue with trying to identify clusters in our data

### Sentence embeddings
We generated embeddings of the quotes using BERT model. This word representation allows to detect sentences that are closer in the embedding space and thus might reveal interesting patterns. Using PCA, we tried to visualize clustering by keeping 2 principal components. Unfortunalty, we didn't observe any clustering between the famous and not famous quotes so we left the embeddings aside for the final analysis.

### Text generation
The last step of the project was to build a 'famous quote generator' that learns how to generate a 'famous' quote that we can use to be famous thanks to ADA. We selected a corpus of the 1000 most famous quotes across years, ranging from 98263 to 1028 occurrences. The text was preprocessed in order to remove punctuation and numbers as well as multiple spacing. An LSTM model was created and trained on 100 epoch using this corpus. The output of the model is the probability of the next word in the sequence. Once the model was trained, we generated new sentences using a random seed of 4 words and limiting its length to 13 words since it is the median length of famous quotes.

The sentences generated are not too bad considering the small dataset and the simplicity of our model. It successfully link ideas like 'terrorism' or 'murder' to 'horrible', 'victims' or 'resilience'. The syntax is a bit sketchy at times, but the grammatical order is usually respected. We still could generate some nice quotes such as:
"These murderous attacks have once again showed us the total hatred of humanity.” This one could definitly become a famous quote.

# Task
* Manon: preprocessing, supervised learning, univariate data analysis, plotting
* Pauline: speaker features, supervised learning, website
* Elodie: feature enrichment using NLP, generation of embeddings, quote generator
* Oihana: topic extraction, figures, notebook

# What did we learn?
We really enjoyed working on the project, which was fun and motivating till the end. We discovered a lot of different tools to play around with the dataset we had, and there are still some possibilities that we didn't explored.  We were a bit disappointed not to find some groundbreaking info about what makes a famous quote, but we guess that's what ADA is about. Anyway, it teached us an important lesson: it is not really the quote which makes you famous but what you makes of it.







