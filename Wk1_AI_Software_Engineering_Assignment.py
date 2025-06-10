# ===== CRYPTOCURRENCY ADVISOR CHATBOT =====
# A rule-based bot that recommends cryptos based on profitability & sustainability.

# ---- 1. Predefined Crypto Data ----
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# ---- 2. Helper Functions ----
def get_most_profitable():
    """Returns the crypto with the best profitability metrics."""
    profitable_coins = [
        name for name, data in crypto_db.items()
        if data["price_trend"] == "rising" and data["market_cap"] == "high"
    ]
    return profitable_coins[0] if profitable_coins else None

def get_most_sustainable():
    """Returns the crypto with the best sustainability score."""
    return max(crypto_db.items(), key=lambda x: x[1]["sustainability_score"])[0]

# ---- 3. Chatbot Logic ----
def respond_to_query(user_query):
    """Processes user input and returns a recommendation."""
    user_query = user_query.lower()
    
    if "profit" in user_query or "grow" in user_query:
        coin = get_most_profitable()
        if coin:
            return f"🚀 For growth, consider {coin}! It's trending up with strong market demand."
        else:
            return "📉 No highly profitable coins match criteria right now."
    
    elif "sustain" in user_query or "green" in user_query:
        coin = get_most_sustainable()
        return f"🌱 For sustainability, {coin} is the best choice (Score: {crypto_db[coin]['sustainability_score']}/10)."
    
    elif "trend" in user_query:
        trending_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 Trending coins: {', '.join(trending_coins)}."
    
    else:
        return "🤖 I can advise on profitability or sustainability. Try asking: 'Which crypto is best for growth?'"

# ---- 4. Main Interaction Loop ----
print("💎 CryptoExpert: Hi! Ask me which crypto to invest in (profit/sustainability).")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("💎 CryptoExpert: Happy investing! Remember: Do your own research. 🚨")
        break
    response = respond_to_query(user_input)
    print(f"CryptoExpert: {response}")
