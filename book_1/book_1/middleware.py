from django.shortcuts import redirect, render



class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # If user is trying to access /admin/
        if request.path.startswith("/admin/"):

            # Allow only Django admin users
            if not request.user.is_authenticated:
                context = {"error_message": "You are not authorized to access the admin panel."}
                return render(request, "book_1/404.html", context)

            if not request.user.is_staff:
                context = {"error_message": "You are not authorized to access the admin panel."}
                return render(request, "book_1/404.html", context)

        return self.get_response(request)
