import base64
from io import BytesIO
from PIL import Image

def store_base64_to_image(data, is_source, is_video=False):
    image_data = base64.b64decode(data)
    image = Image.open(BytesIO(image_data))
    if is_video:
        image.save('facefusion/video_source.png')
    else:
        if is_source:
            image.save('facefusion/source.png')
        else:
            image.save('facefusion/target.png')
