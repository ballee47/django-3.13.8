from django.shortcuts import redirect , render
from django.contrib import messages

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):


        # Allow custom session users
        if request.session.get('custom_user_id'):
            return view_func(request, *args, **kwargs)

        # Otherwise deny access
        messages.warning(request, "Please login to continue.")
        errors = ["Guest users cannot access this page", "Please login first"]
        return render(request, 'book_1/404.html', {'errors': errors})

    return wrapper



def custom_login_admin(view_func):
    def wrapper(request, *args, **kwargs):

        # Allow Django authenticated users
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)

        # Otherwise deny access
        messages.warning(request, "Please login to continue.")
        errors = ["Guest users cannot access this page", "Please login first"]
        return render(request, 'book_1/404.html', {'errors': errors})


    return wrapper





def page_access_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated or request.session.get('custom_user_id'):
            return view_func(request, *args, **kwargs)

        # Guest user
        messages.warning(request, "You are not allowed to access this page")
        errors = ["Guest users cannot access this page", "Please login first"]
        return render(request, 'book_1/404.html', {'errors': errors})

    return wrapper