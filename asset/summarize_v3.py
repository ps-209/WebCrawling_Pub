from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
import re, gc, sys
import numpy as np
from nltk import sent_tokenize

eng_words = set()
kor_words = set()

def pkg_exist():
    try:
        import konlpy, re, numpy, sklearn
    except:
        return False
    else:
        return True
    
# 리스트 설정
def wording(language):
    if(language == 'ko'):
        with open(r"words\ko_word.txt", 'r', encoding='UTF-8') as f:
            kor_words.update(line.strip() for line in f)
    elif(language == 'en'):
        with open(r"words\eng_word.txt", 'r', encoding='UTF-8') as f:
            eng_words.update(line.strip() for line in f)

def Eng(original_text,point = 0.85,num = 2):
    #문장 분리
    text = re.sub(r'\[.*?\]|\(.*?\)', '', original_text)
    separated_text = sent_tokenize(text,'english')
    #소문자
    lower_text = [s.lower() for s in separated_text]
    #불용어 및 문장부호 제거
    clean_text = []
    for sentence in lower_text:
        clean_sentence = re.sub(r'[^\w\s]', '', sentence)
        tokens = clean_sentence.split()
        tokens = [token for token in tokens if token not in eng_words]
        clean_sentence = ' '.join(tokens)
        clean_text.append(clean_sentence)
    #토큰화
    tokenized_text = [re.findall(r'\b\w+\b',sentence) for sentence in clean_text]

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

    summary = [separated_text[i] for i in sorted_rank[:num]]

    del ranked_text
    del sorted_rank
    
    result = '\n'.join(summary)
    gc.collect()
    return result

def Kor(original_text,point = 0.85,num = 2):
    okt = Okt()
    #문장 분리 -> 리스트 형태로
    separated_text = re.split(r'[.!?]+', original_text)
    tokened = [s.strip() for s in separated_text if s.strip()]
    #기호 제거
    cleaned_text = [re.sub(r'\([^()]*\)|\[\d+\]', '', t) for t in tokened]
    
    preprocessed_text = []
    for sentence in cleaned_text:
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

    sentence = "sample"
    sentence2 = """안녕하세요. 오늘은 날이 참 좋네요. 만나서 방가웠습니다. 안녕히가세요."""
    sentence3 = """sample"""
    answer = summarize('ko',sentence2,0.85,2)
    print(answer)
