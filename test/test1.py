from pipowl.semantic import SemanticOwl

sem = SemanticOwl()
vec = sem.encode("我只是隻雪鴞")
print(vec.shape)