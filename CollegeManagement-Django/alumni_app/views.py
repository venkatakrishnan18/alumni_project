from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from .models import Event,JobNotification,Meeting

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

from .models import Feedback  # Assuming you have a Feedback model
from django.contrib import messages
def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']

        # Assuming you have a Feedback model, you can save the feedback like this
        feedback = Feedback(name=name, email=email, comments=comments)
        feedback.save()

        messages.success(request, 'Thank you for your feedback!')
        return redirect('feedback')  # Redirect to the feedback form page

    return render(request, 'feedback.html')

def contact_us(request):
    return render(request, 'contact_us.html')



from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import AlumniRegistrationForm
from .models import Registration 

def Register(request):  # Renamed the view function to avoid conflicts
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)

        if form.is_valid():
            # Save the form to create a new Registration instance
            form.save()

            # Redirect to a success page or do whatever you want
            return redirect('login_alumini')
    else:
        form = AlumniRegistrationForm()

    return render(request, 'Registration.html', {'form': form})


# registration

# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from .forms import RegistrationForm
# from .models import Registration 

# from django.contrib.auth import login, authenticate


# def Registration(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)

#         if form.is_valid():
#             # Create a new Registration object and populate it with the form data
#             registration = Registration(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 rollno=form.cleaned_data['rollno'],
#                 graduation_year=form.cleaned_data['graduation_year'],
#                 major=form.cleaned_data['major'],
#                 current_employer=form.cleaned_data['current_employer'],
#                 current_job_title=form.cleaned_data['current_job_title'],
#                 contact=form.cleaned_data['contact'],
#                 email=form.cleaned_data['email'],
#                 #username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#                 #confirm_password=form.cleaned_data['confirm_password'],
#             )

#             # Save the object to the database
#             registration.save()

#             # Redirect to a success page or do whatever you want
#             return redirect('login_alumini')
#     else:
#         form = RegistrationForm()

#     return render(request, 'Registration.html', {'form': form})


from .forms import CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

# Your existing CustomLoginForm remains unchanged

# def login_alumini(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             # Redirect to the home page or any desired URL name
#             # For example, replace 'home' with your home URL name
#             return redirect('home')  # Replace 'home' with your home URL name
#         else:
#             # If the form is invalid (incorrect credentials), render the login page with errors
#             return render(request, 'login_alumini.html', {'form': form})
#     else:
#         form = CustomLoginForm()

#     return render(request, 'login_alumini.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Registration
from django.contrib import messages

def login_alumini(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                instance = Registration.objects.get(email=email, password=password)
                request.session['user_id'] = instance.id  # Store user's ID in the session
                return redirect('alumni_dashboard')  # Redirect to the alumni dashboard
            except Registration.DoesNotExist:
                messages.error(request, "Invalid credentials. Please try again.")  # Set error message
    else:
        form = CustomLoginForm()
    return render(request, 'login_alumini.html', {'form': form})


from django.db.models import Count

def alumni_dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        instance = Registration.objects.get(id=user_id)
        event_count = Event.objects.count()
        meeting_count = Meeting.objects.count()
        job_notification_count = JobNotification.objects.count()

        context = {
            'instance': instance,
            'event_count': event_count,
            'meeting_count': meeting_count,
            'job_notification_count': job_notification_count
        }
        return render(request, 'alumni_dashboard.html', context)
    else:
        # Handle cases where the user ID is not found in the session
        return redirect('login_alumni')  # Redirect to the login page



def alumini_dashboard_index(request):
    context={}
    return render(request, 'alumini_dashboard_index', context)


def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            instance = Registration.objects.get(id=user_id)
            context = {'instance': instance}
            return render(request, 'profile.html', context)
        except Registration.DoesNotExist:
            # Handle the case where the user ID is not found or does not exist
            # You can redirect to an error page or login page
            return redirect('login_alumini')  # Redirect to the login page
    else:
        return redirect('login_alumini')  # Redirect to the login page



def events(request):
    events = Event.objects.all()  # Query to get all events
    context = {'events': events}
    return render(request, 'events.html', context)

def online_meetings(request):
    context = {}
    return render(request, 'online_meetings.html', context)

def update_profile(request):
    context={}
    return render(request, 'update_profile.html', context)

def job_notifications(request):
    jobs = JobNotification.objects.all()
    print("jobs:",jobs)  # Query to get all events
    context = {'jobs': jobs}
    return render(request, 'job_notification.html', context)

def online_meetings(request):
    Meetings = Meeting.objects.all()
    context = {'Meetings': Meetings}
    
    return render(request, 'online_meetings.html', context)
