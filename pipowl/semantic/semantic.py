import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Tuple


class SemanticOwl:
    """
    SemanticOwl-open 版本（可公開）
    - 基本語義向量編碼
    - cosine similarity
    - top-k search
    """

    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = None

    def _load(self):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(self.model_name)
        
    # -----------------------------------------------------
    # 基本功能：encode
    # -----------------------------------------------------
    def encode(self, text):
        if self.model is None:
            self._load()
        return self.model.encode(text)
    
    # -----------------------------------------------------
    # similarity
    # -----------------------------------------------------
    def similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """計算 cos 相似度"""
        v1 = vec1 / (np.linalg.norm(vec1) + 1e-9)
        v2 = vec2 / (np.linalg.norm(vec2) + 1e-9)
        return float(np.dot(v1, v2))

    # -----------------------------------------------------
    # search（top-k）
    # -----------------------------------------------------
    def search(self, query_vec: np.ndarray, corpus: List[str], top_k: int = 5) -> List[Tuple[str, float]]:
        """
        給 query_vec，在 corpus 裡找到 top-k 最接近的句子
        回傳 [(句子, 相似度), ...]
        """
        corpus_vecs = self.model.encode(corpus)
        corpus_vecs = np.asarray(corpus_vecs, dtype=np.float32)

        # normalize query
        q = query_vec / (np.linalg.norm(query_vec) + 1e-9)

        # similarity
        scores = corpus_vecs @ q

        # 取得 top-k
        idx = np.argsort(scores)[::-1][:top_k]

        return [(corpus[i], float(scores[i])) for i in idx]
