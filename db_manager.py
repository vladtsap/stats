from sqlalchemy import func
from sqlalchemy.orm import Session

from models import Post


def process_post_view(db: Session, path: str, ip_address: str):
    post = db.query(Post).filter(
        Post.path == path,
        Post.ip_address == ip_address
    ).first()

    if post:
        post.views += 1
        db.commit()
    else:
        post = Post(
            path=path,
            ip_address=ip_address,
            views=1,
        )
        db.add(post)
        db.commit()


def get_post_views(db: Session, path: str, ip_address: str) -> int:
    process_post_view(db, path, ip_address)

    post = db.query(
        func.count(Post.id).label('unique_views')
    ).filter(
        Post.path == path
    ).first()

    return post.unique_views
