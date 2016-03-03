from rest_framework.response import Response
from . import helpers
import constants

GENERIC = 0
AUTH = 1

def errors(t):
    fn = helpers.renderToJson(['title', 'message',])
    
    responses = (
        (GENERIC, fn(['Error', 'Error has occured'])),
        (AUTH, fn(['Auth Error', 'Invalid Credentials'])),
    )
    
    return {
        'error': responses[t][1]
    }

def render_error(t=0):
    err_type = t
    return Response(errors(err_type), status=404)