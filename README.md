# AI News Intelligence Platform

An end-to-end Python data pipeline that ingests live news articles, generates automated AI summaries using Google's Gemini Large Language Model, and stores the processed intelligence in a structured PostgreSQL database. 

## Technical Stack
* **Language:** Python 3.x
* **AI/LLM:** Google Gemini API (`google.genai`, Gemini 3.8 Flash)
* **Database:** PostgreSQL (`psycopg2`)
* **Configuration:** Environment Variables (`python-dotenv`)

## System Capabilities & Metrics
* **Global Ingestion Scale:** Built on top of a News API infrastructure capable of querying and retrieving real-time data from 80,000+ global publications and endpoints.
* **LLM Data Compression:** Utilizes advanced transformer models to synthesize raw article text, reducing qualitative data volume by ~90% to generate rapid, highly concentrated intelligence briefings.
* **High-Performance Storage:** Leverages parameterized SQL queries to process and insert batched pipeline data into PostgreSQL with sub-second local execution times.
* **Fault Tolerance:** Engineered with robust exception handling to bypass API rate limits and server unavailability (HTTP 503), preventing pipeline crashes during high-volume processing loops.

## Core Features
* **Automated Topic Searching:** Dynamically fetches real-time articles based on user-defined technological domains (e.g., AI, Robotics, LLMs).
* **Automated Data Processing:** Extracts, cleans, and maps deeply nested JSON API responses into native Python objects.
* **Relational Database Mapping:** Safely inserts the combined API metadata (Source, URL, Published Date) and AI insights into a local relational schema.
* **Secure Configuration:** Protects database credentials and cloud API keys using strict environment variable management, completely isolated from version control.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install the required Python dependencies: `pip install google-genai psycopg2 python-dotenv`
3. Set up a local PostgreSQL server and create a database named `placement_project`.
4. Create the required table by running the following SQL query in pgAdmin:
   ```sql
   CREATE TABLE analyzed_articles (
       id SERIAL PRIMARY KEY,
       title TEXT NOT NULL,
       source TEXT,
       url TEXT,
       published_date TEXT,
       ai_summary TEXT,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );