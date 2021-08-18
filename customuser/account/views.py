from django.shortcuts import render
from django.http import HttpResponseRedirect
from account.forms import SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            gender = form.cleaned_data["gender"]
            dateofbirth = form.cleaned_data["dateofbirth"]
            password = form.cleaned_data["password"]
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, phone=phone, gender=gender, dateofbirth=dateofbirth)
            user.save()
            return HttpResponseRedirect('signup')

    else:
        form = SignUpForm()
        return render(request, 'account/index.html', {'form':form})
