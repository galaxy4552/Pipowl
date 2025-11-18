import numpy as np
from typing import List, Tuple, Optional

from pipowl.semantic import SemanticOwl
from pipowl.light import LightOwl


class LangOwl:
    """
    LangOwl-open 版本（可公開）
    - 使用 SemanticOwl encode
    - 使用 LightOwl 清洗（可關閉）
    - 閹割版 GLUE（單純穩定向量，不洩漏私有邏輯）
    - 基礎 top-k 搜尋
    """

    def __init__(
        self,
        use_clean: bool = True,
        top_k_default: int = 5,
    ):
        self.semantic = SemanticOwl()
        self.light = LightOwl()
        self.use_clean = use_clean
        self.top_k_default = top_k_default

    # -----------------------------------------------------
    # 閹割版 GLUE：只做 normalize + 1% anchor
    # -----------------------------------------------------
    def glue(self, vec):
        return vec  # 不做 normalize
        """
        對語義向量做輕微穩定化。
        閹割版（無個人語氣、無個性向量）
        """

    # -----------------------------------------------------
    # encode + glue
    # -----------------------------------------------------
    def encode(self, text: str) -> np.ndarray:
        if self.use_clean:
            text = self.light.clean_text(text)
        vec = self.semantic.encode(text)
        return self.glue(vec)

    # -----------------------------------------------------
    # top-k（本質：語意搜尋 with glue）
    # -----------------------------------------------------
    def topk(self, query_text: str, corpus: List[str], k: Optional[int] = None):
        k = k or self.top_k_default

        if corpus is None or len(corpus) == 0:
            return []

        # ---------- 原有流程 ----------
        q_vec = self.encode(query_text)

        corpus_vecs = [self.encode(c) for c in corpus]

        if len(corpus_vecs) == 0:
            return []

        corpus_vecs = np.asarray(corpus_vecs, dtype=np.float32)
        q = q_vec / (np.linalg.norm(q_vec) + 1e-9)

        scores = corpus_vecs @ q
        if len(scores) == 0:
            return []

        idx = np.argsort(scores)[::-1][:k]

        return [(corpus[i], float(scores[i])) for i in idx]

