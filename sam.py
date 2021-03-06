from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    sum , mul = 0 , 0
    code = 'success'
    try:
        a, b = int(a), int(b)
        sum = a + b
        mul = a * b
        response_body = html % { 'sum' : sum, 'mul' : mul, 'code' : code}

    except ValueError:
        code  = 'Error'
        response_body = html % { 'sum' : sum, 'mul' : mul, 'code' : code}
    start_response('200 OK', [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))])
    return [response_body]

~                            

