from kadot import Text
from kadot.classifiers import BayesClassifier

# This is a small improvised dataset :)
sentiment_texts = {
    "These pizzas are so good !": 'positive',
    "I'm allergic to pizzas": 'negative',
    "Flowers are a so good choice of gift": 'positive',
    "This gift is broken !": 'negative'
}

bayes = BayesClassifier()
bayes.fit(sentiment_texts)

test = Text("I'm a bit allergic to these flowers !", classifier=bayes)

print(test, test.classify())