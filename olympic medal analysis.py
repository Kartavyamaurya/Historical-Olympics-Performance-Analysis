# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load datasets
try:
    # Adjust paths as needed if using local files
    dict_df = pd.read_csv("dictionary.csv")
    summer_df = pd.read_csv("summer.csv")
    winter_df = pd.read_csv("winter.csv")

    print("Datasets loaded successfully.")
except FileNotFoundError as e:
    print(f"Error loading datasets: {e}")

# Display the first few rows of the summer dataset
print("Sample data from Summer Olympics:")
print(summer_df.head())

# Basic information about the dataset
print("\nDataset Information:")
print(summer_df.info())

# Cleaning the dataset
print("\nChecking for missing values:")
print(summer_df.isnull().sum())

# Fill or drop missing values based on requirements
# Example: Dropping rows with missing values
summer_df = summer_df.dropna()

# Key Analysis and Visualizations
# 1. Distribution of Medals by Country
country_medals = summer_df.groupby("Country")["Medal"].count().sort_values(ascending=False)
print("\nTop countries by medals:")
print(country_medals.head(10))

# Visualization of top 10 countries by medals
top_countries = country_medals.head(10)
plt.figure(figsize=(10, 6))
top_countries.plot(kind="bar", color="gold", edgecolor="black")
plt.title("Top 10 Countries by Total Medals")
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.show()

# 2. Distribution of Medals by Sport
sport_medals = summer_df.groupby("Sport")["Medal"].count().sort_values(ascending=False)
print("\nTop sports by medals:")
print(sport_medals.head(10))

# Visualization of top 10 sports by medals
top_sports = sport_medals.head(10)
plt.figure(figsize=(10, 6))
top_sports.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 10 Sports by Total Medals")
plt.xlabel("Sport")
plt.ylabel("Number of Medals")
plt.show()

# 3. Medal Trends Over Years
year_medals = summer_df.groupby("Year")["Medal"].count()
plt.figure(figsize=(10, 6))
year_medals.plot(kind="line", marker="o", color="green")
plt.title("Medals Trend Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.grid(True)
plt.show()

# Save cleaned data
summer_df.to_csv("cleaned_summer_olympics.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_summer_olympics.csv'.")
