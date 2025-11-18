from pipowl.lang import LangOwl

# 叫出語意偵探 LangOwl
lang = LangOwl()

# 準備一組你想比較的句子清單
corpus = [
    "我今天真的好累",
    "我覺得今天狀態不太好",
    "今天的天氣真的很好",
]

print("模型載入完成！你可以開始輸入句子（Ctrl+C 結束）\n")

# 互動式輸入
while True:
    query = input("請輸入句子： ")

    results = lang.topk(query, corpus)

    print("\n相似結果：")
    for text, score in results:
        print(f"{score:.3f} | {text}")
    print()