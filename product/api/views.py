# from rest_framework import viewsets
# from product.api.serializers import ProductSerializer
# from product.models import Product


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from product.models import Product
from product.api.serializers import ProductSerializer, LoginUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]



class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]



class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


from rest_framework.views import APIView


class LoginUserApiView(APIView):

    def post(self, request):
        # get user data
        data = request.data
        # check user data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid():
            # data is correct, create or get token : + return
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})

        else :
            return Response(serializer.errors, status=400)


class LogoutUserApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user

        token = Token.objects.get(user=user)
        token.delete()
        return Response({'message': 'Logged out successfully'})