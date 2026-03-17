# URL-shortener-service
Backend URL shortening service using Flask with short-code generation, REST APIs, and low-latency redirection

## Overview
This project is a lightweight URL shortening service similar to Bitly. It allows users to submit long URLs, generates unique short codes, and redirects users when the short link is accessed.

## Tech Stack
- Python
- Flask

## Features
- Generate short URLs
- Redirect to original URLs
- Simple web interface
- REST API endpoint for shortening links

## API
### POST /api/shorten
Request:
```json
{
  "url": "https://example.com/very/long/link"
}
{
  "original_url": "https://example.com/very/long/link",
  "short_code": "aB12xY",
  "short_url": "http://127.0.0.1:5000/aB12xY"
}
pip install -r requirements.txt
python app.py
