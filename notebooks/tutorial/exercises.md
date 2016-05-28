## Exercises

### Preprocessing

The primary responsibility you will have before any task involving NLP is to ingest and transform raw text into a corpus that can then be used for performing further evaluations. NLTK provides many corpora for you to work with for exploration, but you must become able to design and construct your own corpora, and to implement `nltk.CorpusReader` objects - classes that in a memory safe and efficient way are able to read entire corpora and analyze them.

Many people get away with the `nltk.PlainTextCorpusReader` - which uses built-in taggers and tokenizers to deal with raw text. However, this methodology leaves you at the mercy of the tagging model that you have provided, and does not allow you to make corrections that are saved in between runs. Instead you should preprocess your text to allow it to be read by the `nltk.corpus.TaggedCorpusReader` or the penultimate corpus, the `nltk.corpus.BracketParseCorpusReader`.

In this task, you will transform raw text into a format that can then be read by the `nltk.corpus.TaggedCorpusReader`. See the documentation at [http://www.nltk.org/api/nltk.corpus.reader.html](http://www.nltk.org/api/nltk.corpus.reader.html) for more information on this reader.

You will find 20-40 documents of recent tech articles from Engadget and Tech Crunch at the following link: [http://bit.ly/nlpnltkcorpus](http://bit.ly/nlpnltkcorpus) - please download them to your local file system. Write a Python program that uses NLTK to preprocess these documents into a format that can be easily read by the `nltk.corpus.TaggedCorpusReader`.

Note that you will have to process these files and remove HTML tags and you might have to do other tasks related to the clean up; to do this I suggest you use the third party library BeautifulSoup which can be found at [http://www.crummy.com/software/BeautifulSoup/](http://www.crummy.com/software/BeautifulSoup/). See also Chapter 3 in the NLTK book for more information.

#### Evaluation

1. What is the word count and vocabulary of this corpus?
2. What is the lexical diversity of the corpus?
3. What are the 5 most common lexical categories (parts of speech)?
4. What are the 10 most common unigrams, the 10 most common bigrams? (please exclude stopwords, using the `nltk.corpus.stopwords('english')` list)
5. How many nouns are in the corpus?

<a id='parse'></a>
### Parsing

Given a seed inventory of pre-terminal and non-terminal symbols (grammatical categories) and a sample lexicon, write a grammar for English noun phrases. Your grammar should cover all legal structures of noun phrases used by the grammatical categories provided. You must include the following:

- noun-noun compounds ("brick wall", "lawn chair")
- relative clauses of the form Rel-Cl ⟶ Rel-Pro V NP ("[the ball] that hit her")

**Note:** You do not need to cover more than one PP in a row, more than one adjective in a row, noun-noun compounds of length > 2, quantifiers followed by determiners ("all of these") or mass nouns ("beer", "sincerity")

You should then write a program that uses an NLTK parser and the grammar you constructed that will return a syntactic tree if the input is a noun phrase or None if the input is ungrammatical. Your program will have to take the input sentence, tokenize it and then tag it according to the lexicon (you can assume that words in this lexicon do not have multiple senses) - you'll then have to pass the grammar phrase (the tags) to the parser.

#### Tagset

    N = noun
    NP = noun phrase
    Adj = adjective
    AdjP = adjective phrase
    Adv = adverb
    Prep = preposition
    PP = prepositional phrase
    Quant = quantifier
    Ord = ordinal numeral
    Card = cardinal numeral	Rel-Cl = relative clause
    Rel-Pro = relative pronoun
    V = verb
    S = sentence
    Det = determiner
    Dem-Det = demonstrative determiner
    Wh-Det = wh-determiner
    PPron = personal pronoun
    PoPron = possessive pronoun

#### Sample Lexicon

    a            Det
    an           Det
    at           Prep
    airplane     NSg
    airplanes    NPl
    airport      NSg
    airports     NPl
    any          Quant
    beautiful    Adj
    big          Adj
    eat          V
    eats         V3Sg
    finished     VPastPP
    four         Card
    fourth       Ord
    he           PPron
    his          PoPron
    in           Prep
    many         Quant
    my           PoPron
    new          Adj
    of           Prep
    offered      VPastPP
    on           Prep
    restaurant   NSg
    restaurants  NPl
    runway       NSg
    runways      NPl
    second       Ord
    some         Quant
    that         Dem-DetSg
    that         Rel-Pro
    the          Det
    this         Dem-DetSg
    these        Dem-DetPl
    third        Ord
    those        Dem-DetPl
    three        Card
    two          Card
    very         Adv
    which        Wh-Det
    who          Wh-Det
    you          PPron

#### Evaluation Phrases

- "Four new airports"
- "Very new airport runways"
- "His second house"
- "Some beautiful dishes which a restaurant offered"
- "The runway that the airport built"

<a id='classify'></a>
### Document Classification

In the first week you created an ingestion mechanism and an NLTK corpus reader for a set of RSS feeds. These feeds potentially have topics associated with them (broad tags like tech, news, sports, etc). In this question you'll build a classifier on a data set of RSS feeds that is provided in the course materials to decide whether or not you can categorize the various topics using one of the classifiers you learned in this week.

The corpus is constructed as follows. Each individual blog post is in its own HTML file stored in a directory labled with the topic. Use the `nltk.CategorizedCorpusReader` or the `nltk.CategorizedPlaintextCorpusReader` to construct your corpora (you may review how the movie reviews data set is structured). To do this you need to pass to the corpus the path to the root of your corpus, and a regular expression to match file names. You also need to use a regular expression passed as the `cat_pattern` keyword argument, which is used to match the category labels. Here is an example for the spam corpus:

    from nltk.corpus import CategorizedPlaintextCorpusReader as EmailCorpus

    corpus   = EmailCorpus("./data/nbspam", r'(?!\.).*\.[a-f0-9]+',
                   cat_pattern=r'(spam|ham)/.*', encoding='iso-8859-1')

    print(corpus.categories())
    print(corpus.fileids())

Create a test set, a dev test set, and a training set from randomly shuffled documents that are in the corpus to use in your development. Save these sets to disk with pickles to ensure that you can develop easily with them.

Create a function that extracts features per document. Choose any features you would like. One idea is to use the most common unigrams; you might be able to use common bigrams as well. If you can think of any other features, feel free to include them as well (maybe an includes_recipe feature, etc.)) You may want to consider a TF-IDF feature to improve your results.

Train the classifier of your choice on the training data, and then improve it with your dev set. Report your final accuracy and the most informative features by running the accuracy checker on the final test set.

#### Evaluation

1. Report accuracy and most informative features of classifier (4 points)
2. Show complete work with submitted Python code (6 points)
3. Create a corpus reader that extends a built-in NLTK corpus reader (4 points)
4. Create an efficient feature extractor (4 points)
5. Achieve an accuracy with your classifier of greater than 85% (2 points)

### Product Classification

The second question involves comparing and contrast the Naive Bayes Classifier with the Maximum Entropy classifier. You will be given an abbreviated data set of product names and their descriptions as well as their label (tops, bottoms, shoes, etc.) - similarly to question one, create a corpus that can read the CSV file - you may want to look at the `nltk.corpus.WordListCorpusReader` for inspiration about how to create such a corpus (each product is on a single line).

Create test and training sets from the data then build both a NaiveBayes and Maxent classifier - make sure that you save these classifiers to disk using the `pickle` module! The Maxent classifier in particular will take a long time to train. Once they're trained; report the accuracy of each as well as the most informative features. Are there any surprises? Which classifier performs better?
