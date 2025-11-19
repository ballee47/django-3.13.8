from django.shortcuts import render , redirect
from . models import Student , gamer 
from . forms import UserForm1
from django.contrib import messages
from book_1.decorators import custom_login_required , custom_login_admin , page_access_required



# Create your views here.
@page_access_required
def app1_fnc(request):
    return render(request,'app1/app1.html')


# def join123(request):
#     if request.method == "POST":
#         form = UserForm(request.POST or None)
#         if form.is_valid():
#              form.save()
#         else:

#             name = request.POST['name']
#             age = request.POST['age']
#             city = request.POST['city']
#             messages.success(request,('fill the form'))               
#             # return redirect('join')
#             return render(request,'book_1/join.html',{'name':name,'age':age,'city':city,})     
#         messages.success(request,('added succesfully'))               
#         return redirect('confirmation')
#     else:
#         form = UserForm()
#         return render(request, 'book_1/join.html',{})
    
    
def app1_fnc2(req):
    response1 = gamer.objects.all()
    return render(req,'app1/page2.html',{'response': response1})

        