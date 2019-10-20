from django.shortcuts import render,redirect
from .models import Pitchingdata
from .forms import PostForm
from django_pandas.io import read_frame

def top(request):
    if request.method == "POST":
        batter = request.POST.get('batter',None)
        df = read_frame(Pitchingdata.objects.all(),fieldnames=['kyusyumark','pitcher','batter'])
        df = df.loc[df['batter']==batter,:]
        return render(request,'blog/detail.html',{'df':df})
    else:
        form = PostForm()
        return render(request,'blog/top.html',{'form':form})
