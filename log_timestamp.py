#!/usr/bin/env python3
"""
Script to log the current date and time in AEST to a CSV file.
This will be run by a GitHub Action on a schedule.
"""
import csv
from datetime import datetime
import pytz
import os

# Define the CSV file path
CSV_FILE = 'timestamps.csv'

def log_timestamp():
    """Log the current date and time in AEST timezone to a CSV file."""
    # Define AEST timezone
    aest = pytz.timezone('Australia/Sydney')
    
    # Get current time in AEST
    current_time = datetime.now(aest)
    
    # Format the timestamp
    timestamp_str = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.isfile(CSV_FILE)
    
    # Append to CSV file
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(['Timestamp', 'Date', 'Time', 'Timezone'])
        
        # Write the timestamp data
        writer.writerow([
            timestamp_str,
            current_time.strftime('%Y-%m-%d'),
            current_time.strftime('%H:%M:%S'),
            current_time.strftime('%Z')
        ])
    
    print(f"Logged timestamp: {timestamp_str}")

if __name__ == '__main__':
    log_timestamp()
