import google.generativeai as genai
import requests
import schedule
import time

# Set API endpoint and credentials
medium_api_key = "YOUR_MEDIUM_API_KEY"
google_api_key = "YOUR_GOOGLE_API_KEY"  # Replace with your Google API key
userId = "19e1e4a66a01690cf3a5797425317c758513e89488cf9b7ccea68e62fb03b7a14"

# Set Gemini API key
genai.configure(api_key=google_api_key)

# Define function to generate and post blog
def generate_and_post_blog():
    try:
        # Generate blog content using Gemini API
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Write a blog post on the topic of AI")

        # Extracting the blog content from the response correctly
        if response.candidates and len(response.candidates) > 0:
            content = response.candidates[0].content.parts[0].text  # Correct access to content
            print("Generated blog content:", content)
        else:
            print("No content generated.")
            return

    except Exception as e:
        print("Error generating blog content:", str(e))
        return

    # Set API endpoint for Medium
    api_endpoint = f"https://api.medium.com/v1/users/{userId}/posts"

    # Set API headers and data
    headers = {"Authorization": f"Bearer {medium_api_key}", "Content-Type": "application/json"}
    data = {
        "title": "Artificial Intelligence: The Future of Technology",  # Use a dynamic title if needed
        "content": content,
        "contentFormat": "html"
    }

    # Make API call to post content
    try:
        response = requests.post(api_endpoint, headers=headers, json=data)
        if response.status_code == 201:
            print("Blog post created successfully!")
        else:
            print("Error creating blog post:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error posting blog to Medium:", str(e))

# Schedule the function to run every day at the specified time (use 24-hour format)
schedule.every().day.at("19:13").do(generate_and_post_blog)

print("Scheduling task to generate and post blog every day at 8:00 AM...")

# Keep the script running to execute the scheduled task
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
