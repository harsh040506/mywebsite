from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample data - replace with your complete dataset
student_data = [
    {"name":"38","marks":79},{"name":"YduE","marks":82},{"name":"Og3","marks":27},{"name":"oT","marks":87},{"name":"Wn0","marks":36},{"name":"rX","marks":90},{"name":"dl","marks":81},{"name":"JN1XYR9xk","marks":34},{"name":"RE","marks":66},{"name":"6PutLE","marks":98},{"name":"WQHGSIe8","marks":23},{"name":"3pz9AiND","marks":28},{"name":"NsE","marks":28},{"name":"c","marks":63},{"name":"2udrKHv3Y","marks":90},{"name":"P3","marks":4},{"name":"Jz7nh5","marks":73},{"name":"6","marks":3},{"name":"4D","marks":54},{"name":"9U2vP","marks":78},{"name":"7I","marks":80},{"name":"kOBdIJ","marks":59},{"name":"Xv","marks":3},{"name":"4","marks":73},{"name":"ni4cdXlHBi","marks":63},{"name":"k3C9Fl9","marks":96},{"name":"F2FbcIpZ","marks":67},{"name":"ynyjje1l","marks":16},{"name":"ZWcOANQh6","marks":7},{"name":"br","marks":45},{"name":"ehM6CvyL","marks":22},{"name":"NY8","marks":38},{"name":"DIcMbKix","marks":36},{"name":"3h7","marks":42},{"name":"S","marks":85},{"name":"FE","marks":66},{"name":"O","marks":98},{"name":"vc","marks":44},{"name":"AB","marks":82},{"name":"K","marks":60},{"name":"4Cfn8","marks":29},{"name":"ceDyKRlSB","marks":23},{"name":"IFcL9VRD7c","marks":9},{"name":"av","marks":71},{"name":"lg6C","marks":58},{"name":"0OjH","marks":55},{"name":"n02DQ","marks":71},{"name":"BydO","marks":77},{"name":"b3Rx","marks":28},{"name":"qNZrfSoOd","marks":78},{"name":"h8l","marks":70},{"name":"49d34Vu","marks":36},{"name":"Q","marks":57},{"name":"eRT3XDhDc","marks":53},{"name":"IlcuKW","marks":1},{"name":"wEviLAUZ","marks":45},{"name":"A0bc","marks":37},{"name":"VDpuEU8","marks":12},{"name":"EsTxLaR1M","marks":13},{"name":"02","marks":19},{"name":"7Wan","marks":51},{"name":"nJCexyMc0","marks":33},{"name":"04eeZ","marks":85},{"name":"8D97Ho","marks":24},{"name":"0EF6ud","marks":3},{"name":"bC3DJt06BN","marks":96},{"name":"vl9","marks":53},{"name":"hr","marks":76},{"name":"5TnLz6BD","marks":52},{"name":"wgdcAtGnz9","marks":19},{"name":"g","marks":20},{"name":"o0","marks":38},{"name":"6DDTIpAqc","marks":59},{"name":"9CDg","marks":97},{"name":"x","marks":18},{"name":"mvwk3K","marks":41},{"name":"b6FdiM","marks":43},{"name":"4l8v6","marks":74},{"name":"wItBV2eLLZ","marks":32},{"name":"2h2DK74HQR","marks":12},{"name":"PsPBe1Wr0R","marks":98},{"name":"WDMcu","marks":30},{"name":"7Nx3H8","marks":22},{"name":"UwoAq","marks":27},{"name":"fy","marks":10},{"name":"EP1","marks":59},{"name":"xMjra6Tb","marks":36},{"name":"7xX4","marks":24},{"name":"xTeYA","marks":60},{"name":"akaPaYpC6S","marks":69},{"name":"8K","marks":11},{"name":"aC8Q","marks":11},{"name":"TM","marks":62},{"name":"dEnC8TVB","marks":68},{"name":"qS","marks":7},{"name":"HIZv","marks":46},{"name":"a2E32nT1M","marks":48},{"name":"EM9VVGBt","marks":64},{"name":"gCBNEuFPGT","marks":79},{"name":"KL","marks":41}
]

# Create lookup dictionary
student_marks = {student["name"]: student["marks"] for student in student_data}

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
