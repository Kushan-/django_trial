
from django.urls import path, include, re_path

from dogs.views import csvQuery, catchQuery




urlpatterns = [
	path("/", csvQuery, name="count"),
    #path("?", catchQuery, name="count")
    re_path('$^', catchQuery, name="redirect_to_root"),

    
]
