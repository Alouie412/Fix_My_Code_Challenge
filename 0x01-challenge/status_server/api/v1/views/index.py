#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


"""
Here is the error. It may not look like it, but in the __init__.py file
in the same level, the url_prefix is set to '/api/v1', which means
we can get rid of that here. The alternate solution is to get rid of
url_prefixes in the __init__.py file. Either works
"""
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
