# pipowl/state/state.py

class StateOwl:
    """Minimal language-state analyzer for pipowl 1.50."""

    def __init__(self):
        pass

    # --------------------------
    # Public API
    # --------------------------
    def analyze(self, text: str) -> dict:
        """Analyze text intent, tone, emotion.

        Parameters
        ----------
        text : str
            Input sentence.

        Returns
        -------
        dict
            {
              "intent": str,
              "tone": str,
              "emotion": str
            }
        """
        intent = self._infer_intent(text)
        tone = self._infer_tone(text)
        emotion = self._infer_emotion(text)

        return {
            "intent": intent,
            "tone": tone,
            "emotion": emotion
        }

    # --------------------------
    # Internal inference rules
    # --------------------------
    def _infer_intent(self, text: str) -> str:
        t = text.strip()

        # 問句
        if t.endswith("?") or "嗎" in t or "?" in t:
            return "ask"

        # 指令
        command_patterns = ["幫我", "請", "麻煩", "幫忙", "給我", "查一下", "幫查"]
        if any(p in t for p in command_patterns):
            return "command"

        # 情緒型
        emotion_keywords = ["我受不了", "我不行了", "我快哭了", "我好痛", "崩潰"]
        if any(e in t for e in emotion_keywords):
            return "emotion"

        # 敘述描述
        return "describe"

    def _infer_tone(self, text: str) -> str:
        # 強語氣
        strong_patterns = ["!", "快點", "拜託快", "你到底", "為什麼"]
        if any(p in text for p in strong_patterns):
            return "strong"

        # 柔語氣
        soft_patterns = ["...", "有點", "有些", "有一點"]
        if any(p in text for p in soft_patterns):
            return "soft"

        return "neutral"

    def _infer_emotion(self, text: str) -> str:
        positive = ["開心", "爽", "喜歡", "太好了", "幸福"]
        negative = ["累", "難過", "討厭", "生氣", "痛", "煩"]

        if any(p in text for p in positive):
            return "positive"
        if any(n in text for n in negative):
            return "negative"

        return "none"
