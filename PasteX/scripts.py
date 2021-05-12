import base64


def b64(num):
    # Converting decimal to base64
    num_bytes = base64.urlsafe_b64encode(num.encode('ascii'))
    return num_bytes.decode('ascii')
