from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
import re, gc, sys, os
import numpy as np
from nltk import word_tokenize


eng_words = set()
kor_words = set()

def pkg_exist():
    try:
        import konlpy, re, numpy, sklearn
    except:
        return False
    else:
        return True

def resource_path(relative_path): #add-data에 사용 - ./words경로
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

# 리스트 설정
def wording(language):
    if(language == 'ko'):
        with open(resource_path(r"words\ko_word.txt"), 'r', encoding='UTF-8') as f:
            kor_words.update(line.strip() for line in f)
        # with open(resource_path(r"words\ko_word.txt"), 'r', encoding='UTF-8') as f:
        #     kor_words.update(line.strip() for line in f)
    elif(language == 'en'):
        with open(resource_path(r"words\eng_word.txt"), 'r', encoding='UTF-8') as f:
            eng_words.update(line.strip() for line in f)
        # with open(resource_path(r"words\eng_word.txt"), 'r', encoding='UTF-8') as f:
        #     eng_words.update(line.strip() for line in f)


def split_sentence(text):
    #문장 분리 -> 리스트 형태로
    #부가 설명등 괄호,기호 제거
    sent1 = re.split(r'[\n.?!]', text)
    sent2 = [re.sub(r'\([^()]*\)|\[\d+\]', '', t) for t in sent1]
    sent3 = [s.strip() for s in sent2 if s.strip()]
    return sent3

def Eng(original_text,point = 0.85,num = 2):
    #문장 분리
    cleaned_text = split_sentence(original_text)
    lower_text = [s.lower() for s in cleaned_text]
    
    #불용어 및 문장부호 제거
    clean_text = []
    for sentence in lower_text:
        if(sentence == "" or len(sentence) == 0):
            continue
        tokens = sentence.split()
        tokens = [token for token in tokens if token not in eng_words]
        clean_sentence = ' '.join(tokens)
        clean_sentence = re.sub(r"[.,?!]", " ", clean_sentence)
        clean_text.append(clean_sentence)

    #토큰화
    tokenized_text = [word_tokenize(s,language="english") for s in clean_text]
    
    #다시 문장 구성
    preprocessed_text = [' '.join(tokens) for tokens in tokenized_text]
    
    try:
        T_matrix = TfidfVectorizer().fit_transform(preprocessed_text).toarray()
        graph_text = np.dot(T_matrix, T_matrix.T)
    except:
        result = '002'
        gc.collect()
        return result

    ranked_text = ranking(graph_text, point) #포인트
    sorted_rank = sorted(ranked_text, key=lambda k: ranked_text[k], reverse=True)

    del graph_text
    del T_matrix

    summary = [cleaned_text[i] for i in sorted_rank[:num]]
    summary = [s + '.' for s in summary]
    del ranked_text
    del sorted_rank
    
    result = '\n'.join(summary)
    gc.collect()
    return result

def Kor(original_text,point = 0.85,num = 2):
    okt = Okt()

    cleaned_text = split_sentence(original_text)
    
    preprocessed_text = []
    for sentence in cleaned_text:
        if(sentence == "" or len(sentence) == 0):
            continue
        nouns = okt.nouns(sentence)
        filtered_text = [noun for noun in nouns if noun not in kor_words]
        preprocessed_text.append(' '.join(filtered_text))
    
    #벡터화
    try:
        T_matrix = TfidfVectorizer().fit_transform(preprocessed_text).toarray()
        graph_text = np.dot(T_matrix, T_matrix.T)
    except:
        result = '002'
        gc.collect()
        return result

    ranked_text = ranking(graph_text, point) #포인트
    sorted_rank = sorted(ranked_text, key=lambda k: ranked_text[k], reverse=True)

    del graph_text
    del T_matrix

    summary = [cleaned_text[i] for i in sorted_rank[:num]]

    del ranked_text
    del sorted_rank

    summary = [s + '.' for s in summary]
    result = '\n'.join(summary)
    gc.collect()
    return result

#문장 순위 정리
def ranking(graph, point):
    A = graph
    d = point
    np.fill_diagonal(A, 0)

    l_sum = np.sum(A, axis=0)
    l_sum[l_sum != 0] = 1 / l_sum[l_sum != 0]
    A = np.multiply(A, l_sum)
    A *= -d
    np.fill_diagonal(A, 1)

    B = (1 - d) * np.ones((A.shape[0], 1))
    ranks = np.linalg.solve(A, B)

    return {idx: r[0] for idx, r in enumerate(ranks)}

def summarize(language, original_text, point, number):
    pkg = pkg_exist()
    if(pkg == False):
        return '001'
    else:
        wording(language)
        if(language == 'ko'):
            return Kor(original_text,point,number)
        elif(language == 'en'):
            return Eng(original_text,point,number)
        else:
            return '004'

if __name__ == '__main__':

    sentence = """"""
    sentence2 = """"""
    sentence3 = """"""
    answer = summarize('ko',sentence3,0.85,5)

    print(answer)
