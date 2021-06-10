import base64
import random
from .models import LinkyItem
from django.http import HttpResponse
from profanity_check import predict
URL_LENGTH = 7


def b64(num):
    # Converting decimal to base64
    num_bytes = base64.urlsafe_b64encode(num.encode('ascii'))
    return num_bytes.decode('ascii')


def generate_id():
    existing_id = LinkyItem.objects.all().values_list('id')
    cur_id = b64(str(random.randint(0, 64**URL_LENGTH)))[:URL_LENGTH+1]
    while cur_id in existing_id:
        cur_id = b64(str(random.randint(0, 64**URL_LENGTH)))[:URL_LENGTH+1]
    return cur_id


def get_custom_id(custom_id):
    existing_id = LinkyItem.objects.all().values_list('id')
    if custom_id in existing_id:
        return generate_id()
    if predict([custom_id])[0] == 1:
        return generate_id()
    return custom_id
