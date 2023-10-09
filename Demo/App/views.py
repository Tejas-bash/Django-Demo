from django.shortcuts import render
from django.views import View
from App.forms import demoForm

class Newproject(View): 
        
    def post(self,request):
        form = demoForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            form.save()
        return render(request,"App/Demo.html",{'form':form})
                
    def get(self,request):
        form = demoForm()
        return render(request,'App/Demo.html',{'form': form})