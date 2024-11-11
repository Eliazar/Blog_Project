import requests

class BlogManager:
    def __init__(self) -> None:
        self.BLOG_POST_BASE_URI = "https://api.npoint.io/c790b4d5cab58020d391"


    def get_blog_posts(self):
        response = requests.get(self.BLOG_POST_BASE_URI)
        return response.json()
    

    def get_blog_post_by_id(self, post_id):
        response = requests.get(self.BLOG_POST_BASE_URI)
        posts = response.json()

        return next((post for post in posts if post.get("id") == int(post_id)), None)