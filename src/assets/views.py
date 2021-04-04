from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from assets.models import Image
from assets.serializers import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    """
    Upload promotion images
    """
    queryset = Image.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = ImageSerializer
