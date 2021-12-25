import calendar
from datetime import date

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis.models import Restaurants


# Create your views here.

@csrf_protect
@api_view(['POST', ])
def open_res(request):
    try:
        rtype = request.data.get("type")
        if rtype is None:
            return Response("Enter a restaurant type")
        curr_date = date.today()
        today = calendar.day_name[curr_date.weekday()].lower()

        # model named Restaurants
        rlist = Restaurants.objects.filter(type = rtype)
        if rlist.exists():
            opened_list = []
            for r in rlist:
                if not r.hours[today]['is_closed']:  # is_closed = False
                    opened_list.append(r.name)
            return JsonResponse(opened_list, safe = False)
        else:
            return Response("Not an available type!")
    except Exception:
        return Response("Error!")
