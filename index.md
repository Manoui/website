

> # “Shoot for the moon. Even if you miss, you'll land among the stars.” Norman Vincent Peale
 
Did you ever dream of your words like the ones of Shakespeare, Einstein or Trump remaining forever etched in the memory of humanity? Would you like to be famous? Then this website might help you!

First, try to write something, we’ll tell you if your words will become famous:
"boo4"

"booo"
{% include button_1.html %}

Anyway, you better try our famous quote generator if you want to succeed, 100% chance of success. Click on the button and here we go:
** WIDGET (quote generator)**

{% include quotes_generator_final.html %}

Inspiring no? Post it right away on Twitter or Instagram and let the magic happen...
(What? nonsense you’re saying? I think that you are just not ready for that new vision on syntax)

** While you are waiting for the fame to come thanks to your quote, you can explore the data and read more about what makes a quote famous. **

Just think about politicians or advertisers that convinced you with just a few words, just by saying 'Yes we can!', 'Make America great again' or 'Logarithms are our friends'. This tiny little sentences made of 3 or 4 words have so much power when pronounced by Barack Obama, Donald Trump or Robert West that they are engraved forever in your mind. Not sure your colleague's remark in front of the coffee machine 'The weather is nice today.' will have as much impact on your brain...
Why does these quotes are so powerful? Is it because of their speaker? Is it because of the quote in itself? 
What makes that some quotes will be remembered forever and others will disappear into nothingness?

That's what we wanted to investigate with our data story, in order to unravel the mystery behind famous quotes.

First, we tried to look into the soul of the quote to find an answer. For instance, does the grammatical syntax plays a role in the fame of words? 
Or are negative quotes more famous than positive ones? Are some topics more trendy than others? Then, we tried to understand the impact of the speaker on
his/her quote. Are the emitters of famous quote distributed equally across continents? Is the fact that the speaker is alive or dead when the quote is cited important?
Are people related to sports more mediatized than artists? It is indeed of high interest for politicians, influencers or companies to generate the perfect quote that will catch people attention.

So while you have the time before the celebrity tornado sweeps you away, slip into the shoes of a data analysist to discover what impacts the fame of a quote!


## Say Hi to the dataset: Quotebank

The data used in this analysis is Quotebank, a corpus containing citations extracted from newspapers over the years 2008 to 2020. If you are interested in the methods used to extract quotes and attribute them to speakers, have a look at the [paper](https://dlab.epfl.ch/people/west/pub/Vaucher-Spitz-Catasta-West_WSDM-21.pdf). You can also use this related [tool](https://quotebank.dlab.tools) that allows you to enter a keyword and it will search the database for related quotes and show you its occurrence over time.

Using this set of quotes (2015-2020), we selected only the 1% most famous quotes with more than 215 occurrences in newspapers, and also sampled random quotes with less than 10 occurrences to be considered as non-famous. With this set of quotes we aim at analyzing what makes a quote famous or what makes it fall into the abyss of oblivion. In order to avoid artifacts of quotes being often cited because of differences in fame among speakers we selected famous and non-famous quotes from speakers appearing in the [Pantheon database](Yu, A. Z., et al. (2016). Pantheon 1.0, a manually verified dataset of globally famous biographies. Scientific Data 2:150075. doi: 10.1038/sdata.2015.75)). It was generated on the basis of Wikipedia bibliographies views, the number of different Wikipedia languages, the coefficient of variation etc. and it combines those values in a single metric, the historical popularity index (HPI).

OK enough with the boring pre-processing steps (crucial in data science tho).
Now let us dive into the data and see if we can answer our existential question.


### Who are the most cited people on this planet?

First, you can take a look at the top 20 of people emitting the most famous quotes, along with their number of cited quotes and THE quote with the most occurrences.

{% include famous_speakers.html %}

Unsurprisingly we see Donald Trump in the first place! He is even indirectly mentioned in the most famous quote of Pope Francis “A person who thinks only about building walls …”. It is also very interesting to see that politicians emitted the largest number of famous quotes, as they are highly mediatized and all their words are reported and analyzed in newspapers.

Let's look now at the dynamics over time. The figure below shows the number of famous quotes emitted over time (2015-2020) by the top 20 of the previous speakers. You can slide your cursor over the peaks to see the quote with the most citations at a specific date, you can zoom in, and also deselect some speakers.

{% include famous_speakers_timeseries.html %}

It is very interesting to see the different peaks and how they relate to highly mediatized events in English newspapers. 
* The peak in September 2016 of Donald Trump is during his presidential campaign were he “unleashes a blizzard of falsehoods, exaggerations and outright lies in the general election, peppering his speeches, interviews and Twitter posts with untruths so frequent that they can seem flighty or random — even compulsive.” 
* The peak of quotations in June 2017 of James Comey, former FBI director, coincides with its testimony after being fired by Donald Trump, and with Jeff Sessions peak, who originally recommended Trump about this firing. 
* Pope Francis visits Washington and New York City on the 24th of September 2015, which explains the quotations in newspapers, and on February 2016 he pronounces a powerful sentence about the American President “A person who thinks only about building walls -- wherever they may be -- and not building bridges, is not Christian ... ”
* The peak in April 2018 of Emmanuel Macron correspond to his speech to the Congress of the United States of America. 

You may already have realized that most of the quotations we collected from Quotebank are largely related to events mediatized in American newspapers. Here, below you can observe the proportion of famous quotes and non-famous quotes according to the speaker's origin.

{% include proportion_geo_famous.html %}

Oups there seem to be a bias in our dataset... Indeed most of the english quotes are from North America or Europe, and little from Africa, South America, Asia and Australia. It seems that quotes that are mediatized in english news articles are mainly from U.S.A., Canada and Europe, which is not surprising. We thus need to be careful in any conclusion we draw from our analysis since they might not apply universally.

### Take your bets!
                                                             
Now it is your turn to take guesses on what makes the fame of a quote by selecting some parameters and seeing their distribution across famous and ‘non-famous’ quotes. You can see parameters at the speakers level, as well as at the quote level. Indeed, using [TextBlob](https://pypi.org/project/textblob/0.9.0/) a natural language processing (NLP) library we defined the polarity and subjectivity of a quote. Polarity scores were calculated on the quotes and range from -1 (negative) to 1 (positive), with 0 representing neutral quotes. Subjectivity scores range from 0 to 1 and we consider subjective quotes with a score above 0.5. 
So, which individual features do you predict can differentiate famous from non-famous quotes?

{% include proportion_features_famous_nonfamous.html %}

Also, you may want to consider combining some features. What do you observe ?

{% include gender_occupation.html %}

Perhaps you are wondering, what are the quotes about? You may have already guessed that most famous quotations over time are related to politics, but justice also appears frequently, a bit less likely are arts and environment. Quotes were tagged using [Empath](https://arxiv.org/pdf/1602.06979.pdf), a tool that can generate and validate new lexical categories on demand from a small set of seed terms, which were manually defined based on Macmillan Thesaurus.

{% include topic_timeseries.html %}

Would you expect a difference in topics between famous and non-famous quotes? If yes which topics would be more or less prominent?

<img src="images/topics_quotes.jpeg" width="600" height="300"> 

Both types of quotes have a high percentage of quotes related to justice. Sports represents 21% of non-famous quotes, whereas it only makes up for 4.73% of famous quotes seems. Politics is in contrast twice much more present in famous quotes compared to non-famous.

It is also interesting the distribution of topics among famous speakers.

<img src="images/example_topics.jpeg" width="600" height="300"> 

**Du coup à enlever ?**
{% include nationality_occupation_complexity.html %}


### Predict fame

You may have already developed an intuition that most famous quotes are emitted by politicians in North America, covering mostly politics or justice. 

{% include famous_combinations.html %}
{% include nonfamous_combinations.html %}

Would you want to consider some additional parameters to predict the fame of a quote? 

**Did you think about the importance of words? What words would you expect to see based on previous observations ?**
{% include word_occurrence_stopwords.html %}

In the plot below you can slide over the plot with your cursor to see the most used words in famous versus non-famous quotes. There are a lot of similarities in the highly frequent words, such as the use of ‘people’, ‘going’, ‘think’, etc. But some frequent words are specific to the famous quotes: ‘us’, ‘president’, ‘country’, etc. as compared to ‘like’, ‘really’, ’time’ in non-famous quotes.
This relates to what you previously observed, in the majority of famous quotes are neutral, as compared to most positive quotes in non-famous ones. Moreover, you saw the high proportion of politician speakers in both the famous and non-famous datasets, which also explains the occurrence of some specific words.

We also considered several additional parameters such as:
* The length of a quote (the number of words, and characters)
* Whether a speaker was alive at the date of the citation.
* The historical popularity index (HPI) of a speaker.
* Grammatical features based on [Part-of-speech tags](https://spacy.io/usage/linguistic-features#pos-tagging) to quantify the number of adverbs, nouns, etc. that a quote contains. This allowed attributing a complexity score to the quotation.
* Named Entity Recognition [(NER)](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da) to identify the number of times a quote mentions a date, a person, an organization, an event, a language, etc.

**Let see if your intuition is correct and whether supervised learning methods agree with you ;)**

Using logistic regression and random forest as supervised learning classifiers, we were able to predict the fame of new quotes with an accuracy of 0.74 %. Here below, you can see which coefficients and their associated feature contributes the most to the prediction.

{% include logistic_regression_coefficients.html %}

{% include rf_coefficients.html %}


###Famous quote generator:
Some further explanation, about the quote generator you used at the top.

We selected a corpus of the 1000 most famous quotes across years, ranging from 98263 to 1028 occurrences. The text was preprocessed in order to remove punctuation and numbers as well as multiple spacing. An LSTM model was created and trained on 100 epoch using this corpus. The output of the model is the probability of the next word in the sequence. Once the model was trained, we generated new sentences using a random seed of 4 words and limiting its length to 13 words since it is the median length of famous quotes. 

Example of generated sentences:
> ”Ensure the safety and democracy in the face of enemies of freedom europe.”
> 
> ”And that was big she was crying when she saw me for republicans.”
> 
> ”These murderous attacks have once again showed us the total hatred of humanity.”
> 
> ”Values will be enhanced when women are granted their rights the meyerowitz stories.”
> 
> ”Relax there should be been an evacuation divinity original sin sin sin sin.”
> 
> ”Are united beyond all borders in horror and sorrow but also in determination.”
> 
> ”Assad regime and has been times of national tragedy took pill in ibiza.”
> 
> ”She weren’t my daughter it would be so much easier for her to.”


**Conclusion: the topic of a quote is of high importance, even more than the speaker's features or the characteristics of the sentence. Indeed, "Content is more than "subject matter. ' It is all the feelings and ideas you bring to your painting." - Rene Huyghe. The choice of words and the speaker are less important than the information it conveys. Didn't take into account intonation or speech context.**


#### References
Timoté Vaucher, Andreas Spitz, Michele Catasta, and Robert West. 2021. Quotebank: A Corpus of Quotations from a Decade of News. In The Four- teenth ACM International Conference on Web Search and Data Mining (WSDM ’21), March 8–12, 2021, Virtual Event, Israel. ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3437963.3441760

Hci.stanford.edu. 2021. [online] Available at: <https://hci.stanford.edu/publications/2016/ethan/empath-chi-2016.pdf> [Accessed 16 December 2021].
