from pipowl.semantic import SemanticOwl
from pipowl.light import LightOwl

sem = SemanticOwl()
light = LightOwl()

query = "我想睡覺"

# 清洗（可選）
q_clean = light.clean_text(query)
q_vec = sem.encode(q_clean)

corpus = [
    "我好累",
    "今天想休息",
    "飛行太久了",
    "我是雪鴞",
    "我想吃東西"
]

results = sem.search(q_vec, corpus, top_k=3)

print("Query:", q_clean)
print("Results:")
for text, score in results:
    print(f"{score:.3f} | {text}")
