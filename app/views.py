from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'insert_topic.html',context=d)
def insert_webpage(request):
    WOL=Webpage.objects.all() #webpage objects all we will store into wol getted from database..
    d={'webpage':WOL}
    return render(request,'insert_webpage.html',context=d)
def insert_access(request):
    AOL=AccessRecord.objects.all()
    d={"access":AOL}
    return render(request,'insert_access.html',context=d)