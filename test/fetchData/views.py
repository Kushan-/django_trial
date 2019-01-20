from django.http import HttpResponse
from django.shortcuts import render
from .models import DogsData

import pandas as pd
print(pd.__version__)

import os
print(os.getcwd()+"/dogs.csv")

df = pd.read_csv(os.getcwd()+"/dogs.csv", skiprows=1)

#df = pd.read_csv("../dogs.csv", skiprows=1)
#print(df)
# Create your views here.

def home_view(request, *args, **kwargs):
	print(request.user)
	return HttpResponse("<h1>yo</h1>")


def csvQuery(request, *args, **kwargs):
	print(request.user)
	return HttpResponse(df)


def catchQuery(request, *args, **kwargs):
	print(request.GET)
	print(DogsData)
	dogsData = DogsData.objects.all() 
	print(len(dogsData))
	for data in dogsData:
		print(data)
	
	for key, val in request.GET.items():
		print(key)
		print(val)
		#queryStr += '(dataset['+key+']=='+val+')&'
	#print(queryStr[:-1])
	#data = df[queryStr[:-1]]

	return HttpResponse("done")

	# def product_list_view(request, *args, **kwargs):
	# 	queryset = DogsData.objects.all()
	# 	context = {
	# 		"objects_list" : queryset
	# 	}

	# 	return render()

'''
 "GET /count?dog_name=Buddy HTTP/1.1" 404 2194
Not Found: /count
[11/Jan/2019 01:28:28] "GET /count?dog_name=Buddy HTTP/1.1" 404 2194
Not Found: /count
[11/Jan/2019 01:28:28] "GET /count?gender=m&borough=brooklyn&spayed_or_neutered=no HTTP/1.1" 404 2235
Not Found: /count
[11/Jan/2019 01:28:28] "GET /count?gender=f&dominant_color=brindle HTTP/1.1" 404 2215
Not Found: /count
[11/Jan/2019 01:28:28] "GET /count?foo=x&bar=y&baz=z HTTP/1.1" 404 2205
'''