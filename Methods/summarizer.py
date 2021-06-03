from pathlib import Path
from nltk.tokenize import word_tokenize, sent_tokenize
from itertools import chain
import numpy as np

def tokenize(text):
    sentences_tokenized = [word_tokenize(tokenized_sentences) for tokenized_sentences in sent_tokenize(text)]
    words = set(chain.from_iterable(sentences_tokenized))
    word_index = {word: k for k, word in enumerate(words)}
    return sentences_tokenized, word_index


def get_summary(k,sentences_tokenized, word_index):
    num_words = len(word_index)
    num_sents = len(sentences_tokenized)
    
    X = np.zeros((num_words, num_sents))
    
    for d, sent in enumerate(sentences_tokenized):
        for word in sent:
            w = word_index[word]
            X[w, d] += 1
    
    U, S, Vt = np.linalg.svd(X)
    
    important_sents_index = []
    for i in range(len(Vt)):
        sent_index = np.argmax(np.abs(Vt[i, :]))
        if sent_index not in important_sents_index:
            important_sents_index.append(sent_index)
            
    summary = ''
    for sent_index in important_sents_index[:k]:
        summary += ' '.join(sentences_tokenized[sent_index])
        summary+="\n" + "+="*40 +"\n"
    return summary.strip()

def summarize(text,k):
    
    sentences_tokenized, word_index = tokenize(text)
    summary = get_summary(k,sentences_tokenized, word_index)
    
    return summary