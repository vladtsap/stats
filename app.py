from fastapi import FastAPI, Response, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config import SessionLocal
from db_manager import get_post_views

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://vladtsap.com',
    ],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return Response()


@app.get('/blog/{post_path}')
def count_blog_views(post_path: str, request: Request, db: Session = Depends(get_db)):
    return get_post_views(
        db=db,
        path=post_path,
        ip_address=request.client.host,
    )
