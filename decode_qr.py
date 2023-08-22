from pyzbar.pyzbar import decode
from PIL import Image
import base64
from io import BytesIO


def decode_qr_from_base64(base64_string):
    try:
        # Convert base64 string to bytes
        image_data = base64.b64decode(base64_string)

        # Create a PIL Image object
        image = Image.open(BytesIO(image_data))

        # Decode QR codes from the image
        decoded_objects = decode(image)

        if decoded_objects:
            qr_data = decoded_objects[0].data.decode('utf-8')
            return qr_data
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None