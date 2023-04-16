from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name = "home"),
    path('bestXI',views.bestXI,name="bestXI"),
    path("predictXI",views.predictXI,name="predictXI")
]