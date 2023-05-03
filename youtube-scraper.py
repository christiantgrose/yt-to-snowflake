import os
import json
from googleapiclient.discovery import build

# Set up YouTube Data API credentials
api_key = 'YOUR API KEY HERE'
youtube = build('youtube', 'v3', developerKey=api_key)

# Define parameters for the API request
params = {
    'part': 'snippet,statistics',
    'chart': 'mostPopular',
    'regionCode': 'GB',
    'maxResults': 100
}

# Call the API to retrieve the top 100 trending videos in the UK
response = youtube.videos().list(**params).execute()

# Save the results to a JSON file
with open('trending_videos_uk.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)


