# SC1015 Mini-Project - Ethereum Price Prediction:

Lab FDDA, Group 10

### Members

 Werner Soon Shi Xu (U2320610D),
 Ramanujam Mohanraj Nivetha (U2323405J),
 Wang Min-Jen (U2320226D)

### Instructor 

Course Instructor: Dr Smitha K G (Co-Ord) and Mr. Ong Chin Ann
Teaching Assistant: Kuzmin Nikita

### PROBLEM DEFINITION:

 How can we create an algorithmic trading bot that uses historical data to predict future Ethereum price movements?

 ### STEPS:
1. Find correlation between price of Ethereum and something related to Ethereum
   This is so that we can use the value of that factor related to predict the price of Ethereum
2. Plot the linear regression to estimate the future price of Ethereum
3. Use classification table to determine whether to purchase Ethereum based of historical data
4. Use Gradiant Boosted Model

### DATASETS USED:

Used "Ethereum Historical Data" from Kaggle with the following datasets:
1. Bitcoin Prices 
2. Fear & Greed index of Bitcoin/Cryptocurrency 
3. AMD/NVDA Stock Prices (From Yahoo Finance)
4. Created our own data set from news section in Ethereum category of investing.com - Ethereum Sentiment Data

### WHAT WE LEARNT:
- Vader Sentiment Analysis
- Web Scraping
- Gradient Boosted Model

### OUTCOME:

We have managed to produce a predictor of Ethereum price based on historical data as well as a tool to decide if we should purchase or sell Ethereum depending on the change in Bitcoin price the previous day.

### INSIGHTS:


- Ethereum is closely linked to Bitcoin and the GPU industry

- Do not trade based off the Fear & Greed Index of Crypto, it is not a good predictor of future data

- Avoid relying on investing.com news for Ethereum predictions due to its limited predictive value.  Exercise caution when using VADER for financial news sentiment analysis, as it may not be reliable.

### REFERENCES:

https://www.kaggle.com/datasets/kapturovalexander/bitcoin-and-ethereum-prices-from-start-to-2023
https://finance.yahoo.com/quote/NVDA/history/
https://finance.yahoo.com/quote/AMD/history/
https://finance.yahoo.com/quote/ETH-USD/history/
https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html
https://www.investing.com/crypto/ethereum/news






