import MeCab
import os
import pandas as pd
import matplotlib.pyplot as plt

mecab = MeCab.Tagger()

text = {}
word = {}
wordCount = {}
files = os.listdir('./dataset')
for file in files:
  with open(f"./dataset/{file}", "r") as f:
    print(file)

    # テキスト読み込み
    text[file] = f.read()
    
    # 形態素解析
    word[file] = []
    wTmp = mecab.parse(text[file]).split("\n")
    for wTmp2 in wTmp:
      if wTmp2 == "EOS":
        break
      word[file].append(wTmp2.split("\t"))
    print(f"形態素数: {len(word[file])}")
    
    # 品詞の出現回数
    wordCount[file] = {}
    for wTmp in word[file]:
      if wTmp[0] not in wordCount[file]:
        wordCount[file][wTmp[0]] = 1
      else:
        wordCount[file][wTmp[0]] += 1

    # データフレーム化
    wordCountDf = pd.Series(wordCount[file])
    wordCountDfTop10 = wordCountDf.sort_values(ascending=False).head(10)

    # グラフ化
    plt.figure(figsize=(10,5))
    wordCountDfTop10.plot(kind='bar')
    plt.title('Top 10 words')
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.show()
