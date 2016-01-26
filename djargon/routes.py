"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

# kilroy added this for static content
from bottle import static_file

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/doc')
@view('doc')
def doc():
    """Renders the simple doc page."""
    return dict(
        title='Doc',
        message='Simple documentation page.',
        year=datetime.now().year
    )

# The following is supposed to get us an html file.
#   The first line shows the URL extension: djargon.azurewebsites.net/documentation
#   The second line points to a view (see view folder; file extension is .tpl ('.template')
#     It is unclear if this points to the subsequent function. 


# The static_file() function is a helper to serve files in a safe and convenient 
# way (see Static Files). This example is limited to files directly within the 
# /path/to/your/static/files directory because the <filename> wildcard won’t 
# match a path with a slash in it.
@route(’/static/documentation’)
def server_static(filename):
return static_file(filename, root=’/path/to/your/static/files’)


@route('/documentation')
@view('documentation')
def documentation():
    """Renders the extensive documentation page."""
    return dict(
        title='Documentation',
        message='Big documentation page.',
        year=datetime.now().year
    )