from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://vladtsap.com',
        '*'
    ],  # TODO?
    allow_methods=["*"],
    allow_headers=["*"],
)

COUNTER = 0


@app.get('/')
def test_request():
    return Response()


@app.get('/test')
def test_counter():
    global COUNTER
    COUNTER += 1
    return COUNTER


@app.get('/blog/{post_path}')
def count_blog_views(post_path: str, request: Request):
    print()
    print(post_path)
    print(request.client.host)
    print(request.headers)
    global COUNTER
    COUNTER += 1
    print(COUNTER)
    return COUNTER
