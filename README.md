# auto-medium-poster

# AI-Powered Blog Post Generator and Publisher

This project uses Google Gemini API to generate AI-powered blog content on a specific topic and automatically posts the generated content to Medium using the Medium API. The blog generation and posting tasks are scheduled to run daily at a specified time.

## Features

- Automatically generates blog content using Google Gemini API.
- Posts the generated content to Medium.
- Scheduled to run daily at a specified time.
- Customizable content and scheduling.

## Technologies Used

- **Google Generative AI (Gemini API)**: Used for generating blog content.
- **Medium API**: Used for posting the generated blog to Medium.
- **Schedule**: Used to schedule the task to run at a specific time.
- **Requests**: For making HTTP requests to the Medium API.

## Prerequisites

- Python 3.x
- A Medium account and a valid Medium API key.
- Access to Google Gemini API with a valid API key.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blog-post-generator.git
   cd blog-post-generator
