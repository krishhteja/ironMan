import nltk
from nltk.corpus import wordnet

synonyms = []
antonyms = []

word = "good"

for syn in wordnet.synsets(word):
    main = syn.name()
    w1 = wordnet.synset(main)
    print(w1)
    for lem in syn.lemmas():
        print(lem)
        temp = str(lem)
        mainword = (temp.split('\'')[1])
        required = mainword.split('.')[0] + "." + mainword.split('.')[1] + "."  + mainword.split('.')[2]
        w2 = wordnet.synset(required)
        #print(w2)
        #print(w1.wup_similarity(w2))


####https://www.geeksforgeeks.org/get-synonymsantonyms-nltk-wordnet-python/
