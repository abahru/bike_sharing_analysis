import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# Plot trip duration distribution
plt.figure(figsize=(10, 5))
df.groupby('member_casual')['trip_duration'].plot(kind='hist', alpha=0.6, bins=50, legend=True)
plt.xlabel("Trip Duration (Minutes)")
plt.ylabel("Count")
plt.title("Trip Duration Distribution: Members vs. Casual Riders")
plt.savefig("trip_duration_distribution.png")
plt.show()

# Count bike type preference
bike_pref = df.groupby(['member_casual', 'rideable_type']).size().unstack()

# Plot bike type preference
bike_pref.plot(kind='bar', stacked=True, figsize=(8, 5))
plt.ylabel("Number of Trips")
plt.title("Bike Type Preference: Members vs. Casual Riders")
plt.savefig("bike_type_preference.png")
plt.show()
