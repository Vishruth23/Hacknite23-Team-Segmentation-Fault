from django.shortcuts import render, redirect
from django.http import HttpResponse
#from . import views
from . import overall_season_11
from . import playing11
from . import analysis2023

# Create your views here.

def home(request):
    if request.GET:
        return render(request,"bestXI.html")
    return render(request, "home.html")

def bestXI(request):
    if request.GET:
        if request.GET["team"]=="All Teams":
            data=overall_season_11.find_best_XI((request.GET["year"]))
            return render(request,"bestXI.html",context={"data":data[0], "year" : request.GET["year"], "team" : "All Teams","image1":data[1],"image2":data[2]})
        else:
            data = playing11.find_best_teamXI((request.GET["team"]), int(request.GET["year"]))
            return render(request, "bestXI.html", context = {"data":data[0], "year" : request.GET["year"], "team": request.GET["team"],"image1":data[1], "image2":data[2]})
    data=overall_season_11.find_best_XI("2022")
    return render(request,"bestXI.html",context={"data":data[0], "year": "2022", "team" : "All Teams","image1":data[1], "image2":data[2]})
 
def predictXI(request):
    eleven,eleven2=analysis2023.predictXI()
    return render(request,"predictXI.html",context={"data":eleven, "data1":eleven2}) 

    
    
