from helper import remove_punc
import math
import hw8_1
import nltk
import nltk.tokenize as tk
import numpy as np
nltk.download("punkt")
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
#Clean and prepare the contents of a document
#Takes in a file name to read in and clean
#Return a single string, without stopwords, spaces, and punctuation
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def read_and_clean_doc(doc) :
    #1. Open document, read text into *single* string
    f = open(doc)
    data = f.read()
    f.close()
    #2. Filter out punctuation from list of words (use remove_punc)
    data = remove_punc(data)
    #3. Make the words lower case
    data = data.lower()
    data = tk.word_tokenize(data)
    #4. Filter out stopwords
    stop = set(stopwords.words('english'))
    all_no_stop = [n for n in data if not n in stop]
    #5. Remove remaining whitespace
    all_no_stop = "".join(all_no_stop)
    return all_no_stop
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames* and a number *n* corresponding to the length of each ngram
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per ngram (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the list of ngrams output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of ngrams that should correspond to the columns in
#docword
def build_doc_word_matrix(doclist, n) :

    #1. Create the cleaned string for each doc (use read_and_clean_doc)
    ngram_set = set()
    ngramlist = []
    ngramlist_doc = []
    freqlist_doc = []
    i = 0
    for doc in doclist:
        clean_string = read_and_clean_doc(doc)
        ngram_temp_set = set()
        freq = dict()
    #2. Create and use ngram lists to build the doc word matrix
        ngrams = hw8_1.get_ngrams(clean_string, n)
        for ngram in ngrams:
            if not ngram in ngram_set: ngramlist.append(ngram)
            ngram_set.add(ngram)
            ngram_temp_set.add(ngram)
            if ngram in freq: freq[ngram] += 1
            else: freq[ngram] = 1
        ngramlist_doc.append(ngram_temp_set)
        freqlist_doc.append(freq)
    docword = np.ndarray((len(doclist), len(ngramlist)))
    ngramlist = sorted(ngramlist)
    for i, doc in enumerate(doclist):
        row = []
        for ngram in ngramlist:
            lookup = freqlist_doc[i]
            if ngram in ngramlist_doc[i]: row.append(lookup[ngram])
            else: row.append(0)
        docword[i] = row
    return docword, ngramlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def build_tf_matrix(docword) :
    
    #fill in
    rows = docword.shape[0]
    cols = docword.shape[1]
    rowSum = np.sum(docword, axis=1)
    tf = np.ndarray((rows, cols))
    for r in range(rows):
        ls = []
        for c in range(cols):
            item = docword.item(r,c)
            ls.append(item / rowSum[r])
        tf[r] = ls
    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of ngrams in the doc word matrix)
#Don't forget the log factor!
def build_idf_matrix(docword) :
    
    #fill in
    idf = []
    rows = docword.shape[0]
    cols = docword.shape[1]
    for c in range(cols):
        count = 0
        for r in range(rows):
            if docword[r][c] != 0: count += 1
        idf_temp = math.log10(rows / count)
        idf.append(idf_temp)
    idf = np.array(idf)
    idf = idf.reshape(1, len(idf))
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def build_tfidf_matrix(docword) :
    
    #fill in
    rows = docword.shape[0]
    cols = docword.shape[1]
    tf = build_tf_matrix(docword)
    idf = build_idf_matrix(docword)
    tfidf = np.ndarray((rows, cols))
    for r in range(rows):
        ls = []
        for c in range(cols):
            tf_temp = tf[r][c]
            idf_temp = idf[0][c]
            ls.append(tf_temp * idf_temp)
        tfidf[r] = ls
    return tfidf
    
#Find the three most distinctive ngrams, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most unique ngrams in each document
def find_distinctive_ngrams(docword, ngramlist, doclist) :
    distinctive_words = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    tfidf = build_tfidf_matrix(docword)
    sorted = np.argsort(-tfidf, axis=1)
    for i, filename in enumerate(doclist):
        ls = [ngramlist[sorted[i][0]], ngramlist[sorted[i][1]], ngramlist[sorted[i][2]]]
        distinctive_words[filename] = ls
    return distinctive_words


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    #Some main code:
    '''directory='lecs'
    path = join(directory, '1_vidText.txt')
    read_and_clean_doc(path)
    #build document list
    
    path='lecs'
    file_list = [f for f in listdir(path) if isfile(join(path, f))]
    path_list = [join(path, f) for f in file_list]
    
    mat,wlist=build_doc_word_matrix(path_list)
    
    tfmat = build_tf_matrix(mat)
    idfmat = build_idf_matrix(mat)
    tfidf = build_tfidf_matrix(mat)
    results = find_distinctive_words(mat,wlist,file_list)'''
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    
    print("*** Testing read_and_clean_doc ***")
    print(read_and_clean_doc(path1)[0:20])
    print("*** Testing build_doc_word_matrix ***") 
    doclist =[path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist, 3)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing build_tf_matrix ***") 
    tf = build_tf_matrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing build_idf_matrix ***") 
    idf = build_idf_matrix(docword)
    print(idf[0][0:10])
    print("*** Testing build_tfidf_matrix ***") 
    tfidf = build_tfidf_matrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing find_distinctive_words ***")
    print(find_distinctive_ngrams(docword, wordlist, doclist))
