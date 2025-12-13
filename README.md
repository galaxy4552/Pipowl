# pipowl 🦉  
Open Semantic Tools for Python

[![PyPI version](https://img.shields.io/pypi/v/pipowl.svg)](https://pypi.org/project/pipowl/)
![License](https://img.shields.io/pypi/l/pipowl.svg)
[![Downloads](https://static.pepy.tech/badge/pipowl)](https://pepy.tech/project/pipowl)

v1.4.8 SemanticOwl + LightOwl + LangOwl Open-Core (10KB)
v1.5.0 StateOwl open-core (14KB)
v1.5.1 Enhanced CLI interface (48KB)

No change to core semantic behavior

---

## pipowl 提供：

### **SemanticOwl**
輕量語意編碼器（使用 SentenceTransformer）

### **LightOwl**
文本清洗工具

### **LangOwl**
語意搜尋（top-k + cosine similarity）

### **StateOwl**
簡易狀態表示

---

## 安裝

```bash
pip install pipowl
使用方式
① 叫出 LangOwl（像叫一隻貓頭鷹出來）
python

from pipowl.lang import LangOwl

lang = LangOwl()
② 準備一些要比對的句子清單
python

corpus = [
    "我今天真的好累",
    "我覺得今天狀態不太好",
    "今天的天氣真的很好",
]
③ 丟一句話進去，看哪句最像
python

results = lang.topk("我今天真的很想睡覺，因為工作太累了", corpus)
④ 印出結果（分數＋句子）
python

for text, score in results:
    print(score, text)
    
總結

pipowl 是一個用來「比較句子語意相似度」的小工具。

你只要給它兩個東西：

你的句子（要查的）

你的一組句子（要比的）

它就會告訴你「哪一句最像」。

輸出示例
0.903 我今天真的好累
0.882 我覺得今天狀態不太好
0.834 今天的天氣真的很好

快速試用（Quickstart）
py -m quickstart

quickstart.py
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

minimal.py
from pipowl.lang import LangOwl

lang = LangOwl()
results = lang.topk("我很累", ["我好累", "我想吃飯"])
print(results)

```bash