<div id="just-line-break"></div>
<div id="just-line-break"></div>
<div id="just-line-break"></div>
<div id="just-line-break"></div>
<div id="just-line-break"></div>
<div id="just-line-break"></div>
<div id="just-line-break"></div>
<div id="just-line-break"></div>

<br/>

<div id="line-break-and-tab"></div>
<div id="just-line-break"></div>
<br/>
<div id="line-break-and-tab"></div>


<p style="text-align:center">
   <font size="6" id="lien">
     <b>Did you ever dream of your words like the ones of Shakespeare, Einstein, or Trump remaining forever etched in the memory of humanity ? Would you like to be famous ? Then this website might help you !</b>
   </font>
 

</p>


***

<div id="just-line-break"></div>
<br/>
<div id="line-break-and-tab"></div>

     
### First, try to write something, we’ll tell you if your words have a chance to become famous (max 140 characters):
{% include button_1.html %}

### Anyway, you better try our **famous quote generator** if you want to succeed
<p style="text-align:center">
   <font size="5" id="lien">
     <b>Click on the button and here we go:</b>
   </font>
</p>


{% include quotes_generator_final.html %}

### **Inspiring no?** Post it right away on Twitter or Instagram and let the magic happen... 
(What? The syntax isn't right? ? Maybe our generator needs a little bit more training)

<p style="text-align:center">
   <font size="5" id="lien">
     <b>While you are waiting for the fame to come thanks to your quote, you can explore the data and read more about what makes a quote famous.</b>
   </font>
</p>


Just think about politicians or advertisers that convinced you with just a few words, just by saying 'Yes we can!', 'Make America great again' or 'Logarithms are our friends'. These tiny little sentences made of 3 or 4 words have so much power when pronounced by Barack Obama, Donald Trump, or Robert West that they are engraved forever in your mind. Not sure your colleague's remark in front of the coffee machine 'The weather is nice today.' will have as much impact on your brain...
Why do these quotes are so powerful? Is it because of their speaker? Is it because of the quote in itself? 
What makes that some quotes will be remembered forever and others will disappear into nothingness?

That's what we wanted to investigate with our data story, in order to unravel the mystery behind famous quotes.

First, we tried to look into the soul of the quote to find an answer. For instance, does grammatical syntax play a role in the fame of words? 
Or are negative quotes more famous than positive ones? Are some topics more trendy than others? Then, we tried to understand the impact of the speaker on
his/her quote. Are the emitters of famous quotes distributed equally across continents? Is the fact that the speaker is alive or dead when the quote is cited important?
Are people related to sports more mediatized than artists? It is indeed of high interest for politicians, influencers, or companies to generate the perfect quote that will catch people's attention.

**So while you have the time before the celebrity tornado sweeps you away, slip into the shoes of a data analysist to discover what impacts the fame of a quote!**


## Say Hi to the dataset: Quotebank

The data used in this analysis is Quotebank, a corpus containing citations extracted from newspapers over the years 2008 to 2020. If you are interested in the methods used to extract quotes and attribute them to speakers, have a look at the [paper](https://dlab.epfl.ch/people/west/pub/Vaucher-Spitz-Catasta-West_WSDM-21.pdf). You can also use this related [tool](https://quotebank.dlab.tools) that allows you to enter a keyword and it will search the database for related quotes and show you its occurrence over time.

Using this set of quotes (2015-2020), we selected only the 1% most famous quotes with more than 215 occurrences in newspapers, and also sampled random quotes with less than 10 occurrences to be considered as non-famous. With this set of quotes, we aim at analyzing what makes a quote famous or what makes it fall into the abyss of oblivion. In order to avoid artifacts of quotes being often cited because of differences in fame among speakers we selected famous and non-famous quotes from speakers appearing in the [Pantheon database](Yu, A. Z., et al. (2016). Pantheon 1.0, a manually verified dataset of globally famous biographies. Scientific Data 2:150075. doi: 10.1038/sdata.2015.75)). It was generated on the basis of Wikipedia bibliographies views, the number of different Wikipedia languages, the coefficient of variation etc. and it combines those values in a single metric, the historical popularity index (HPI).

OK enough with the boring pre-processing steps (crucial in data science tho).
Now let us dive into the data and see if we can answer our existential question.


## Who are the most cited people on this planet?

First, you can take a look at the top 20 of people emitting the most famous quotes, along with their number of cited quotes and THE quote with the most occurrences.

{% include famous_speakers.html %}

Unsurprisingly we see Donald Trump in the first place! He is even indirectly mentioned in the most famous quote of Pope Francis “A person who thinks only about building walls …”. It is also very interesting to see that politicians emitted the largest number of famous quotes, as they are highly mediatized and all their words are reported and analyzed in newspapers.

Let's look now at the dynamics over time. The figure below shows the number of famous quotes emitted over time (2015-2020) by the top 20 of the previous speakers. You can slide your cursor over the peaks to see the quote with the most citations at a specific date, you can zoom in, and also deselect some speakers.

{% include famous_speakers_timeseries.html %}

It is very interesting to see the different peaks and how they relate to highly mediatized events in English newspapers. 
* The peak in September 2016 of Donald Trump is during his presidential campaign where he “unleashes a blizzard of falsehoods, exaggerations and outright lies in the general election, peppering his speeches, interviews and Twitter posts with untruths so frequent that they can seem flighty or random — even compulsive.” 
* The peak of quotations in June 2017 of James Comey, former FBI director, coincides with its testimony after being fired by Donald Trump, and with Jeff Sessions peak, who originally recommended Trump about this firing. 
* Pope Francis visits Washington and New York City on the 24th of September 2015, which explains the quotations in newspapers, and on February 2016 he pronounces a powerful sentence about the American President “A person who thinks only about building walls -- wherever they may be -- and not building bridges, is not Christian ... ”
* The peak in April 2018 of Emmanuel Macron correspond to his speech to the Congress of the United States of America. 

You may already have realized that most of the quotations we collected from Quotebank are largely related to events mediatized in American newspapers. Here, below you can observe the proportion of famous quotes and non-famous quotes according to the speaker's origin.

{% include proportion_geo_famous.html %}

Oups there seem to be a bias in our dataset... Indeed most of the English quotes are from North America or Europe, and little from Africa, South America, Asia and Australia. It seems that quotes that are mediatized in English news articles are mainly from U.S.A., Canada and Europe, which is not surprising. We thus need to be careful in any conclusion we draw from our analysis since they might not apply universally.

## Take your bets!
                                                             
Now it is your turn to take guesses on what makes the fame of a quote by selecting some parameters and seeing their distribution across famous and ‘non-famous’ quotes. You can see parameters at the speakers level, as well as at the quote level. Using [TextBlob](https://pypi.org/project/textblob/0.9.0/) a natural language processing (NLP) library we defined the polarity and subjectivity of a quote. Polarity score range from -1 (negative) to 1 (positive), with 0 representing neutral quotes. Subjectivity score range from 0 to 1 and we consider subjective quotes with a score above 0.5 (subjective quotes express an opinion or feeling as opposed to factual quotes).
So, which individual features do you think can differentiate famous from non-famous quotes? (more info about the features under the figure)

{% include proportion_features_famous_nonfamous.html %}

The jobs are defined as followed:
* POLITICS: politician, judge, lawyer, social activist etc
* NEGATIVE_CONNOTATION_JOB: pornographic actor, mafioso, poker player, extremist etc
* MEDIA_ARTS: comedian, singer, presenter etc
* MEDIA_SCIENCE: inventor, astronaut etc (such as Elon Musk)
* ARTS: photographer, film maker, painter etc
* SPORTS: athletes, soccer player, coach etc
* SCIENCES: physician, chemist etc

Also, you may want to consider combining some features. What do you observe ?

{% include gender_occupation.html %}

We see that for both genders politicians are the most represented in the famous quotes. But we can see that there is a higher proportion of women in MEDIA_ARTS who are quoted than men. We can observe the inverse effect for SPORTS, where men quotes are more represented. In general, non-famous quotes have better coverage of all topics whereas famous quotes are centered around politics, media arts and sports.

Perhaps you are wondering, what are these quotes about? Maybe that's what makes them famous! Let's take a look into the topic distribution over famous and non-famous quotes. Would you expect a difference in topics between famous and non-famous quotes? If yes which topics would be more or less prominent?

{% include topic_timeseries.html %}

You may have already guessed that most famous quotations over time are related to justice and politics. Whereas arts and environment are a bit less likely (maybe the consequence of a certain climate sceptic president...?). Quotes were tagged using [Empath](https://arxiv.org/pdf/1602.06979.pdf) and generating manually lexical fields for topics.

{% include topic_analysis.html %}

Both types of quotes have a high percentage of quotes related to justice. Sports represents 21% of non-famous quotes, whereas it only makes up for 4.73% of famous quotes seems. Politics is in contrast twice much more present in famous quotes compared to non-famous.

It is also fun to see the distribution of topics among famous speakers, let's take a look at the quotes from Trump and Pope Francis:

{% include topic_analysis_DT_PF.html %}

We also analyzed if a quote mentioned a place, a person, a work of art, an organization etc and see if it affected its number of citations (the legend is below the graph if not clear):

{% include theme_analysis.html %}

The key is the following:
* PERSON: People, including fictional.
* NORP: Nationalities or religious or political groups.
* FAC: Buildings, airports, highways, bridges, etc.
* ORG: Companies, agencies, institutions, etc.
* GPE: Countries, cities, states.
* LOC: Non-GPE locations, mountain ranges, bodies of water.
* PRODUCT: Objects, vehicles, foods, etc. (Not services.)
* EVENT: Named hurricanes, battles, wars, sports events, etc.
* WORK_OF_ART: Titles of books, songs, etc.
* LAW: Named documents made into laws.
* LANGUAGE: Any named language.
* DATE: Absolute or relative dates or periods.
* TIME: Times smaller than a day.
* PERCENT: Percentage, including "%".
* MONEY: Monetary values, including unit.
* QUANTITY: Measurements, as of weight or distance.
* ORDINAL: "first", "second", etc.
* CARDINAL: Numerals that do not fall under another type
* NONE: no entity detected

As you can see, making reference to one of the entities mentioned above doesn't seem to play a role in the fame of a quote. The distribution is more or less the same between famous and non-famous quotes so we better look somewhere else...

## How to be a mainstream famous quote emitter:

You may have already developed an intuition that most famous quotes are emitted by politicians in North America, covering mostly politics or justice. Let's see what combinations of the previously seen parameters seem to be the most successful when it comes to having a famous quote:

{% include famous_combinations.html %}

Uh-oh it looks like you have to be **a male politician from North America talking about politics** if you want to be quoted somewhere. Too bad if you don't enter this box, but you can always give it a try :)
Now let's take a look at the combinations that yield non-famous quotes:

{% include nonfamous_combinations.html %}

Ok so it looks like **European athletes that talk about sports** are not really popular... Just stop doing sports, move to USA and do politics if you want to be famous.
Now that we have a better overview of the profile of speakers behind famous quotes, we can take a closer look at the quotes.

## Is the word 'platypus' often used in famous sentences?
In the plot below you can slide over the plot with your cursor to see the most used words in famous versus non-famous quotes:

{% include word_occurrence_stopwords.html %}


There are a lot of similarities in the highly frequent words, such as the use of ‘people’, ‘going’, ‘think’, etc. But some frequent words are specific to the famous quotes: ‘us’, ‘president’, ‘country’, etc. as compared to ‘like’, ‘really’, ’time’ in non-famous quotes.
This relates to what you previously observed, you saw the high proportion of politician speakers in both the famous and non-famous datasets, which also explains the occurrence of some specific words.

We also considered several additional parameters such as:
* The length of a quote (the number of words, and characters)
* Whether a speaker was alive at the date of the citation.
* The historical popularity index (HPI) of a speaker.
* Grammatical features based on [Part-of-speech tags](https://spacy.io/usage/linguistic-features#pos-tagging) to quantify the number of adverbs, nouns, etc. that a quote contains. 
* Named Entity Recognition [(NER)](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da) to identify the number of times a quote mentions a date, a person, an organization, an event, a language, etc.
* Complexity score using [Gunning Fog rating](https://en.wikipedia.org/wiki/Gunning_fog_index)

We chose only to present the most interesting results in this article but you can go and check on our Github for more about the methods and results: https://github.com/epfl-ada/ada-2021-project-aficionada

Here are the main info about famous and not famous quotes:
* 50% of the famous quote have at least 13 words compared to 20 for non famous -> non-famous quotes tend to be longer
* 50% of the famous quote have at least a polarity of 0 (neutral) compared to 0.04 (neutral) for non-famous -> no difference
* 50% of the famous quote have at least a subjectivity of 0.35 (quite factual) compared to 0.41 (quite factual) for non-famous -> no difference
* 50% of the famous quote have at least a Gunning Fog complexity score of 16 (quite complicated) compared to 14 (quite complicated) for non-famous -> no difference

As you can see, the secret behind famous quotes doesn't really seem to rely on syntax, complexity or sentiment.

## And what does machine learning think about it?

Now let's check if your intuitions were correct. Have you already heard about Machine Learning (ML for close friends)? Anyway, don't worry this is not the time and place to discuss stochastic gradient descent algorithms ;)
The only thing you need to know is that we created ML models that given an unseen quote, can predict if the quote will be famous or not. We trained a Logistic Regression model (don't panic if you never heard about it). And our model predicted the fame of new quotes with an accuracy of 73 %! That is to say, it could tell in 73% of cases if a quote was famous or not. Here below, you can see which coefficients and their associated feature contribute the most to the prediction.

In the graph below, these are the coefficients we obtained for our Logistic Regression model. Don't worry if you don't understand 100% this graph, the only thing you need to know is that features with positive coefficient values will augment the chance of a quote being famous, whereas coefficient with negative values will lower the chance of a quote to be famous. Values close to zero means the feature doesn't really have an impact to predict if a quote is famous or not.

{% include logistic_regression_coefficients.html %}

For instance, being a politician augments your chance of having a famous quote, which confirms what we saw previously. Whereas coming from Asia really lowers your chance for your quote to be famous... (in English newspaper at least). The number of characters doesn't seem to impact the prediction of our model.

It is interesting to see that ML algorithms retrieve phenomenons we identified before, it also gives new ideas to design a more complex analysis.

## Famous quote generator:
Some further explanation, about the quote generator you used at the top in case you are curious about it :)

We selected a corpus of the 1000 most famous quotes across years, ranging from 98263 to 1028 occurrences in newspapers. The text was preprocessed in order to remove punctuation and numbers as well as multiple spacing. We trained a model (ML again!!!) on this corpus that learned the syntax and vocabulary of this corpus. The output of the model is the probability of the next word in a sequence of words (i.e. after 'I' one probable word is 'am' for instance). Once the model learned how to 'speak' in English, we generated new sentences limiting its length to 13 words since it is the median length of famous quotes. Ok the syntax is not perfect but the generator links successfully ideas like 'terrorism' and 'violence' or 'floods' and 'boat'. With more time and resources we could surely generate better quotes! --> invest in [Aficionada!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

Example of cool generated sentences:
> ”Ensure the safety and democracy in the face of enemies of freedom europe.”
> 
> ”And that was big, she was crying when she saw me for republicans.”
> 
> ”These murderous attacks have once again showed us the total hatred of humanity.”
> 
> ”Often innocent blood doesn much matter to the dead they re going to.”
> 
> ”Are united beyond all borders in horror and sorrow but also in determination.”
> 
> ”In political history what important is that everybody work together to ensure to.”

Wow some are very powerful and inspiring.


### Conclusion
We hope you enjoyed your time on this website. We saw that the syntax and sentiment of a quote are not that important in making it famous or not. Most of the emitters of famous quotes are politicians, but it is not surprising because they are highly mediatized in the newspapers. Maybe they have a special talent with words? However, as a good data scientist, you must acknowledge the limitations of your analysis. First, we saw that most of the quotes we have are from North America so the results are a bit biased. Also, we didn't take into account the intonation or speech context which might play an important role in how a quote is portrayed in the press. Anyway, quick go and check if your quote buzzed on the internet!

<div id="just-line-break"></div>
<br/>
<div id="line-break-and-tab"></div>

<p style="text-align:center">
   <font size="5" id="lien">
     <i>Thanks for reading! We shot for the moon and landed in the stars...<br> -The Aficionada Team-</i>
   </font>

</p>


<div id="just-line-break"></div>

<div id="just-line-break"></div>
<br/>
<div id="line-break-and-tab"></div>

### References

* Timoté Vaucher, Andreas Spitz, Michele Catasta, and Robert West. 2021. Quotebank: A Corpus of Quotations from a Decade of News. In The Four- teenth ACM International Conference on Web Search and Data Mining (WSDM ’21), March 8–12, 2021, Virtual Event, Israel. ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3437963.3441760

* Hci.stanford.edu. 2021. [online] Available at: <https://hci.stanford.edu/publications/2016/ethan/empath-chi-2016.pdf> [Accessed 16 December 2021].

* GitHub link for the README and the Python notebook: https://github.com/epfl-ada/ada-2021-project-aficionada.git


