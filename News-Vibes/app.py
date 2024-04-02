import streamlit as st
from modules.news_api import fetch_news
from modules.sentiment_analysis import init_classifier, analyze_sentiment
from modules.stock_data import fetch_ticker_symbol, fetch_historical_data
import plotly.graph_objs as go
import csv
from datetime import datetime

# Initialize the sentiment analysis classifier
classifier = init_classifier()

# Streamlit setup for user input
st.title("News Vibes")
stock_name = st.text_input("Enter the stock name:")

analysis_done = False

if st.button("Analyze Sentiment"):
    ticker_symbol = fetch_ticker_symbol(stock_name)
    if ticker_symbol:
        with st.spinner('Fetching and analyzing news...'):
            counts = []
            dates = []
            count = 0
            
            news_articles = fetch_news(stock_name)
            for title, published_at in news_articles:
                sentiment = analyze_sentiment(classifier, title)
                count += 1 if sentiment == 'POSITIVE' else -1
                counts.append(count)
                dates.append(published_at)
            
            fig = go.Figure(
                data=[go.Scatter(
                    x=dates,
                    y=counts,
                    mode='lines+markers',
                    hoverinfo='text',
                    text=[title for title, _ in news_articles]
                )]
            )
            fig.update_layout(
                title='Sentiment Over Time',
                xaxis_title='Date Published',
                yaxis_title='Sentiment Count',
                hovermode='closest'
            )
            st.plotly_chart(fig, use_container_width=True)

            news_text = "\n\n".join([f"{title} - {published_at[:10]}" for title, published_at in news_articles])
            st.text_area("News Articles:", news_text, height=300)


            historical_data = fetch_historical_data(ticker_symbol)
            st.write(f"Historical Data for {stock_name} ({ticker_symbol}):")
            # Extract and plot the open, close, and volume data
            open_data = []
            close_data = []
            volume_data = []
            hist_dates = []
            for date, values in historical_data.items():
                hist_dates.append(date)
                open_data.append(float(values["1. open"]))
                close_data.append(float(values["4. close"]))
                volume_data.append(int(values["5. volume"]))

            # Plotting open and close data
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=hist_dates, y=open_data, name="Open", line=dict(color="blue")))
            fig.add_trace(go.Scatter(x=hist_dates, y=close_data, name="Close", line=dict(color="green")))
            fig.update_layout(title="Open and Close Prices Over Time", xaxis_title="Date", yaxis_title="Price")
            st.plotly_chart(fig, use_container_width=True)

            # Plotting volume data
            fig = go.Figure()
            fig.add_trace(go.Bar(x=hist_dates, y=volume_data, name="Volume", marker_color="red"))
            fig.update_layout(title="Volume Over Time", xaxis_title="Date", yaxis_title="Volume")
            st.plotly_chart(fig, use_container_width=True)


            analysis_done = True

if analysis_done:
    # Ask for user opinion after displaying all graphs
    st.write("Your Opinion:")
    col1, col2 = st.columns(2)
    sentiment = None
    if col1.button("Bullish", key="bullish"):
        sentiment = "Bullish"
    if col2.button("Bearish", key="bearish"):
        sentiment = "Bearish"

    # Create CSV file with stock name, date, user input, and latest values
    if sentiment:
        with open("data/stock_sentiment.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if hist_dates:
                latest_date = hist_dates[0]  # Assuming the first date is the latest
                latest_open = open_data[0]
                latest_close = close_data[0]
                latest_volume = volume_data[0]
                writer.writerow([stock_name, datetime.now().strftime("%Y-%m-%d"), sentiment,
                                 latest_open, latest_close, latest_volume])
            else:
                writer.writerow([stock_name, datetime.now().strftime("%Y-%m-%d"), sentiment])
        st.success(f"Recorded {sentiment} sentiment for {stock_name}")
