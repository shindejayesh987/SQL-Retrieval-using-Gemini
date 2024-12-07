# Gemini SQL Query Retrieval App

This project demonstrates a Streamlit application that leverages Google's Gemini AI model to convert natural language questions into SQL queries and retrieve data from an SQLite database.

## Overview

The Gemini SQL Query Retrieval App allows users to input questions in plain English, which are then converted into SQL queries using Google's Gemini AI model. The SQL queries are executed against an SQLite database, and the results are displayed to the user in an interactive web interface built with Streamlit.

## Features

- Converts natural language questions to SQL queries.
- Retrieves and displays data from an SQLite database.
- Simple and interactive web interface using Streamlit.

## Prerequisites

- Python 3.6 or higher
- Docker (optional, for containerized deployment)

## Setup

### Clone the Repository

```sh
git clone (https://github.com/shindejayesh987/SQL-Retrieval-using-Gemini)
```


### Install Dependencies

Install the required Python libraries listed in requirements.txt:

```sh
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the project directory and add your Google API key:

```sh
GOOGLE_API_KEY=your_google_api_key
```

## Database Setup
Run the sqlite.py script to set up the SQLite database (student.db) and insert sample data:

```sh
python sqlite.py
```

## Usage
To start the Streamlit application, run:

```sh
streamlit run sql.py
```


Open your web browser and navigate to http://localhost:8501 to access the Gemini SQL Query Retrieval App.

# File Descriptions

## sql.py
This script is the main application that:

  - Loads environment variables using Python Dotenv.
  - Configures the Google Gemini AI model using google.generativeai.
  - Defines functions to interact with the Gemini AI model and SQLite database.
  - Sets up and runs the Streamlit web application to handle user input, query generation, and data retrieval.

## sqlite.py
This script sets up the SQLite database (student.db):

  - Creates the STUDENT table with columns NAME, CLASS, and SECTION.
  - Inserts sample records into the STUDENT table for demonstration purposes.

## requirements.txt
This file lists the Python dependencies required for the project:

  - streamlit: For building and serving the web interface.
  - google-generativeai: For using Google's Gemini AI model.
  - python-dotenv: For loading environment variables from .env file.

## Dependencies
  - Streamlit: A Python library for creating interactive web applications.
  - Google Generative AI: Python package for accessing Google's AI models.
  - Python Dotenv: Python library for managing environment variables.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
