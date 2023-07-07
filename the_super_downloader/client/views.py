from django.shortcuts import render
from client.download import Downloader

def download(request):

    return render(request, 'download.html')
