# News_Vibes

## Overview

This project is a Stock Sentiment Analysis tool built with Streamlit. It allows users to analyze the sentiment trend of a particular stock based on recent news headlines and visualize the stock's historical performance. The application fetches news articles related to the entered stock name, performs sentiment analysis on the headlines, and displays the sentiment trend over time. Additionally, it fetches and displays the historical open, close, and volume data for the stock. Users can also record their sentiment (Bullish or Bearish) for the stock, which is saved in a CSV file for future reference.

## Features

- **News Article Fetching**: Fetches recent news articles related to the entered stock name using the News API.
- **Sentiment Analysis**: Performs sentiment analysis on news headlines using the DistilBERT model to determine the sentiment trend over time.
- **Stock Data Visualization**: Fetches and displays historical stock data (open, close, volume) using the Alpha Vantage API and yfinance.
- **User Sentiment Recording**: Allows users to record their sentiment (Bullish or Bearish) for the stock, which is saved in a CSV file.

## Installation

1. **Clone the repository**:

    ```bash
   git clone https://github.com/muditgaur-1009/News-Vibes.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd News-Vibes
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API keys**:

    - Obtain a News API key from [https://newsapi.org/account](https://newsapi.org/account).
    - Obtain an Alpha Vantage API key from [https://www.alphavantage.co/](https://www.alphavantage.co/).
    - Open the `utils/constants.py` file and add your API keys:

        ```python
        NEWS_API_KEY = "<Your_News_API_Key>"
        ALPHA_VANTAGE_API_KEY = "<Your_Alpha_Vantage_API_Key>"
        ```

5. **Run the application**:

    ```bash
    streamlit run app.py
    ```

    The application will start running, and you can access it in your web browser at `http://localhost:8501`.

## Usage

1. **Enter a Stock Name**: In the input field, enter the name of the stock you want to analyze (e.g., "Adani Power", "Tatamotors").
2. **Analyze Sentiment**: Click the "Analyze Sentiment" button to fetch news articles, perform sentiment analysis, and display the sentiment trend and historical stock data.
3. **Record Your Sentiment**: After reviewing the analysis, you can record your sentiment (Bullish or Bearish) for the stock, which will be saved in a CSV file.



