from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

@app.route('/cl/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return "hi"

# @app.route('/login')
# def login():
#     return "asdasd"

@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')
    # if request.method == 'POST':
    #     print "do nothing"
    # else:
    #     print "show!!!"


#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/')
# def index():
#     print 'as'
# #

#
# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name
#
@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

with app.test_request_context():
   print url_for('index', filename='style.css')
   print url_for('login')
   print url_for('profile', username='saul')

#
# @app.route('/hello')
# def hello_world():
#     return 'Hello, World!'
#
# @app.route('/user/<username>')
# def profile(username): pass
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
# @app.route('/about')
# def about():
#     return 'The about page'
# #
# with app.test_request_context():
#     print url_for('index')
#     print url_for('login')
#     print url_for('profile', username='Saul Toscano')
