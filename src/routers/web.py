from fastapi import APIRouter # type: ignore
from starlette.responses import HTMLResponse # type: ignore

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>Car Sharing Demo</head>
        <body>
            <h1>Welcom to car sharing service.</h1>
            <p>Here is some text for you.</p>
        </body>
    </html>
    """
