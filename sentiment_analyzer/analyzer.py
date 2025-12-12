from transformers import pipeline


class StudentTextSentimentAnalyzer:
    """
    Analyze sentiment of student-related texts
    such as feedback, lecture reviews, meeting notes.
    """

    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis")

    def analyze(self, text: str) -> dict:
        if not text or not text.strip():
            return {"label": "EMPTY", "score": 0.0}

        result = self.analyzer(text, truncation=True)[0]
        return {
            "label": result["label"],
            "score": float(result["score"])
        }