# Supabase + Streamlit Demo

This is a demo application that showcases integration between Supabase and Streamlit.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Supabase credentials:
```
SUPABASE_URL=https://dfynoybzknipsilokcpe.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmeW5veWJ6a25pcHNpbG9rY3BlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU0NDMxODksImV4cCI6MjA2MTAxOTE4OX0.qNXzV84tr-oCYuCKqEAW2ZaYQviT1D3eh0WNFU9TxZI
```

3. Run the app:
```bash
streamlit run app.py
```

## Deployment

This app can be deployed to GitHub Pages or other platforms. For GitHub Pages:

1. Push your code to GitHub
2. Go to your GitHub repository settings
3. Enable GitHub Pages under the "Pages" section
4. Select the main branch as the source

## Features

- Basic Streamlit UI
- Supabase client integration
- Environment variable support
- Form handling
