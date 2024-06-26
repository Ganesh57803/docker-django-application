from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.
def registerPage(request):
    form = CustomUserCreationForm


    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        form.instance.is_staff=True
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, "registration/register.html", context)