from flask import Flask, request, render_template, redirect, session, url_for
from database import User, Post, Comment, Database
import sqlite3

app = Flask(__name__)
app.secret_key="JRBS"

@app.route("/")
def home():
    return redirect(url_for('posts'))

@app.route("/login")
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        username = request.form["name"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        verify = Database(name, password)
        answer = verify.login()
        if not answer == "ok":
            return render_template("login.html", message = "Username does not exist or incorrect user/pw combination")
        else:
            redirect(url_for('posts'))

@app.route("/signup")
def signup():
    if request.method=="GET":
        return render_template("register.html")
    else:
        username = request.form["name"].encode("ascii", "ignore")
        password1 = request.form["password1"].encode("ascii", "ignore")
        password2 = request.form["password2"].encode("ascii", "ignore")
        displayname = request.form["displayname"].encode("ascii","ignore")
        button = request.form["button"]
        box = request.form["acceptTerms"]
        if button == "Register":
            if not box:                
                return render_template("register.html", message = "you need to check the box first")
            elif stuff.check(username) : #check will return true if  username is not found, false otherwise
                session["name"] = username
                add = Database(username, password)
                add.register()
                return redirect(url_for('posts'))
        
@app.route("/new")
def new():
    button1 = request.form["cancel"]
    button2 = request.form["submit"]
    title = request.form["title"]
    post = request.form["post"]
    if request.method=="GET":
        return render_template("new.html")
    elif button1:
        return redirect(url_for('posts'))
    elif button2:
        #add = Post() *****what to add in the parenthese...hmmmm....
        return redirect(url_for('posts'))

#@app.route("/archive")
#def archive():                     ****don't really see the difference b/w this and /posts, so will
#    if request.method=="GET":        comment this out for now******
#        return render_template

#@app.route("/admin") ******leaving this blank for now. saving for later.*****
#def admin(): *****admin should be able to delete posts and stuff here****

@app.route("/posts")
def posts():
    button = request.form["users"]
    page = request.form["pagenumber"]
    if request.method=="GET":
        return render_template("posts.html")
    elif button:
        if 'username' in session:
            user_id = stuff.getUser()
            return redirect(url_for('posts/user/{user_id}' % user_id))
        else
            page_number = page #don't think this works, but putting it here anyway
            return redirect(url_for('posts/{page_number}' % page)

@app.route("/posts/{page_number}")
def posts():
    button = request.form["home"]
    page = request.form["pagenumber"]
    if request.method=="GET":
        return render_template("posts") #dunno what to do here, maybe use databse to create the page?
    elif button == "home"
        return redirect(url_for('posts')
    else
        page_number = page
        return redirect(url_for('posts/{page_number}' % page)
    
@app.route("/posts/user/{user_id}")
def posts():
    button = request.form["home"]
    page = request.form["pagenumber"]
    if request.method=="GET":
        return render_template("posts") #same as above
    elif button == "home"
        return redirect(url_for('posts')
    else 
        page_number = page
        return redirect(url_for('posts/user/{user_id}/{page_number}' % page))

@app.route("/posts/user/{user_id}/{page_number}")
def posts():
    button = request.form["home"]
    page = request.form["pagenumber"]
    if request.method=="GET":
        return render_template("posts") # same as above
    elif button == "home"
        return redirect(url_for('posts')
    else
        page_number = page
        return redirect(url_for('posts/user/{user_id}/{page_number}'))

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('posts')
