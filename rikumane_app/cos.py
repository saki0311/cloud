# coding: UTF-8
import MeCab
from collections import Counter

def cos(text,company_text):
    # text = "所属するテニスサークルで、学園祭模擬店出店を発案企画し、責任者として取り組んだ。退部者が多いという問題に対して、全員が共通の目標に向かって長期間活動する経験によって、組織に愛着を持ち活動を継続すると考えたことが動機である。練習機会の減少や財政難を理由に反対する部員もいたが、強豪サークルの代表や過去の学園祭出店経験者に実際に話を聞き、報告書にまとめることで部員の懸念事項を解決し、出店へと至った。また出店の際に３つの部門を設け、部員がどれか１つの部門に所属する仕組みを構築することで、全員が当事者意識を持てるようにした。結果、出店を成功させるだけでなく、前年比約２５％退部者を減らすことができた。"
    # company_text = "私は犬です。所属しているサークルはテニスです。"
    text = text
    company_text = company_text
    mecab_user = MeCab.Tagger("")
    mecab_company = MeCab.Tagger("")
    node_user = mecab_user.parseToNode(text)
    node_company = mecab_company.parseToNode(company_text)

    #利用者用
    word_list_user = []
    while node_user:
        word_type = node_user.feature.split(',')[0]
        if word_type in ['名詞','形容詞']:
            word_list_user.append(node_user.surface)
        node_user = node_user.next

    #企業用
    word_list_company = []
    while node_company:
        word_type = node_company.feature.split(',')[0]
        if word_type in ['名詞','形容詞']:
            word_list_company.append(node_company.surface)
        node_company = node_company.next

    #利用者の抽出単語頻度計算
    count_user = Counter(word_list_user)

    #企業の抽出単語頻度計算
    count_company = Counter(word_list_company)

    #COS類似度計算結果
    result = calc_cos(count_user,count_company)

    return result

def calc_cos(wordsA,wordsB):
    # 文書Aのベクトル長を計算
    lengthA = sum(wordsA[word] ** 2 for word in wordsA) ** 0.5

    # 文書Bのベクトル長を計算
    lengthB = sum(wordsB[word] ** 2 for word in wordsB) ** 0.5

    # AとBの内積を計算
    dotProduct = sum(wordsA[word] * wordsB[word] for word in wordsA & wordsB)

    # cos類似度を計算
    cos = dotProduct / (lengthA * lengthB)
    return cos

if __name__ == '__main__':
    text = "所属するテニスサークルで、学園祭模擬店出店を発案企画し、責任者として取り組んだ。退部者が多いという問題に対して、全員が共通の目標に向かって長期間活動する経験によって、組織に愛着を持ち活動を継続すると考えたことが動機である。練習機会の減少や財政難を理由に反対する部員もいたが、強豪サークルの代表や過去の学園祭出店経験者に実際に話を聞き、報告書にまとめることで部員の懸念事項を解決し、出店へと至った。また出店の際に３つの部門を設け、部員がどれか１つの部門に所属する仕組みを構築することで、全員が当事者意識を持てるようにした。結果、出店を成功させるだけでなく、前年比約２５％退部者を減らすことができた。"
    company_text = "私は犬です。所属しているサークルはテニスです。"

    print(cos(text,company_text))