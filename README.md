# Data Analyst Assistant API

A simple FastAPI-based API for uploading and analyzing CSV files.
It provides mean, median, and standard deviation for numeric columns.

## Run the API

```bash
uvicorn main:app --reload
```

## Endpoint

POST `/analyze/`  
Body: CSV File  
Returns: JSON summary of data
