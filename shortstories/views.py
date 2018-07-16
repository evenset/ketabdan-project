from django.http import HttpResponse
def index(request):
    return  HttpResponse('Author,Title,Status,Publication_Date')



