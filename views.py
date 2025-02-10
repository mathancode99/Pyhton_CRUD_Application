from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    if request.method == "POST":
        student_info = Student (S_name=request.POST.get('name'),
                               S_dept=request.POST.get('dept'),
                               S_rollno=request.POST.get('rollno'),
                               S_mobile=request.POST.get('mobile'))
        student_info.save()
        
        return redirect('home')
        
        
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def Studentdetails(request):
    
    context={
        "all_details": Student.objects.all(),
    }
    
    return render(request,'student_details.html',context)
    
    
def deldata(request,id):
    
    delete_info=Student.objects.get(id = id)
    
    delete_info.delete()
    
    return redirect('/sd')    


def updatedata(request,id):
    
    update_info=Student.objects.get(id = id)
    
    if request.method == "POST":
        
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        roll=request.POST.get('rollno')
        mobile=request.POST.get('mobile')
        
        update_info.S_name=name
        update_info.S_dept=dept
        update_info.S_rollno=roll
        update_info.S_mobile=mobile
        
        update_info.save()
        
        return redirect('/sd')
         
    return render(request,'index.html',{'data':update_info})    
    
    