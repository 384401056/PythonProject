from django.http import HttpResponse
from django.shortcuts import render
import os
from django_Q.settings import BASE_DIR
# Create your views here.

def index(request):
    return render(request, 'FileUpload/index.html')

def upload(request):
    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        print(type(myfile),myfile) # InMemoryUploadedFile类型
        print(myfile.name)
        print(myfile.chunks()) # 文件的字节块

        with open( os.path.join('FileUpload/files/',myfile.name), 'wb') as f:
            for chunk in myfile.chunks(): # chunk 将大文件分块，每次64k
                print(chunk)
                f.write(chunk)

    return HttpResponse('OK')