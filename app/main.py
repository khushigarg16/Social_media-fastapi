from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

#models.Base.metadata.create_all(bind= engine)  //since we have alembic so don't need it

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return{"data": posts}


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='khushi16', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break

#     except Exception as error:
#         print("Connecting to databse failed")
#         print("Error: ", error)
#         time.sleep(2)



# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {"data": posts}

# @app.post("/posts")
# def create_posts(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#      (post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found")
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()

#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING * """,
#      (post.title, post.content, post.published, str(id),))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return {"data": updated_post}


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate (my_posts):
#         if p['id'] == id:
#             return i


# @app.get("/")
# def root():
#     return {"message": "Welcome to fastapi"}


# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}


# @app.post("/createposts")
# def create_posts(payLoad: dict = Body(...)):
#     print (payLoad)
#     return {"message": "Successfully created post"}

# @app.post("/createposts")
# def create_posts(payLoad: dict = Body(...)):
#     print (payLoad)
#     return {"new_post": f"title: {payLoad['title']}, content: {payLoad['content']}"}

# @app.post("/posts")
# def create_posts(post: Post):
#     print (post)
#     print (post.dict())
#     return {"data": post}

# @app.post("/posts", status_code = status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict['id'] = randrange(0, 1000000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}


# @app.get("/posts/{id}")
# def get_post(id):
#     print(id)
#     return {"post_detail": f"Here is post of id {id}"}

# @app.get("/posts/{id}")
# # def get_post(id: int, reponse: Response):
# def get_post(id: int):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} was not found")
#         # reponse.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id {id} was not found"}
#     return {"post_detail": post}


# @app.delete("/posts/{id}", status_code =status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     # deleting post
#     # find the index in the array that has the required id
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
#     my_posts.pop(index)
#     # return {"message": "post was successfully deleted"}
#     return Response(status_code = status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
#     return {"data": post_dict}