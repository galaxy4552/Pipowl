import numpy as np
from typing import List, Tuple, Optional

from pipowl.semantic import SemanticOwl


class LangOwl:
    """
    LangOwl-open
    SemanticOwl
    - 純語義 top-k
    """

    def __init__(
        self,
        top_k_default: int = 5,
    ):
        self.semantic = SemanticOwl()
        self.top_k_default = top_k_default

    # -----------------------------------------------------
    # encode
    # -----------------------------------------------------
    def encode(self, text: str) -> np.ndarray:
        return self.semantic.encode(text)

    # -----------------------------------------------------
    # top-k semantic search
    # -----------------------------------------------------
    def topk(
        self,
        query_text: str,
        corpus: List[str],
        k: Optional[int] = None
    ) -> List[Tuple[str, float]]:
        k = k or self.top_k_default

        if not corpus:
            return []

        q_vec = self.encode(query_text)
        corpus_vecs = [self.encode(c) for c in corpus]

        corpus_vecs = np.asarray(corpus_vecs, dtype=np.float32)
        q = q_vec / (np.linalg.norm(q_vec) + 1e-9)

        scores = corpus_vecs @ q
        idx = np.argsort(scores)[::-1][:k]

        return [(corpus[i], float(scores[i])) for i in idx]

