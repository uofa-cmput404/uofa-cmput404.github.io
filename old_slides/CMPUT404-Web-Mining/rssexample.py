import feedparser
import difflib
import json
cbc = feedparser.parse("http://rss.cbc.ca/lineup/topstories.xml")
#print(json.dumps(cbc))
print("\n\n################################################\n\n")
cnn = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")
#print(json.dumps(cnn))
print("\n\n################################################\n\n")
cbc_titles = [x['title'] for x in cbc.get('entries')]
cnn_titles = [x['title'] for x in cnn.get('entries')]
res = [(x,difflib.get_close_matches(x,cbc_titles,1,0.01)) for x in
            cnn_titles]
print(json.dumps(res))

from nltk.tokenize import wordpunct_tokenize as tokenize
from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))
def jaccard(set1, set2):
    iset = set1.intersection(set2)
    #return len(iset)
    return len(iset) / float(len(set1) + len(set2) - len(iset))
    
def string_jaccard(str1, str2):
    s1 = set(tokenize(str1.lower())).difference(stopset)
    s2 = set(tokenize(str2.lower())).difference(stopset)
    return jaccard(s1,s2)
    
def rankSimilar(title, titles):
    jtitles = [(string_jaccard(title,t), t) for t in titles]
    jtitles.sort(reverse=True)
    return jtitles
        
jres = [(x,rankSimilar(x,cbc_titles)[0]) for x in
            cnn_titles]


from gensim.test.utils import common_corpus, common_dictionary
from gensim.similarities import MatrixSimilarity
import gensim
import gensim.parsing.preprocessing
from gensim.corpora import Dictionary
import gensim.models.tfidfmodel
from gensim.test.utils import get_tmpfile
from gensim.matutils import sparse2full, unitvec
from gensim.models.ldamodel import LdaModel




stripped_documents = [gensim.parsing.preprocessing.preprocess_string(document) for document in cbc_titles + cnn_titles]
words = Dictionary(stripped_documents)
corpus = [words.doc2bow(doc) for doc in stripped_documents]
tfidf = gensim.models.tfidfmodel.TfidfModel(corpus)
tfidfcorp = [tfidf[doc] for doc in corpus]
index = gensim.similarities.docsim.MatrixSimilarity(tfidfcorp)
def doc2query(doc):
    prep = gensim.parsing.preprocessing.preprocess_string(doc)
    bow = words.doc2bow(prep)
    q = tfidf[bow]
    return q
    
index[doc2query(cbc_titles[0])]
