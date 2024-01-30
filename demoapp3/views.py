from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import regform
from.models import reg

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello, World!")

def hello_world(request):
    return render(request, 'hello.html')

def insert(request):
    form= regform()
    if request.method=='POST':
        form=regform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
    return render(request,'form.html',{'form':form})




def login(request):
    return render(request, 'login.html')




def userlog(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        cr=reg.objects.filter(username=username, password=password)
        if cr:
            user_details=reg.objects.get(username=username, password=password)

            id=user_details.id
            name=user_details.name
            username=user_details.username
            email=user_details.email

            request.session['id']=id
            request.session['name']=name
            request.session['username']=username
            request.session['email']=email
            
            return redirect('welcome')
        else:
           
            return render(request,'login.html')
    else:
        return render(request,'view.html')
    
def welcome(request):
     id= request.session['id']
     name=request.session['name']
     username=request.session['username']
     return render(request, 'welcome.html',{'id':id,'name':name,'username':username})
 
def view(request):
    cr=reg.objects.all()
    return render(request, 'view.html',{'cr':cr})

def detail_view(request,pk):
     cr=reg.objects.get(id = pk)
     return render(request,'detail_view.html',{'cm':cr})
 
def update(request,pk):
    dr=reg.objects.get(id=pk)
    form=regform(instance=dr)
    if request.method =="POST":
        form=regform(request.POST,instance=dr)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,"update.html",{'form':form})

def delete(request,pk):
    dr=reg.objects.get(id=pk)
    dr.delete()
    return redirect('view')
    
        