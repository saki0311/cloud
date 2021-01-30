# coding: UTF-8
from wordcloud import WordCloud
import MeCab
from matplotlib import pyplot as plt

# ますいが書いた###
import matplotlib
matplotlib.use('Agg')
################

def generate_wc(text):
    text = "所属するテニスサークルで、学園祭模擬店出店を発案企画し、責任者として取り組んだ。退部者が多いという問題に対して、全員が共通の目標に向かって長期間活動する経験によって、組織に愛着を持ち活動を継続すると考えたことが動機である。練習機会の減少や財政難を理由に反対する部員もいたが、強豪サークルの代表や過去の学園祭出店経験者に実際に話を聞き、報告書にまとめることで部員の懸念事項を解決し、出店へと至った。また出店の際に３つの部門を設け、部員がどれか１つの部門に所属する仕組みを構築することで、全員が当事者意識を持てるようにした。結果、出店を成功させるだけでなく、前年比約２５％退部者を減らすことができた。"
    # text = "私は犬です。"
    mecab = MeCab.Tagger("")
    node = mecab.parseToNode(text)
    
    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        if word_type == '名詞' or '形容詞':
            
            word_list.append(node.surface)
        node = node.next

    word_chain = ' '.join(word_list)

    wordcloud = WordCloud(background_color="white",
                            font_path="./static/ttc/03SmartFontUI.ttf",
                            # font_path="/System/Library/Fonts/ヒラギノ明朝 ProN.ttc",
                            # font_path="C:\Windows\Fonts\msgothic.ttc",
                            collocations=False,
                            width=800,height=600).generate(word_chain)


    plt.imshow(wordcloud)
    plt.axis('off')
    #plt.show()

