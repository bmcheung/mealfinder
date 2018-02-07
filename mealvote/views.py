from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from .forms import UserForm

# Create your views here.

def home(request):
    return HttpResponse("hello")

class Home(View):
    # main page that directs users to rooms and log in

    def get(self, request):
        form = UserForm()
        return render(request, "mealvote/index.html", {"form": form})

    def post(self, request):
        form_type = request.POST["extra"]
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if form_type == '0':
                # register a new user
                try:
                    user = User.objects.create_user(username = data['username'], password = data['password'])
                    if user is not None:
                        login(request, user)
                        return redirect(reverse('mealvote:dashboard'))
                except:
                    messages.add_message(request, messages.ERROR, 'Username must be unique.')
            elif form_type == '1':
                # log in to user
                user = authenticate(username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return redirect(reverse('mealvote:dashboard'))
                else:
                    messages.add_message(request, messages.ERROR, 'Username or password is incorrect')
        # elif form_type == '2':
        #     # join a room as a guest

        else:
            return redirect('/')

class Dashboard(View):
    # displays once user logs in, allowing user to edit profile, manage current rooms, or create a room

    def get(self, request):
        return render(request, "mealvote/dashboard.html")
