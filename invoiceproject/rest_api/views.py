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



items=[{
    "invoice_id":1,
    "client_name":"Vivek Mondal",
    "date":"Wed May 02 2023",
    "items":[{"desc":"This a very good Cosmetic Product.","quantity":5,"rate":500}]

}]           
class InvoiceList(View):
    def get(self,request):
        return JsonResponse(items,safe=False)   


class Itemadd(View):
    def post(self,request):
        item_detail=json.loads(request.body)
        item_detail["invoice_id"]=len(items)+1

        items.append(item_detail)

        return JsonResponse(items,safe=False)

class ItemwithId(View):
    def get(self,request,invoice_id):
        itemfound=None

        
        
        for item in items:
            if(item["invoice_id"]==invoice_id):
                itemfound=item
                break
        if itemfound:
            return JsonResponse(itemfound,safe=False,status=200)
        else:
            raise Http404("Item Not Found!!")    
               
            
class NewItemAdd(View):
    def post(self,request,invoice_id):
        data=json.loads(request.body)
        itemfound=None
        for item in items:
            if (item["invoice_id"]==invoice_id):
                itemfound=item
                break
        if itemfound:    
            # itemfound.=len(itemfound)+1
            itemfound["items"].append(data)
            
            return JsonResponse(itemfound,safe=False)
        else:
            raise Http404()

                
               


    