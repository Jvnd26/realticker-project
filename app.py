from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy stock data
stocks = [
    {"ticker": "AAPL", "company": "Apple", "price": 185, "change": 1.2, "volume": "78M"},
    {"ticker": "MSFT", "company": "Microsoft", "price": 412, "change": 0.8, "volume": "45M"},
    {"ticker": "GOOG", "company": "Google", "price": 135, "change": -0.5, "volume": "30M"}
]

@app.route('/api/stocks/top10')
def get_stocks():
    return jsonify(stocks)

@app.route('/api/stocks/<ticker>')
def get_stock(ticker):
    for stock in stocks:
        if stock["ticker"] == ticker:
            # Fake AI analysis
            if stock["change"] > 0:
                trend = "Upward"
            else:
                trend = "Downward"

            return jsonify({
                "stock": stock,
                "analysis": {
                    "trend": trend,
                    "risk": "Medium",
                    "suggestion": "Long-term investment"
                }
            })
    return jsonify({"error": "Not found"})

if __name__ == '__main__':
    app.run(debug=True)