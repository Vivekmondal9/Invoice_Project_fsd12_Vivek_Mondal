from django.http import Http404,HttpResponseBadRequest,JsonResponse
from django.views import View
import json
from .serializer import RegisterSerializer

users=[]
class RegistrationView(View):
    def post(self,request):
        user_data=json.loads(request.body)
        user_data["user_id"]=len(users)+1

        user_serializer=RegisterSerializer(data=user_data)


        if (user_serializer.is_valid()):
            for user in users:
                if(user["Email"]==user_serializer.data["Email"]):
                    # raise Http404("User is Already Registered!!")
                    return HttpResponseBadRequest("User is already registered!!")
                
            users.append(user_data)
                
            
            return JsonResponse(users,safe=False,status=200)
        else:
            return HttpResponseBadRequest()
    