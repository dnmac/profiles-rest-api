from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    #Whenever you're sending a post put or patch request,
    #expect the variables set in HelloSerializer, i.e name.

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'USES HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manualled to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        #standard way to retrieve a serializer when working in an APIView.

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
            #returns all erros as a dictionary.

    def put(self, pk=None):
        """Handle updating an object"""
        #usually set pk(primary key) to an object with that pk,
        #which is to be updated.
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """"Handle a partial update of an object"""
        #i.e only updating the surname in a name object.
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        #Used to delete objects in database
        return Response({'method': 'DELETE'})