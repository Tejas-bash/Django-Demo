from django.shortcuts import render
from django.views import View

class Newproject(View): 
    def get(self,request):
        context = { "Tejas":"Targhale","Age":25,}
        return render(request,'App/Demo.html',{'data': context})
        
    