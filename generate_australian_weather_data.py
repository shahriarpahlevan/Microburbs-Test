import openai
import pandas as pd

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

# Define cities and seasons
cities = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide']
seasons = ['Summer', 'Autumn', 'Winter', 'Spring']

# Function to get weather description from OpenAI
def get_weather_description(city, season):
    prompt = f"What is the typical weather like in {city}, Australia during {season}?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Create an empty dictionary to store the data
data = {city: [] for city in cities}

# Populate the dictionary with LLM responses
for season in seasons:
    for city in cities:
        weather_description = get_weather_description(city, season)
        data[city].append(weather_description)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data, index=seasons)

# Save the DataFrame to a CSV file
csv_filename = 'australian_cities_weather.csv'
df.to_csv(csv_filename)

print(f"CSV file '{csv_filename}' generated successfully.")