from rest_framework.response import Response 
from rest_framework.views import APIView

class TestAPIView(APIView):
    def get(self, request):
        return Response({'get': 'get'})
    
    def post(self, request):
        return Response({'post': 'post'})
    
    def put(self, request):
        return Response({'put': 'put'})