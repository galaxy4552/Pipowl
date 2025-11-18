from pipowl.semantic import SemanticOwl
from pipowl.light import LightOwl

# 1. 建立物件
sem = SemanticOwl()
light = LightOwl()

# 2. 清洗文字
raw = "   我   是 隻 雪鴞！！！ 🦉🦉  \n"
cleaned = light.clean_text(raw)
print("Cleaned:", cleaned)

# 3. 向量編碼
vec = sem.encode(cleaned)
print("Vector shape:", vec.shape)
