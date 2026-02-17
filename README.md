# Streamlit Actions Flow Test

This repository demonstrates a simple timestamp logging system that uses GitHub Actions and Streamlit.

## Overview

The system consists of three main components:

1. **Python Script** (`log_timestamp.py`): Logs the current date and time in AEST (Australian Eastern Standard Time) to a CSV file
2. **GitHub Action** (`.github/workflows/log_timestamp.yml`): Runs the Python script on a schedule (every hour) and commits the updated CSV file
3. **Streamlit App** (`streamlit_app.py`): Displays the timestamp data from the CSV file in a user-friendly interface

## How It Works

### Automated Logging
- The GitHub Action runs automatically every hour (or can be triggered manually)
- It executes the Python script to add a new timestamp entry to `timestamps.csv`
- The updated CSV file is automatically committed back to the repository

### Streamlit Dashboard
- Hosted on Streamlit Community Cloud
- Reads and displays all timestamps from the CSV file
- Shows statistics (total entries, first entry, latest entry)
- Provides a download button for the CSV data
- Updates automatically when the CSV file is updated

## Local Development

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running the Timestamp Logger
```bash
python log_timestamp.py
```

### Running the Streamlit App
```bash
streamlit run streamlit_app.py
```

## Files

- `log_timestamp.py` - Script that logs timestamps to CSV
- `streamlit_app.py` - Streamlit application for displaying timestamps
- `timestamps.csv` - CSV file containing logged timestamps
- `requirements.txt` - Python dependencies
- `.github/workflows/log_timestamp.yml` - GitHub Action workflow configuration

## Deployment

### Streamlit Cloud
1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy the app by selecting this repository
5. The app will automatically use `streamlit_app.py` as the entry point

### GitHub Actions
The workflow is automatically enabled and will run:
- Every hour at minute 0
- On push to the main branch
- Manually via the "Actions" tab in GitHub