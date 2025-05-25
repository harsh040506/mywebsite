from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(names: List[str] = Query(..., alias="name")):
    """
    Get marks for students by name
    Example: /api?name=X&name=Y
    Returns: {"marks": [mark_X, mark_Y]}
    """
    try:
        marks = [student_marks.get(name) for name in names]
        return {"marks": marks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
