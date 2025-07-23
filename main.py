from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/analyze/")
async def analyze_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    summary = {
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "mean": df.mean(numeric_only=True).to_dict(),
        "median": df.median(numeric_only=True).to_dict(),
        "std_dev": df.std(numeric_only=True).to_dict()
    }

    return JSONResponse(content=summary)
