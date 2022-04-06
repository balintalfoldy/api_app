from typing import List
from app import api_schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    def validate(post):
        return api_schemas.PostOut(**post)
    
    post_map = map(validate, res.json())
    posts_list = list(post_map)

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = api_schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id