from django.shortcuts import render,redirect

# Create your views here.
def login_view(request):
	if request.method=="POST":
		username=request.POST.get('username')
		request.session('username',username)
		return redirect('profile')
	return render(request,"login.html")


def profile(request):
	username=request.session.get('username')
	if not username:
		return redirect('login')

	role='Admin' if username=="Venu" else "Employee"
	return render(request,"profile.html",{"username":username,"role":role})

def about(request):
	return render(request,"about.html")

def logout_view(request):
	request.session.flush()
	return redirect("login")