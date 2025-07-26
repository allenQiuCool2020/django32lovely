from django.http import HttpResponse
import random
"""
To render html web pages
"""

def home(request):
    name = "Allen"
    number = random.randint(1, 100)
    HTML_STRING = f"""
    <h1>Hi there, {name}! - {number} </h1>
    """
    return HttpResponse(HTML_STRING)