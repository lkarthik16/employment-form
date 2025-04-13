from django.shortcuts import render, redirect
from .forms import EmploymentFormForm

def home(request):
    return render(request, 'home.html')

def employment_form(request):
    if request.method == 'POST':
        form = EmploymentFormForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page
    else:
        form = EmploymentFormForm()

    return render(request, 'employment_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')