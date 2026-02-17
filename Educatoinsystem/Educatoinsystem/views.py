# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm
# from .models import Profile

# from .forms import SignupForm

# def home_page(request):
#     return render(request, "home.html")

# def aboutus(request):
#     return render(request, "aboutus.html")

# def courses(request):
#     return render(request, "courses.html")

# def course_detail(request, course_id):
#     return HttpResponse(f"Details of Course ID: {course_id}")

# def register(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')   # after signup go to home
#     else:
#         form = SignupForm()

#     return render(request, "register.html", {'registrationform': form})
# def login_view(request):
#     error = None
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('details')
#         else:
#             error = "Invalid credentials"

#     return render(request, 'login.html', {'error': error})

# @login_required
# def details(request):
#     if Profile.objects.filter(user=request.user).exists():
#         return redirect('dashboard')

#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('dashboard')
#     else:
#         form = ProfileForm()

#     return render(request, 'details.html', {'form': form})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProfileForm
from .models import Profile


#  HOME PAGES -

def home_page(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def courses(request):
    return render(request, "courses.html")

def course_detail(request, course_id):
    return HttpResponse(f"Details of Course ID: {course_id}")


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # go to login after signup
    else:
        form = SignupForm()

    return render(request, "register.html", {'registrationform': form})


# Authentacication  system
# def login_view(request):
#     error = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('details')
#         else:
#             error = "Invalid username or password"

#     return render(request, 'login.html', {'error': error})
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('details')
        else:
            error = "Invalid username or password"

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('homepage')


# USER DETAILS 

# @login_required(login_url='login')
# def details(request):
#     # If details already filled, go to dashboard
#     if Profile.objects.filter(user=request.user).exists():
#         return redirect('dashboard')

#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('dashboard')
#     else:
#         form = ProfileForm()

#     return render(request, 'details.html', {'form': form})

@login_required(login_url='login')
def details(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        # Bind POST data to form
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'details.html', {
        'form': form,
        'profile': profile
    })



@login_required(login_url='login')
def dashboard(request):
    profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {'profile': profile})
