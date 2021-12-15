

“Shoot for the moon. Even if you miss, you'll land among the stars.” Norman Vincent Peale
Did you ever dream of your words like the ones of Shakespeare, Einstein or Trump remaining forever etched in the memory of humanity? Would you like to be famous? Then this website might help you! First, try to write something, we’ll tell you if your words will become famous:

{%  include templates/index_1512_2.html  %}
-WIDGET (predict if sentence famous or not)-

(train a model only on quote features so the user doesn’t have to enter any info or ask for nationality, gender etc?)

Display a sentence based on the result:
-If ‘not famous’: Ouch too bad, did you really mean to say that? It sucks maybe, try our famous quote generator 
peut être marrant de mettre des phrases hyper cassantes comme sur How Bad Is Your Streaming Music? (pudding.cool)
-If ‘famous’: Wow impressive you’re definitely going somewhere with that spirit!

Anyway you better try our famous quote generator if you want to succeed, enter the first words of your sentence and the length of words and here we go:

-WIDGET (quote generator)-

Inspiring no? Post it right away on twitter or instagram and let the magic happen
-WIDGET (put the quote on a ‘inspirational quote background’)-
Un truc qui génère des images de ce type ça pourrait être marrant, avec un truc pour les poster direct sur insta ou fb haha

 
While you are waiting for the fame to come thanks to your quote, you can explore the data and read more about what makes a quote famous:
Graph interactif+ résultats intéressants, plus en mode rapport

Grammatical features:
Model makes a prediction of which tag is the most likely regarding the context. We generated some features that count the occurrences of a grammatical class in each sentence.
The grammatical features were generated using the universal POS tag thanks to SpaCy library. They count the number of adjectives, nouns, verbs etc in a sentence. 
Apparently there is no clear difference between the grammatical content/syntax of famous and mon-famous sentences. They are not considered as important features by the supervised learning models. We better try to look somewhere else...
Universal POS tags (universaldependencies.org)
Entity recognition:
We used Named Entity Recognition (NER) to extract entity information about quotes. Do they refer to a place? A person? Or an event? NER is a useful tool to extract meaningful information from sentences.  If multiple entities are present in one sentence, we chose the class with the most occurrences within that sentence in order to attribute only one main entity to a quote (i.e. if a quote is about a person, a place etc)
It appears that quotes about Work of Art 
PERSON People, including fictional.
NORP Nationalities or religious or political groups.
FAC Buildings, airports, highways, bridges, etc.
ORG Companies, agencies, institutions, etc.
GPE Countries, cities, states.
LOC Non-GPE locations, mountain ranges, bodies of water.
PRODUCT Objects, vehicles, foods, etc. (Not services.)
EVENT Named hurricanes, battles, wars, sports events, etc.
WORK_OF_ART Titles of books, songs, etc.
LAW Named documents made into laws.
LANGUAGE Any named language.
DATE Absolute or relative dates or periods.
TIME Times smaller than a day.
PERCENT Percentage, including "%".
MONEY Monetary values, including unit.
QUANTITY Measurements, as of weight or distance.
ORDINAL "first", "second", etc.
CARDINAL Numerals that do not fall under another type.

{% include famous_quotes_ts.html %}

## Famous quote generator:

We selected a corpus of the 1000 most famous quotes across years, ranging from 98263 to 1028 occurrences. The text was preprocessed in order to remove punctuation and numbers as well as multiple spacing. An LSTM model was created and trained on 100 epoch using this corpus. The output of the model is the probability of the next word in the sequence. Once the model was trained, we generated new sentences using a random seed of 4 words and limiting its length to 13 words since it is the median length of famous quotes. 

exemple of sentences:
-”Ensure the safety and democracy in the face of enemies of freedom europe.”
-”And that was big she was crying when she saw me for republicans.”
-”These murderous attacks have once again showed us the total hatred of humanity.”
-”Values will be enhanced when women are granted their rights the meyerowitz stories.”
-”Relax there should be been an evacuation divinity original sin sin sin sin.”
-”Are united beyond all borders in horror and sorrow but also in determination.”
-”Assad regime and has been times of national tragedy took pill in ibiza.”
-”She weren’t my daughter it would be so much easier for her to.”

<p float="left">
  <img src="/images/people_slogan.png" width="100" />
  <img src="/images/brand_slogan.pn" width="100" /> 
</p>



### Data Overview

People's slogan           |  Brands' slogan
:-------------------------:|:-------------------------:
![](/images/people_slogan.png){width=25%}  |  ![](/images/brand_slogan.png){width=25%}

A brand is a voice and a product is a souvenir. - Lisa Gansky
Nike – “Just Do it”
Red Bull — “Red Bull Gives You Wings”
Make America Great Again - Donald Trump
Yes we can. - Barack Obama

Ebaqdesign.com. 2021. Top Brand Slogans & How to Create One. [online] Available at: <https://www.ebaqdesign.com/blog/brand-slogans> [Accessed 15 December 2021].


Analyzing the fame of a quote is of high interest for example for politicians or brands. Indeed, they are seeking to generate a quote that sticks in your head. But what makes the fame of a quote ? Does it depend on the speaker, on the content, or on the length of a quote ?

First of all let see which speakers emitted the most famous quotes during the years 2015-2020. Unsurprisingly we see Donald Trump in the first place ! He is even indirectly mentionned in the most famous quote of Pope Francis “A person who thinks only about building walls …”. It is also very interesting to see that politicians emitted the largest number of famous quotes, as they are highly mediatized and all their words are reported and analyzed in newspapers.

{% include famous_speakers.html %}

The graph below shows the number of famous quotes emitted over time (2015-2020) by the top 20 of the previous speakers. It is very interesting to see the different peaks and how they relate to highly mediatized events in English newspapers. 
* The peak in September 2016 of Donald Trump is during its presidential compaign were he “unleashes a blizzard of falsehoods, exaggerations and outright lies in the general election, peppering his speeches, interviews and Twitter posts with untruths so frequent that they can seem flighty or random — even compulsive.” 
* The peak of quotations in June 2017 of James Comey, former FBI director, coincides with its testimony after being fired by Donald Trump, and with Jeff Sessions peak, who originally recommended Trump about this firing. 
* The Pope Francis visits Washington and New York City on the 24th of September 2015 “Thank you very much -- and God bless America!”
* The peak in April 2018 of Emmanuel Macron correspond to its speech to the Congress of the United States of America. 

{% include famous_speakers_timeseries.html %}

Let us now look at the proportion of famous quotes and non-famous quotes around the globe, as well as their co-occurrence with other features from the speakers emitting the quote.

{% include proportion_geo_famous.html %}

##### Topics
Over time:
{% include topic_timeseries.html %}

Distribution: 
![topics](topics_quotes.jpeg)

Some examples:
![Example_topics](example_topics.jpeg)

### Data distribution

Now it is your turn to take guesses on what makes the fame of a quote by selecting some parameters and see their distribution across famous and ‘non-famous’ quotes. Which features do you predict can differentiate famous from non-famous quotes ?

{% include proportion_features_famous_nonfamous.html %}

Combining features
{% include gender_occupation.html %}


## Data results

{% include famous_combinations.html %}

Combining features
{% include nationality_occupation_complexity.html %}

### The importance of words
Did you think about the importance of words ? What words would you expect to see based on previous observations ? 
Now let see if you were right :)

{% include word_occurrence_stopwords.html %}

In the plot below you can slide over the plot with your cursor to see the most used words in famous versus non-famous quotes. There are a lot of similarities in the highly frequent words, such as the use of ‘people’, ‘going’, ‘think’, etc. But some frequent words are specific to the famous quotes: ‘us’, ‘president’, ‘country’, etc. as compared to ‘like’, ‘really’, ’time’ in non-famous quotes.
These relates to what you previously observed, in the majority of famous quotes are neutral, as comapred to most positive quotes in non-famous ones. Moreover, you saw the high proportion of politician speakers in both the famous and non-famous dataset, which also explains the occurence of some specific words.


Using logistic regression as supervised learning to try to classify whether a quote will be famous or not, the coefficient contributing the most are displayed here below.

{% include logistic_regression_coefficients.html %}

Using random forest as supervised learning to try to classify whether a quote will be famous or not, the coefficient contributing the most are displayed here below.

{% include rf_coefficients.html %}

**Have fun and play with the plot! It supports the interpretations we made previously!**
Feel free to investigate the graphs by activating the traces for averaging over different time ranges and/or by zooming in! The number of elections or votes is visualized by the diameter of the bubbles.


***About the elections* (second plot):***
What about the *large green bubble* ? It accounts for the near-thousand elections was were closed in the month of May 2007 -- encompassing two of our election-closure pics!



**Conclusion: Give people time to know you, to hear your opinions, and discuss about your program, increasing your election duration might increase your chances of winning!**



#### **Can we observe social network theories? 
#### Or
#### Are people influenced by other people's votes and can tendencies be reversed ?**


That does look somewhat confusing to you maybe but no worries, we put the message behind this graph into numbers for you. Long story short, there is a **20%** chance that the election outcome might still switch around until the end of the election. So don't just start your celebration yet, no one likes people that claim victory before they've actually won ([we have no one specific in mind of course](https://www.youtube.com/watch?v=W9d6j2uO6MI)). Concerning your bottle of champagne however, keep it within reach, [in case of victory you'll deserve it, in case of defeat you'll need it](https://vinepair.com/articles/fake-drinking-quotes/).


