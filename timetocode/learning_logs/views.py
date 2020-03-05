from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Home page for a learning log"""
    return render(request, 'learning_logs/index.html')

def topic(request,topic_id):
    """Show topic and all the entries"""
    return render(request,'learning_logs/topic.html')

def results(request):
        """Home page for a learning log"""
        user_input = request.GET['user_input']
        return render(request, 'learning_logs/result.html',{'home_input':user_input})