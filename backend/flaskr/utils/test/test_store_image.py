import os
import sys
sys.path.append(os.path.join('..'))

import store_image
import base64


with open('test.jpg', 'rb') as data:
    s = base64.b64encode(data.read())

b_s = s.decode('utf-8')
print(b_s)

store_image.store_base64_to_image(b_s, is_source=True)
