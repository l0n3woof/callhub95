from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

import time

from fibo import fib_dict

class Fibresp(APIView):
    def get(self, request):
        start = time.time()
        num = request.query_params.get('num', None)
        try:
            number = fib_dict[int(num)]
        except:
            return Response({'result':'please enter a valid integer for calculation'})
        end = time.time()
        total = int(start) - int(end)
        return Response({'result':number, 'time_taken':(str(total) + ' seconds')})

