import base64
import random
from .models import LinkyItem
URL_LENGTH = 7
def b64(num):
    # Converting decimal to base64
    num_bytes = base64.urlsafe_b64encode(num.encode('ascii'))
    return num_bytes.decode('ascii')

def generate_id():
    existing_id = LinkyItem.objects.all().values_list('id')
    cur_id = b64(str(random.randint(0,64**URL_LENGTH)))[:URL_LENGTH+1]
    while cur_id in existing_id:
        cur_id = b64(str(random.randint(0,64**URL_LENGTH)))[:URL_LENGTH+1]
    return cur_id