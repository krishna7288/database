from django.shortcuts import render,redirect
from .forms import RegisterDataForm,upload
from django.contrib import messages
from .models import Register,File
from django.contrib.auth.models import User
#from models import new


# Create your views here..




def home(request):
  return render(request,"home.html")


def database(request):
    data = Register.objects.all()
    files = File.objects.all()
    if data:                                                     
        return render(request, "database.html", {'data': data, 'files': files})        
    else:
        return render(request, "database.html")    
                                                    

\
def register(request):
    if request.method == 'POST':
          username=request.POST["username"]
          email=request.POST["email"]
          password1=request.POST["password1"]
          password2=request.POST["password2"]
          if password1==password2:    
            user=User.objects.create_user(username=username, email=email, password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created! You are now able to log in.')
            return redirect('login')
          else: 
            messages.warning(request,'Password mismatch! Please try again.') 
            return redirect('register')
    else:          
          form=RegisterDataForm()       
          return render(request,"register.html",{'form':form}) 
  
  
def delete(request,id):
  data=Register.objects.get(id=id)
  data.delete()
  messages.error(request,"Delete Successfully completed")
  return redirect('database')

          
 
def update(request,id):
  data=Register.objects.get(id=id)
  if request.method=="POST":
    name=request.POST['name']
    age=request.POST['age']
    address=request.POST['address']
    mail=request.POST['mail']
    data.name=name  
    data.age=age
    data.address=address
    data.mail=mail
    data.save()
    messages.success(request,"update successfully completed")
    return redirect("database")
  return render(request,"update.html",{'data':data})

def uploadFile(request):
    if request.method == 'POST':
        form1 = upload(request.POST,request.FILES)                
        if form1.is_valid():
            form1.save()
            messages.success(request,"Upload successfully completed")
            return redirect("database")
            # Redirect to success page
    else:
        form1 = upload()
    return render(request, 'upload.html', {'form1': form1})   
  
 

      
               
              
     
