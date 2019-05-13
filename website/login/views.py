from django.shortcuts import render
from django.contrib.auth.models

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth
