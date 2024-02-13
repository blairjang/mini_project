from django.shortcuts import render
from api import address
# Create your views here.
def index(request):
    # print(request.POST["address1"])
    # print(request.POST["address2"])
    data = address.search("서울시","마포구","웨딩메이크업")
    context = {
        "data" : data
    }


    return render(request, "index.html", context)
