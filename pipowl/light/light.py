import re
import unicodedata
from typing import List


class LightOwl:
    """
    LightOwl-open 版本（可公開）
    - 輕量文字清洗
    - 適合在送進 SemanticOwl 之前用
    - 不包含任何個人化規則
    """

    def __init__(
        self,
        max_length: int = 500,
        remove_emoji: bool = True,
        squeeze_spaces: bool = True,
    ):
        """
        :param max_length: 單一句子保留的最大長度（太長就捨棄）
        :param remove_emoji: 是否移除 emoji / 非常用符號
        :param squeeze_spaces: 是否把多個空白壓成一個
        """
        self.max_length = max_length
        self.remove_emoji = remove_emoji
        self.squeeze_spaces = squeeze_spaces

    # -----------------------------------------------------
    #  基礎：清洗單一句子
    # -----------------------------------------------------
    def clean_text(self, text: str) -> str:
        """
        清洗單一句子：
        - 去掉前後空白
        - 可選：壓縮空白
        - 可選：移除 emoji / 控制字元
        - 限制最大長度
        """
        if text is None:
            return ""

        # 標準化（避免全形／半形怪異問題）
        text = unicodedata.normalize("NFKC", text)

        # 去掉前後空白
        text = text.strip()

        if self.squeeze_spaces:
            # 把連續空白、tab 變成一個空白
            text = re.sub(r"\s+", " ", text)

        if self.remove_emoji:
            text = self._remove_emoji_like(text)

        # 掉太長的句子（避免爆掉 semantic 模型）
        if len(text) > self.max_length:
            return ""

        return text

    # -----------------------------------------------------
    #  清洗多行文字（例如整個檔案）
    # -----------------------------------------------------
    def clean_lines(self, text: str) -> List[str]:
        """
        把一大段文字切成多行，分別清洗：
        - 依照換行拆開
        - 清洗每一行
        - 移除空行
        """
        if text is None:
            return []

        lines = text.splitlines()
        cleaned = []

        for line in lines:
            c = self.clean_text(line)
            if c:  # 丟掉空字串
                cleaned.append(c)

        return cleaned

    # -----------------------------------------------------
    #  清洗句子列表
    # -----------------------------------------------------
    def clean_corpus(self, sentences: List[str]) -> List[str]:
        """
        清洗一組句子：
        - 適合在做語料前置處理時使用
        """
        if sentences is None:
            return []

        cleaned = []
        for s in sentences:
            c = self.clean_text(s)
            if c:
                cleaned.append(c)
        return cleaned

    # -----------------------------------------------------
    #  內部工具：移除 emoji / 控制字元
    # -----------------------------------------------------
    def _remove_emoji_like(self, text: str) -> str:
        """
        盡量移除 emoji / 各種裝飾符號：
        - 利用 unicode 類別過濾
        這是「安全版本」，不做太激進的刪除。
        """
        cleaned_chars = []
        for ch in text:
            cat = unicodedata.category(ch)
            # C* = control chars
            # So = Symbol, other (emoji 通常在這裡)
            if cat.startswith("C"):
                continue
            if cat == "So":
                continue
            cleaned_chars.append(ch)
        return "".join(cleaned_chars)
