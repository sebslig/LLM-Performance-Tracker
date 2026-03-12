import streamlit as st
import pandas as pd
import plotly.express as px
from core.storage import MetricsStore

st.set_page_config(page_title="LLM Eval Dashboard", layout="wide")

st.title("Model Performance Leaderboard")

store = MetricsStore()
data = store.load_all()

if not data:
    st.info("No evaluation data found. Run a benchmark first!")
else:
    df = pd.DataFrame(data)
    
    # Summary Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Avg Latency", f"{df['latency_ms'].mean():.2f} ms")
    c2.metric("Avg Cost", f"${df['cost_usd'].mean():.5f}")
    c3.metric("Total Runs", len(df))

    # Visualization
    st.subheader("Latency vs Cost")
    fig = px.scatter(df, x="latency_ms", y="cost_usd", color="model_id", 
                     hover_data=["prompt"], title="Performance Tradeoffs")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Raw Results")
    st.dataframe(df.sort_values("timestamp", ascending=False))
