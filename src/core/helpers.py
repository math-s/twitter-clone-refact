import binascii
import datetime
import os
import random
import string
import sys
from io import BytesIO

from django.core.cache import cache
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from PIL import Image
from rest_framework_simplejwt.tokens import RefreshToken


def generate_key():
    return binascii.hexlify(os.urandom(25)).decode()


def resizeAndCropImage(uploadedImage, multiplier=1):
    dimension = 500
    name = {1: '', 2: '_medium', 3: '_low'}

    imgTemp = Image.open(uploadedImage)
    imgTemp = imgTemp.convert('RGB')
    outputIoStream = BytesIO()
    width, height = imgTemp.size
    smaller_edge = width if width < height else height

    #  crop edges
    left = (width - smaller_edge)/2
    top = (height - smaller_edge)/2
    right = (width + smaller_edge)/2
    bottom = (height + smaller_edge)/2

    imgTempCropped = imgTemp.crop((left, top, right, bottom))

    imgTmpResized = imgTempCropped.resize(
        (dimension, dimension), Image.ANTIALIAS
    )

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


def generateRandomStringOfSize(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def dateTimeDelayedByMinutes(minutes):
    expiring_datetime = timezone.now() + datetime.timedelta(minutes=30)
    return expiring_datetime


def generate_code(size, minutes, user):
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(size)).upper()
    cache.set(f'code{user.id}', code, 60*minutes)
    return code


def get_access_token_for_user(user):
    return RefreshToken.for_user(user).access_token
