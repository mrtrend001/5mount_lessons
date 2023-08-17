from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from products.models import Product


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(instance=products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not Fount'},
                        status=status.HTTP_404_NOT_FOUND)

    data = ProductSerializer(instance=product, many=False).data
    return Response(data=data)


@api_view(['GET', 'POST'])
def test_api_view(request):
    dict_ = {
        'test': 'Hello World',
    }
    return Response(status=status.HTTP_200_OK,
                    data=dict_)
