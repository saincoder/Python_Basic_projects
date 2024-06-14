from rembg import remove
from PIL import Image

input_path = 'own.jpg'
out_put = 'output.png'

input_img = Image.open(input_path)
output_img = remove(input_img)
output_img.save(out_put)