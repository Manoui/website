

> “Shoot for the moon. Even if you miss, you'll land among the stars.” Norman Vincent Peale

Did you ever dream of your words like the ones of Shakespeare, Einstein or Trump remaining forever etched in the memory of humanity? Would you like to be famous? Then this website might help you! First, try to write something, we’ll tell you if your words will become famous:

**WIDGET (predict if sentence famous or not)**

{%  include templates/index_1512_2.html  %}
(train a model only on quote features so the user doesn’t have to enter any info or ask for nationality, gender etc?)

Display a sentence based on the result:
* If ‘not famous’: Ouch too bad, did you really mean to say that? It sucks maybe, try our famous quote generator 
peut être marrant de mettre des phrases hyper cassantes comme sur How Bad Is Your Streaming Music? (pudding.cool)
* If ‘famous’: Wow impressive you’re definitely going somewhere with that spirit!

Anyway you better try our famous quote generator if you want to succeed, enter the first words of your sentence and the length of words and here we go:

** WIDGET (quote generator)**

Inspiring no? Post it right away on twitter or instagram and let the magic happen
-WIDGET (put the quote on a ‘inspirational quote background’)-
Un truc qui génère des images de ce type ça pourrait être marrant, avec un truc pour les poster direct sur insta ou fb haha

 
** While you are waiting for the fame to come thanks to your quote, you can explore the data and read more about what makes a quote famous. **


<p float="left">
  <img src="images/people_slogan.png" width="250" height="250">
  <img src="images/brand_slogan.png" width="400" height="400"> 
</p>


I would bet these slogan ring a bell to you! Those quotes emitted by famous personnalities remain in your mind and are cited over again, but why ? Whats makes the fame of those quotes. This is the million dollar question. 

"A brand is a voice and a product is a souvenir."- Lisa Gansky
Consumers use products, but the brand is what speaks to them. One recent exemple is Dacia with its "Everybody drives a duster.", that advertisement for sure caught your attention, perhaps you even sang, as compared to other car advertisements that were left unoticed. 

Mediatized people often want to make the buzz, in order to create their own brand and remain famous. A precident has also a slogan during its compaign, and it should be short, appealing and stick in your head. It is of high interest to generate a famous that will be cited multiple times.

So what makes the fame of a quote ? Does it depend on the speaker, on the content, or on the length of a quote ? Through this website, you will fit the shoes of a data analysis to discover what parameters define the fame of a quote.


### What are the trends ?

First of all let see which famous speakers (based on the [Pantheon database](Yu, A. Z., et al. (2016). Pantheon 1.0, a manually verified dataset of globally famous biographies. Scientific Data 2:150075. doi: 10.1038/sdata.2015.75)) emitted the most famous quotes during the years 2015-2020. 

{% include famous_speakers.html %}

Unsurprisingly we see Donald Trump in the first place ! He is even indirectly mentionned in the most famous quote of Pope Francis “A person who thinks only about building walls …”. It is also very interesting to see that politicians emitted the largest number of famous quotes, as they are highly mediatized and all their words are reported and analyzed in newspapers.

Let's look now at the dynamics over time. The figure below shows the number of famous quotes emitted over time (2015-2020) by the top 20 of the previous speakers. You can slide your cursor over the peaks to see the quote with the most citations at a specific date, you can zoom in, and also deselect some speakers.

{% include famous_speakers_timeseries.html %}

It is very interesting to see the different peaks and how they relate to highly mediatized events in English newspapers. 
* The peak in September 2016 of Donald Trump is during its presidential compaign were he “unleashes a blizzard of falsehoods, exaggerations and outright lies in the general election, peppering his speeches, interviews and Twitter posts with untruths so frequent that they can seem flighty or random — even compulsive.” 
* The peak of quotations in June 2017 of James Comey, former FBI director, coincides with its testimony after being fired by Donald Trump, and with Jeff Sessions peak, who originally recommended Trump about this firing. 
* Pope Francis visits Washington and New York City on the 24th of September 2015, which explains the quotations in newspapers, and on February 2016 he pronounces a powerful sentence about the American President “A person who thinks only about building walls -- wherever they may be -- and not building bridges, is not Christian ... ”
* The peak in April 2018 of Emmanuel Macron correspond to its speech to the Congress of the United States of America. 

You may already have realized that most of the quotations we collected from Quotebank are largely related to events mediatized in American newspapers. Here, below you can observe the proportion of famous quotes and non-famous quotes according to the speakers origin.

{% include proportion_geo_famous.html %}


### The bets are open
                                                             
Now it is your turn to take guesses on what makes the fame of a quote by selecting some parameters and see their distribution across famous and ‘non-famous’ quotes. Which individual features do you predict can differentiate famous from non-famous quotes ?

{% include proportion_features_famous_nonfamous.html %}

Also, consider combining some features. What do you observe ?

{% include gender_occupation.html %}

Perahps you are wondering, what are the quotes about ? You may have already guessed that most famous quotations over time are related to politics, but justice also appears frequently, a bit less lkely are arts and environment. 

{% include topic_timeseries.html %}

Would you expecte a difference in topics between famous and non-famous quotes ? If yes which topics would be more or less prominent ?

<img src="images/topics_quotes.jpeg" width="600" height="300"> 

Both types of quotes have a high percentage of quotes related to justice. Sports represents 21% of non-famous quotes, whereas it only makes up for 4.73% of famous quotes seems. Politics is in contrast twice much more present in famous quotes compared to non-famous.

It is also interesting the distribution of topics among famous speakers.

<img src="images/example_topics.jpeg" width="600" height="300"> 

Du coup à enlever ?
{% include nationality_occupation_complexity.html %}

### Predict fame

You may have already developed an intuition that most famous quotes are emitted by politicians in North America, covering mostly politics or justice. 

{% include famous_combinations.html %}

Would you want to consider to some additional parameters to predict the fame of a quote? 

**Did you think about the importance of words ? What words would you expect to see based on previous observations ?**

{% include word_occurrence_stopwords.html %}

In the plot below you can slide over the plot with your cursor to see the most used words in famous versus non-famous quotes. There are a lot of similarities in the highly frequent words, such as the use of ‘people’, ‘going’, ‘think’, etc. But some frequent words are specific to the famous quotes: ‘us’, ‘president’, ‘country’, etc. as compared to ‘like’, ‘really’, ’time’ in non-famous quotes.
These relates to what you previously observed, in the majority of famous quotes are neutral, as comapred to most positive quotes in non-famous ones. Moreover, you saw the high proportion of politician speakers in both the famous and non-famous dataset, which also explains the occurence of some specific words.

**Let see if your intuition is correct, and whether supervised learning methods agree with you ;)**

Using logistic regression and random forest as supervised learning classifiers, we were able to predict the fame of new quotes with an accuracy of 0.74 %. Here below, you can see which coefficients and the associated feature contributing the most to the prediction.

{% include logistic_regression_coefficients.html %}

{% include rf_coefficients.html %}

**Conclusion: the topic of a quote is of high importance, even more than the speakers features or the characteristics of the sentence. Indeed, "Content is more than "subject matter. ' It is all the feelings and ideas you bring to your painting." - Rene Huyghe. The choice of words and the speaker are less important than the information it conveys. **



