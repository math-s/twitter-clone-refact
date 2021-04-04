from rest_framework import serializers
from assets.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'pk', 'image_high_url', 'image_medium_url', 'image_low_url'
        )
