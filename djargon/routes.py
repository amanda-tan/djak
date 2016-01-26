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
        message='You can contact me at rob 5 at uw dot edu.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Djargon is all about using Bottle to build out some documentation on Azure.',
        year=datetime.now().year
    )

# This is copycat of '/about' and so on; it doesn't render a static page (which is what I want at the moment)
# @route('/doc')
# @view('doc')
# def doc():
#     """Renders the simple doc page."""
#     return dict(
#         title='Doc',
#         message='Simple documentation page.',
#         year=datetime.now().year
#     )

# kilroy added this @route to bind the method 'kilroy_hardcoded_callback()' 
#   to the '/documentation' extension; see layout.tpl
@route('/documentation')
def kilroy_hardcoded_callback():
    return static_file('Djocumentation.pdf', root='./static/pdf/')

# kilroy: documentation.html at ./static/html is the older version; but this was a pain to build out of 
#   OneNote; took several tedious steps. 
