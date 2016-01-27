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
#   to the '/documentation' extension; see layout.tpl.
#   There is no view binding because the pdf would not coexist with a standard djargon page... faik!
@route('/documentation')
@route('/documentation.pdf')
@route('/documentation.fubar')
def kilroy_hardcoded_callback():
    return static_file('Djocumentation.pdf', root='./static/pdf/')

# kilroy: documentation.html at ./static/html is the older version; but this was a pain to build out of 
#   OneNote; took several tedious steps. 

@route('/api')
@view('api')
def api_no_args():
    """Renders the api page as documentation"""
    return dict(title='API', message='Format = djargon.a.n/api/hydrograph?qual=val&qual=val&qual=val&qual=val', year=datetime.now().year)

# Here is an example of using the same view for multiple routes
@route('/api/<command>')
@view('api')
def api(command):
    """Interprets an API call."""
    # kilroy debug: return dict(title='API', message=command, year=datetime.now().year)

    failed = 0
    fubar = command.split('&')
    thisCmd = 'null'

    #for c in args:
    #    thisArgPair = c.split('=')
    #    if thisArgPair[0] == 'command':
    #        thisCmd = thisArgPair[1]
    #        break

    return dict(title='API', message=command, year=datetime.now().year)

    #if thisCmd == 'hydrograph':
    #    goodMsg = str(len(args)) + ' args; '
    #    for i in range(len(args)):
    #        thisQual = args[i].split('=')
    #        if len(thisQual) != 2:
    #            failed = 3
    #            break
    #        if thisQual[0] == 'start':    goodMsg += 'start at ' + thisQual[1] + ', '
    #        if thisQual[0] == 'end':      goodMsg += 'end at ' + thisQual[1] + ', '
    #        if thisQual[0] == 'station':  goodMsg += 'station is ' + thisQual[1] + ', '
    #        if thisQual[0] == 'interval': goodMsg += 'interval is ' + thisQual[1] 
    #else: failed = 2
    #if failed > 0: return dict(title='API', message='Ooops qualifier parse failed with error = ' + str(failed), year=datetime.now().year)
    #else: return dict(title='API', message=goodMsg, year=datetime.now().year)
         
# kilroy: in this case we look for a filename fitting the regular expression *\.png where 
#   I put hockney.png in the appropriate folder. So url/images/hockney.png or url/image/hockney.png works...
#   but without suitable machinery (kilroy) it is just vestigial. 
@route('/images/<filename:re:.*\.png>')
@route('/image/<filename:re:.*\.png>')
def send_image(filename): 
    return static_file(filename, root='./static/images', mimetype='image/png')
