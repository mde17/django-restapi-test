from rest_framework.response import Response
from . import helpers

GENERIC = 0
AUTH = 1

def errors(t):
    fn = helpers.renderToJson(['title', 'message','status',])
    
    responses = (
        (GENERIC, fn(['Error', 'Error has occured', 400])),
        (AUTH, fn(['Auth Error', 'Invalid Credentials', 401])),
    )
    
    return {
        'error': responses[t][1]
    }

def render_error(t=0):
    err_type = t
    return Response(errors(err_type), status=404)