from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Kkma, Okt
import numpy as np
import nltk, re

eng_words = set()
kor_words = set()

# 리스트 설정
def wording():
    with open(r"words\ko_word.txt", 'r', encoding='UTF-8') as f:
        kor_words.update(line.strip() for line in f)

    with open(r"words\eng_word.txt", 'r', encoding='UTF-8') as f:
        eng_words.update(line.strip() for line in f)

# 문장 정규화
def regular(text):
    pattern = re.compile(r'\[\d*\]')
    return re.sub(pattern, '', text)

# 문장 짧은 것들 통합
def integrated(language, original):
    sentences = []

    if language == 'en':
        token = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = token.tokenize(original)
    elif language == 'ko':
        sentences = Kkma().sentences(original)

    for i in range(len(sentences)):
        if len(sentences[i]) <= 10:
            sentences[i-1] += (' ' + sentences[i])
            sentences[i] = ''

    return [sentence for sentence in sentences if sentence]

# 통합된 문장 명사화
def nounization(language, integrated_sentences):
    noun_sentences = []

    if language == 'en':
        stop_words = eng_words
        st = nltk.stem.SnowballStemmer('english')
        n1 = [w for w in integrated_sentences if w not in stop_words]
        noun_sentences = [sentence for sentence in n1 if sentence]
    elif language == 'ko':
        stop_words = kor_words
        okt = Okt()
        for sentence in integrated_sentences:
            nouns = okt.nouns(sentence)
            filtered_nouns = [n for n in nouns if n not in stop_words and len(n) > 1]
            noun_sentences.append(' '.join(filtered_nouns))

    return noun_sentences

# 그래프는 랭킹 부여할 기반 그래프, point는 비율
def ranking(graph, point):
    A = graph.copy()
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

# 메인 코드
def summarize_sentence(language, original, point, number):
    wording()

    original = regular(original)
    integrated_text = integrated(language, original)
    noun_text = nounization(language, integrated_text)

    try:
        T_matrix = TfidfVectorizer().fit_transform(noun_text).toarray()
        graph_text = np.dot(T_matrix, T_matrix.T)
    except:
        return '004'

    ranked_text = ranking(graph_text, point)
    sorted_rank = sorted(ranked_text, key=lambda k: ranked_text[k], reverse=True)

    summary = [integrated_text[i] for i in sorted_rank[:number]]
    

    return '\n'.join(summary)
