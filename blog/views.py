from django.shortcuts import render,redirect
from .models import Pitchingdata
from .forms import PostForm
from django_pandas.io import read_frame


def top(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            balltype = form.cleaned_data['balltype']
            batter = form.cleaned_data['batter']
            df = read_frame(Pitchingdata.objects.all())
            df = df.loc[(df['batter']==batter) & (df['balltype']==balltype)]
            return render(request,'blog/detail.html',{'df':df})
    else:
        form = PostForm()
        batter_list = set(Pitchingdata.objects.values_list('batter',flat=True))
        balltype_list = set(Pitchingdata.objects.values_list('balltype',flat=True))

    return render(request,'blog/top.html',{'form':form,'batter':batter_list,'balltype':balltype_list})
