import nltk

vocab = nltk.corpus.cmudict.dict()

def guttextan(fileid):
    out = [[stresses(w.lower()) for w in sent] for sent in nltk.corpus.gutenberg.sents(fileid)]
    f = open('out-' + fileid, 'w')
    for sent in out:
        f.write(str(sent) + '\n')
    f.close()
def stresses(word):
    try:
        return [int (char) for syll in vocab[word][0] for char in syll if not syll.isdigit() and char.isdigit()]
    except KeyError:
        punct = {
            ',': [3],
            ':': [4],
            ';': [5],
            '.': [6],
            '?': [6],
            '!': [6]
        }
        return punct.get(word, [word])
