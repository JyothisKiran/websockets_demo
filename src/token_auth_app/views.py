from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

# @api_view(["POST"])
# def loginView(request, *args, **kwargs):
# 	username = request.POST.get("username")
# 	password = request.POST.get("password")
# 	password = make_password(password)
# 	print(username, password)
# 	try:
# 		user = authenticate(username=username, password=password)
# 		print(user)
# 		# print('hi')
# 		# for user in User.objects.all():
# 		# 	print(user.username)
# 		# user = User.objects.filter(username=username)
# 		# print("user",user)
# 	except Exception as e:
# 		print('exception',e.__cause__())
# 		user = None
# 	if not user:
# 		return Response({
# 			"user_not_found": "There is no user \
# 			with this username and password !"
# 		})
# 	token = Token.objects.get_or_create(user=user)
# 	print(token[0])
# 	return Response(data={
# 		"token": token[0], "success":True
# 	})

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(["POST"])
def loginView(request, *args, **kwargs):
    username = request.POST.get("username")
    password = request.POST.get("password")

    try:
        user = authenticate(request, username=username, password=password)
    except Exception as e:
        print('exception', e)
        user = None

    if not user:
        return Response({
            "user_not_found": "There is no user with this username and password!"
        })

    token, created = Token.objects.get_or_create(user=user)
    print(token.key)

    return Response(data={
        "token": token.key,
        "success": True
    })


def loginViewPage(request):
	return render(request, 'chat/testing.html')
