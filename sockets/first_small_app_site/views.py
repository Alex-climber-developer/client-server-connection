def blog():
  with open('client-server connection/sockets/first_small_app_site/templates/blog.html') as blog:
    return blog.read()

def index():
  with open('client-server connection/sockets/first_small_app_site/templates/index.html') as index:
    return index.read()
