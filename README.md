# pipowl 🦉  
Open Semantic Tools for Python

[![PyPI version](https://img.shields.io/pypi/v/pipowl.svg)](https://pypi.org/project/pipowl/)
![License](https://img.shields.io/pypi/l/pipowl.svg)
[![Downloads](https://static.pepy.tech/badge/pipowl)](https://pepy.tech/project/pipowl)

pipowl: 目標：快速、穩定的 embedding 相似度工具

v1.6.0
---

## pipowl 提供：

### **SemanticOwl**
輕量語意編碼器（使用 SentenceTransformer）

### **LangOwl**
語意搜尋（top-k + cosine similarity）

---

## 安裝

```bash
pip install pipowl
```

## 使用方式

```bash
① 叫出 LangOwl（像叫一隻貓頭鷹出來）

from pipowl.lang import LangOwl

lang = LangOwl()
② 準備一些要比對的句子清單

corpus = [
    "我今天真的好累",
    "我覺得今天狀態不太好",
    "今天的天氣真的很好",
]
③ 丟一句話進去，看哪句最像

results = lang.topk("我今天真的很想睡覺，因為工作太累了", corpus)
④ 印出結果（分數＋句子）

for text, score in results:
    print(score, text)    
```

## 總結

```bash
pipowl 是一個用來「比較句子語意相似度」的小工具。

你只要給它兩個東西：

你的句子（要查的）

你的一組句子（要比的）

它就會告訴你「哪一句最像」。
```

## 輸出示例

```bash
0.903 我今天真的好累
0.882 我覺得今天狀態不太好
0.834 今天的天氣真的很好
```

## 快速試用（Quickstart）

### quickstart.py
- py -m quickstart

```bash
from pipowl.lang import LangOwl

# 叫出語意偵探 LangOwl
lang = LangOwl()

# 準備一組你想比較的句子清單
corpus = [
    "我今天真的好累",
    "我覺得今天狀態不太好",
    "今天的天氣真的很好",
]

# 互動式輸入
while True:
    query = input("請輸入句子： ")

    results = lang.topk(query, corpus)

    print("\n相似結果：")
    for text, score in results:
        print(f"{score:.3f} | {text}")
    print()
```

### minimal.py

```bash
from pipowl.lang import LangOwl

lang = LangOwl()
results = lang.topk("我很累", ["我好累", "我想吃飯"])
print(results)

```