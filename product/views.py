from hmac import digest
from unicodedata import digit
from rest_framework.decorators import api_view
from product.models import Product, Category
from rest_framework.response import Response
import json

# GET, POST, PUT, PATCH, DELETE

@api_view(['POST'])
def create_product(request):
    data = request.data

    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    is_available = data.get('is_available') == "true"
    image = data.get('image')

    category = data.get('category')

    if name is None or description is None or price is None or stock is None or is_available is None or image is None:
        return Response(data = {"error": "All fields are required"}, status=400)

    try:
        price = float(price)
    except Exception as e:
        return Response(data = {"error": "Price must be a number"}, status=400)

    try:
        stock = float(stock)
    except Exception as e:
        return Response(data = {"error": "Price must be a number"}, status=400)


    try:
        category = Category.objects.get(pk=category)
    except Exception as e:
        return Response(data = {"error": "Category not found"}, status=400)

    product = Product.objects.create(
        name = name,
        description = description,
        price = price,
        stock = stock,
        is_available = is_available,
        image = image,
        category = category
    )

    response_data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "is_available": product.is_available,
        "image": product.image.url,
        "category": {
            "id": product.category.id,
            "name": product.category.name,
        },
        "updated_at": product.updated_at,
        "created_at": product.created_at
    }
    
    return Response(data = response_data, status=201)

@api_view(['GET'])
def get_product(request):
    products = Product.objects.all()

    response_data = []

    for product in products:
        response_data.append({
            "id": product.id,
            "name": product.name,
        })
    return Response(data = response_data, status=200)

@api_view(['GET'])
def get_product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    response_data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "is_available": product.is_available,
        "image": product.image.url if product.image else None,
        "category": {
            "id": product.category.id if product.category else None,
            "name": product.category.name if product.category else None,
        },
        "updated_at": product.updated_at,
        "created_at": product.created_at
    }
    return Response(data = response_data, status=200)

@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = request.data
    
    product.name = data.get('name')
    product.description = data.get('description')
    product.price = data.get('price')
    product.stock = data.get('stock')
    product.is_available = data.get('is_available') == "true"
    product.save()

    response_data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "is_available": product.is_available,
        "image": product.image.url if product.image else None,
        "updated_at": product.updated_at,
        "created_at": product.created_at
    }
    return Response(data = response_data, status=200)

@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response(status=200)