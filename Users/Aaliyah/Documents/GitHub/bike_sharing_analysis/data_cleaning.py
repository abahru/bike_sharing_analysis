import pandas as pd

# Load dataset
df = pd.read_csv("202405-capitalbikeshare-tripdata.csv")

# Convert timestamps to datetime
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# Calculate trip duration in minutes
df['trip_duration'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# Remove trips with duration <= 0
df = df[df['trip_duration'] > 0]

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("✅ Data cleaned and saved!")
