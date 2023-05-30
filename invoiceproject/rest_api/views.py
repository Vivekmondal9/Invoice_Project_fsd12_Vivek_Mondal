from django.http import Http404,HttpResponseBadRequest,JsonResponse
from django.views import View
import json
from .serializer import RegisterSerializer

users=[{"firstName":"Vivek",
        "lastName":"Mondal",
        "email":"vivekmondal9@gmail.com",
        "phone":7980183902,
        "password":"vivekmondaL9@",
        "confirmPassword":"vivekmondaL9@"
        }]
class RegistrationView(View):
    def post(self,request):
        user_data=json.loads(request.body)
        user_data["user_id"]=len(users)+1

        user_serializer=RegisterSerializer(data=user_data)


        if (user_serializer.is_valid()):
            for user in users:
                if(user["email"]==user_serializer.data["email"]):
                    # raise Http404("User is Already Registered!!")
                    return HttpResponseBadRequest("User is already registered!!")
                
            users.append(user_data)
                
            
            return JsonResponse(users,safe=False,status=200)
        else:
            return HttpResponseBadRequest()
        
class LoginView(View):
    def post(self,request):
        user_data=json.loads(request.body)
        for index,item in enumerate(users):
            if (user_data["email"]==item["email"] and user_data["password"]==item["password"]):
                return JsonResponse("Login Successful",safe=False,status=200)
            else:
                raise Http404("Invalid Username Or Password!!")


    