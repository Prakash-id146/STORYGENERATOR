# this is our story generator project and try to explain in comments
# in each step why we use this command 
# here is two thing is needed one is install to python package 
#  or libraries nltk , spacy , gensim 
# and another to download is python datasets that is punkit,stopwords
import nltk 
# here we install one libraries nltk
from nltk.corpus import stopwords

# nltk.corpus: This module provides access to 
# various text corpora. For example, it includes a collection o
# f stopwords, which are common words that are usually filtered
# out before processing text (e.g., "and", "the", "is").

# stopwords: The stopwords module in nltk contains a list of 
# common words in various languages that are often removed 
# from text to focus on more meaningful words.

from nltk.tokenize import word_tokenize, sent_tokenize
# word_tokenize and sent_tokenize:
#     These functions are used to break down text into words
#     (word tokenization) and sentences (sentence tokenization).
from collections import Counter
# collections: This module provides specialized container datatypes.
# One of the commonly used classes is Counter,
# which is used to count the occurrences of 
# elements in a collection (like a list).
# Sample long story (you can replace this with your own story)
story = """
 the story about paramaatama RAJIV DIXIT JI  WHO IS REAL DEVOTE OF INDIA 
 HE IS THE PERSON WHO WANTS TO MAKE DEASESLESS AND ANCIENT RAMARAJYA INDIA BUT HE DIES AT 45 AGE IN HEART ATTACK 
 BUT IN REALY IT IS A PLAN TO MURDER TO HIM  NOW I WANTS TO TELL ABOUT HIS LIFE ANDSTORY 
 
 SUMMERY 
 Rajiv Dixit was an influential Indian social activist known for his passionate advocacy of Swadeshi (self-reliance) 
 and his opposition to globalization and neoliberalism. Born on November 30, 1967, in Nah, 
 Uttar Pradesh, he founded the Azadi Bachao Andolan (Save Independence Movement) in 1992, 
 aiming to counter the influence of foreign multinationals and Western culture on India.

Dixit was deeply inspired by the Bhopal disaster of 1984, which led him to question the
role of multinational corporations in India. His activism was shaped by Gandhian historian Dharampal.
He delivered thousands of speeches across India, spreading his message through recordings on CDs and tapes1.

In 2004, Dixit collaborated with yoga guru Ramdev to form the Bharat Swabhiman Andolan,
which combined economic self-reliance with the promotion of yoga and Ayurveda. 
The movement had political ambitions, and they launched the Bharat Swabhiman party in 2010, 
aiming to contest the 2014 Indian general election1.

Rajiv Dixit passed away on November 30, 2010,
under controversial circumstances during a campaign tour in Chhattisgarh. His death marked
the end of the Bharat Swabhiman party's political aspirations1.
NOW IS THE TIME TO MAKE A COMMITEMENT TO CHANGE OUR SOCITE AND 
REMOVE CORROPTION AND NEPOTISM IN EVERY FIELD 
IF ALL INDIA AND WORLD PEOPLE COMMITE TOGATHER MAKE RAMA RAJYA

RAM RAM RAM

"""

# Tokenize the story into words
words = word_tokenize(story.lower())

# Remove stopwords and punctuation
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

# Get the frequency distribution of words
word_freq = Counter(filtered_words)
# Get the most common words (key insights)
most_common_words = word_freq.most_common(10)  # Top 10 words

# Print the key insights
print("Key Insights (Most Common Words):")
for word, freq in most_common_words:
    print(f"{word}: {freq}")

# Tokenize the story into sentences
sentences = sent_tokenize(story)

# Print the first 5 sentences as part of the summary
print("\nStory Summary (First 20Sentences):")
for sentence in sentences[:20]:
    print(sentence)
