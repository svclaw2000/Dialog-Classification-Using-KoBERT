from konlpy.tag import Komoran

def tokenize(ss):
    komoran = Komoran()
    return [[t[0] for t in komoran.pos(s)] for s in ss]