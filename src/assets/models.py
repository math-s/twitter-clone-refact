from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

import sys

# from uuid import uuid1
from io import BytesIO
from PIL import Image as ImagePIL

from core.helpers import resizeAndCropImage


class Image(models.Model):
    """
    Asset class to handle all images from the application
    """
    image_high_url = models.ImageField(
        'Image (high)', blank=False, null=False, upload_to='images'
    )
    image_medium_url = models.ImageField(
        'Image (medium)', blank=True, null=True, upload_to='images'
    )
    image_low_url = models.ImageField(
        'Image (low)', blank=True, null=True, upload_to='images'
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.image_high_url = resizeAndCropImage(
                self.image_high_url, multiplier=1
            )
            self.image_medium_url = resizeAndCropImage(
                self.image_high_url, multiplier=2
            )
            self.image_low_url = resizeAndCropImage(
                self.image_high_url, multiplier=3
            )
        super(Image, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage, multiplier=1):
        dimension = 500
        name = {1: '', 2: '_medium', 3: '_low'}

        imgTemp = ImagePIL.open(uploadedImage)
        outputIoStream = BytesIO()
        imgTmpResized = imgTemp.resize((dimension, dimension))
        imgTmpResized.save(
            outputIoStream, format='JPEG', quality=int(100/multiplier)
        )
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(
            outputIoStream,
            'ImageField',
            f"{uploadedImage.name.split('.')[0]}{name[multiplier]}.jpg",
            'image/jpeg',
            sys.getsizeof(outputIoStream), None
        )
        return uploadedImage
