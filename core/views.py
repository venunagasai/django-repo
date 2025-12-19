from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def home(request):
    user = request.user
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        wish = "Good Morning"
    elif 12 <= hour < 18:
        wish = "Good Afternoon"
    else:
        wish = "Good Evening"

    # Specific logic for muralikrishna
    if user.username == "muralikrishna":
        greeting = "Hello Sir"
        tag = "(Owner of Abacus Insights)"
        display_name = "Murali Krishna" # Or from user object
    else:
        # Fallback for other users
        greeting = f"Hello {user.first_name if user.first_name else user.username}"
        tag = "Employee"
        display_name = user.first_name if user.first_name else user.username

    context = {
        "greeting": greeting,
        "wish": wish,
        "tag": tag,
        "display_name": display_name,
        "time": now.strftime("%H:%M"),
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")
