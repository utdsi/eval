

from flask import Flask,request


app = Flask(__name__)

post=[]
count=1


@app.route("/")

def get():
    return post

@app.route("/add",methods=["GET","POST"])

def add_post():
    
    global post,count
    
    name = request.form.name
    posts = request.form.posts
    
    pos = {
        name:name,
        posts:posts,
        id:count
    }
    
    post.append(pos)
    count+=1
    
    return ({"msg":"posted successfully"})
 
 
@app.route("/delete/<int:id>",methods=["DELETE"])

def delete_post(id):
    
    global post 
    
    for item in post:
        
        if(post["id"]==id):
            
            del item 
            return ({"msg":"item deleted"})  
    return ({"msg":"post not found"})


if(__name__=="__main__"):
    
    app.run()