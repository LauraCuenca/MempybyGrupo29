from PIL import Image

i = "acura-logo.png"
# My image is a 200x374 jpeg that is 102kb large
foo = Image.open(f"../recursos/datasets/images_logo/images/{i}")
print(foo.size)
# I downsize the image with an ANTIALIAS filter (gives the highest quality)
foo = foo.resize((120, 90), Image.ANTIALIAS)
foo.save(f"../recursos/datasets/images_logo/images/{i}", quality=95)
