from waitress import serve
    
from davis_blog.wsgi import application
    
if __name__ == '__main__':
    serve(application, port='8000')