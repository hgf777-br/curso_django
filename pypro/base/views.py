from django.http import HttpResponse

# Create your views here.


def home(request):
    raise ValueError()
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        Olá Django!
    </body>
    </html>""", content_type='text/html')
