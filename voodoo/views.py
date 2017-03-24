from django.shortcuts import render


def index(req):
    """renders index page"""
    return render(req, 'index.html', {})
