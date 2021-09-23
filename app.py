from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    root_path='/stats',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # TODO?
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
    print(post_path)
    print(request.client.host)
    # print(request.headers)
    print()
    global COUNTER
    COUNTER += 1
    return COUNTER
