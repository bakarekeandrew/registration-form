from django.shortcuts import render, redirect
from .forms import ApplyForm
from django.contrib import messages

def apply(request): 
    # we create an instance of the form so we can pass it to the template
    if request.method == "POST":
        # if the request is a POST request then save data
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application was created successfully.")
            return redirect("/apply/")
    else:
        # if the request sent by the user if not a post request, return a normall form
        form = ApplyForm() 
        return render(request, "index.html", {'form':form}) 
        # {} this bracket is not neccesary


# /admin/