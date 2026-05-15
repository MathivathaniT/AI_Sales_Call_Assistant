
from textblob import TextBlob

def analyze_call(text):
    blob = TextBlob(text)

    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    summary = text[:250] + "..." if len(text) > 250 else text

    suggestions = []

    if "price" in text.lower():
        suggestions.append("Explain the product value and ROI clearly.")

    if "not interested" in text.lower():
        suggestions.append("Offer a limited-time demo or discount.")

    if "features" in text.lower():
        suggestions.append("Highlight advanced product features.")

    if not suggestions:
        suggestions.append("Maintain engagement and ask follow-up questions.")

    return {
        "summary": summary,
        "sentiment": sentiment,
        "suggestions": suggestions
    }
