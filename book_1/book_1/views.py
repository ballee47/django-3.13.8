from django.shortcuts import render ,redirect , HttpResponse
from ch_1.models import web_user
from ch_1.forms import  UserForm2
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db import models
from .decorators import custom_login_required , custom_login_admin , page_access_required





# home page


def home1(request):
    return render(request,'book_1/mainapp1.html')


 # login page

def login1(request):     
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #  Try Django's built-in auth first
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username} (Django user)!")
            return redirect('home')

        #  Try your custom model next
        try:
            custom_user = web_user.objects.get(username=username)
            # compare password (plain or hashed)
            if custom_user.password == password or check_password(password, custom_user.password):
                # manually create session
                request.session['custom_user_id'] = custom_user.id
                request.session['custom_username'] = custom_user.username
                messages.success(request, f"Welcome, {custom_user.username} (Custom user)!")
                return redirect('loggedin')
            else:
                messages.error(request, "Incorrect password.")
        except Exception as e:
                  print(e)

    return render(request, 'book_1/login.html')


    
           
def logout1(request):
    django_logout(request)
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect('home')



def loggedin(request):
    return render(request,'book_1/mainappLogedin.html' , )








#join page

def join1234(request):
     if request.method == "POST":
        form = UserCreationForm()
        context = {'form': form}
        return render (request, 'book_1/join2.html', context)



def join12345(request):
    if request.method == "POST":
        form = UserForm2(request.POST, request.FILES)
        datae= {'form':form}
        if form.is_valid():
            saved_object = form.save()
            request.session['saved_id'] = saved_object.id
            messages.success(request, 'Added successfully!')
            return redirect('confirmation1')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserForm2()

    return render(request, 'book_1/join.html', {'form': form})
  

#crud
     

     
# def data2a(request,successForm):
#     result1 = {
#         'name': 'bilal ali'
#     }
#     return render(request,'book_1/success.html',result1)



def data3(request):
    saved_id = request.session.get('saved_id')
    saved_obj = None
    if saved_id:
        saved_obj = get_object_or_404(web_user, id=saved_id)

    return render(request, 'book_1/confirmation.html', {'saved_obj': saved_obj})

    
def list_gamer(request):
    webusers = web_user.objects.all()
    return render(request, 'book_1/list.html' , {'webuser': webusers})


def update_gamer(request, id):
    gmr = get_object_or_404(web_user, id=id)
    if request.method == "POST":
        # form= {'form':form}
        form = UserForm2(request.POST, request.FILES, instance=gmr)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('list_gamers')
    else:
        form = UserForm2(instance=gmr)
    return render(request, 'book_1/update.html', {'form': form})



def delete_gamer(request, id):
    gmr = get_object_or_404(web_user, id=id)
    if request.method == "POST":
        gmr.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('list_gamers')
    return render(request, 'book_1/delete.html', {'gmr': gmr})



def play_cod(request ,):
    return HttpResponse("this the cod gaming room")    


def view_profile(request):
    user = request.user if request.user.is_authenticated else None
    if not user and request.session.get('custom_user_id'):
        user = web_user.objects.filter(id=request.session['custom_user_id']).first()
    
    if not user:
        messages.warning(request, "Please log in to view your profile.")
        return redirect('loginpage')

    # Handle updates
    if request.method == 'POST':
        editable_fields = [
            f.name for f in user._meta.fields
            if f.name not in ('id', 'password', 'last_login', 'date_joined', 'is_staff', 'is_superuser')
            and not isinstance(f, (models.DateField, models.DateTimeField))
        ]
        for field in editable_fields:
            new_value = request.POST.get(field)
            if new_value is not None:
                setattr(user, field, new_value)
        user.save()
        messages.success(request, "✅ Profile updated successfully!")
        return redirect('home')
    # Prepare display data
    user_details = {
        f.name: getattr(user, f.name) for f in user._meta.fields
        
    }

    return render(request, 'book_1/profile.html', {'user_details': user_details})







#the page2 working

ALL_GAMES = {
    'adventure': {
        'godofwar': {'id': 89, 'title': 'God of War', 'desc': 'Greek mythology action game' ,'rating': 7.2},
        'lastofus': {'id': 96, 'title': 'The Last of Us', 'desc': 'Emotional adventure','rating': 7.9},
    },
    'action': {
        'residentevil': {'id': 65, 'title': 'Resident Evil', 'desc': 'Zombie survival horror','rating': 6.2},
        'uncharted': {'id': 77, 'title': 'Uncharted', 'desc': 'Treasure hunting action', 'rating': 7.6},
    },
    'racing': {
        'needforspeed': {'id': 22, 'title': 'Need for Speed', 'desc': 'High-speed racing','rating': 6.2},
        'forza': {'id': 33, 'title': 'Forza Horizon', 'desc': 'Open world racing experience','rating': 6.2},
    },
}



def get_game_by_id(game_id):
    for cat, games in ALL_GAMES.items():
        for name, info in games.items():
            if info['id'] == game_id:
                return {**info, 'category': cat, 'name': name}
    return None


@page_access_required
def page2(request):
    categories = ALL_GAMES.keys()
    return render(request, 'book_1/page2.html', {'categories': categories})

# 2️⃣ Show games in selected category
def page2_category(request, category):
    games = ALL_GAMES.get(category, {})
   # Choose template based on category
    # if category == 'adventure':
    #     template = 'book_1/adventure.html'
    # elif category == 'action':
    #     template = 'book_1/action.html'
    # elif category == 'racing':
    #     template = 'book_1/racing.html'
    # else:
    #     template = 'book_1/category.html'
    return render(request, 'book_1/category.html', {'category': category, 'games': games})

# 3️⃣ Show game details
def page2_detail(request, category, id, names):
    game = ALL_GAMES.get(category, {}).get(names)

    if category not in ALL_GAMES:
        return render(request, 'book_1/404.html', status=404)
        # raise Http404("Category not found.")

    # Get game
    game = ALL_GAMES[category].get(names)

    # Check if game exists
    if not game or game['id'] != id:
        return render(request, 'book_1/404.html', status=404)
        # raise Http404("Game not found.")

    context = {
        'id': id,
        'category': category,
        'title': game.get('title'),
        'desc': game.get('desc'),
        'rating': game.get('rating'),
    }

    return render(request, 'book_1/detail.html', context)
