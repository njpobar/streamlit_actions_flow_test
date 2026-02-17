"""
Streamlit application to display timestamp data from CSV file.
"""
import streamlit as st
import pandas as pd
import os

# Configure the page
st.set_page_config(
    page_title="Timestamp Logger",
    page_icon="🕐",
    layout="wide"
)

# Title
st.title("🕐 Timestamp Logger - AEST")
st.markdown("This app displays timestamps logged by a GitHub Action in Australian Eastern Standard Time (AEST).")

# CSV file path
CSV_FILE = 'timestamps.csv'

# Check if the CSV file exists
if os.path.isfile(CSV_FILE):
    # Read the CSV file
    df = pd.read_csv(CSV_FILE)
    
    # Display statistics
    st.subheader("📊 Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Entries", len(df))
    
    with col2:
        if len(df) > 0:
            st.metric("First Entry", df.iloc[0]['Date'])
        else:
            st.metric("First Entry", "N/A")
    
    with col3:
        if len(df) > 0:
            st.metric("Latest Entry", df.iloc[-1]['Date'])
        else:
            st.metric("Latest Entry", "N/A")
    
    # Display the data
    st.subheader("📅 Timestamp Log")
    
    # Show most recent entries first
    df_display = df.iloc[::-1].reset_index(drop=True)
    
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True
    )
    
    # Display raw data option
    with st.expander("🔍 View Raw Data"):
        st.write(df_display)
    
    # Download button
    csv_data = df.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name="timestamps.csv",
        mime="text/csv"
    )
    
else:
    st.warning("⚠️ No timestamp data found. The CSV file will be created when the GitHub Action runs.")
    st.info("The GitHub Action will automatically log timestamps to the CSV file on a schedule.")
