from PIL import Image


img = """https://www.carlogos.org/car-logos/toyota-logo.png
https://www.carlogos.org/car-logos/honda-logo.png
https://www.carlogos.org/car-logos/chevrolet-logo.png
https://www.carlogos.org/car-logos/ford-logo.png
https://www.carlogos.org/car-logos/mercedes-benz-logo.png
https://www.carlogos.org/car-logos/jeep-logo.png
https://www.carlogos.org/car-logos/bmw-logo.png
https://www.carlogos.org/car-logos/porsche-logo.png
https://www.carlogos.org/car-logos/subaru-logo.png
https://www.carlogos.org/car-logos/nissan-logo.png
https://www.carlogos.org/car-logos/cadillac-logo.png
https://www.carlogos.org/car-logos/volkswagen-logo.png
https://www.carlogos.org/car-logos/lexus-logo.png
https://www.carlogos.org/car-logos/audi-logo.png
https://www.carlogos.org/car-logos/ferrari-logo.png
https://www.carlogos.org/car-logos/volvo-logo.png
https://www.carlogos.org/car-logos/jaguar-logo.png
https://www.carlogos.org/car-logos/gmc-logo.png
https://www.carlogos.org/car-logos/buick-logo.png
https://www.carlogos.org/car-logos/acura-logo.png
https://www.carlogos.org/car-logos/bentley-logo.png
https://www.carlogos.org/car-logos/dodge-logo.png
https://www.carlogos.org/car-logos/hyundai-logo.png
https://www.carlogos.org/car-logos/lincoln-logo.png
https://www.carlogos.org/car-logos/mazda-logo.png
https://www.carlogos.org/car-logos/land-rover-logo.png
https://www.carlogos.org/car-logos/tesla-logo.png
https://www.carlogos.org/car-logos/ram-logo.png
https://www.carlogos.org/car-logos/kia-logo.png
https://www.carlogos.org/car-logos/chrysler-logo.png
https://www.carlogos.org/car-logos/pontiac-logo.png
https://www.carlogos.org/car-logos/infiniti-logo.png
https://www.carlogos.org/car-logos/mitsubishi-logo.png
https://www.carlogos.org/car-logos/oldsmobile-logo.png
https://www.carlogos.org/car-logos/maserati-logo.png
https://www.carlogos.org/car-logos/aston-martin-logo.png
https://www.carlogos.org/car-logos/bugatti-logo.png
https://www.carlogos.org/car-logos/fiat-logo.png
https://www.carlogos.org/car-logos/mini-logo.png
https://www.carlogos.org/car-logos/alfa-romeo-logo.png
https://www.carlogos.org/car-logos/saab-logo.png
https://www.carlogos.org/car-logos/genesis-logo.png
https://www.carlogos.org/car-logos/suzuki-logo.png
https://www.carlogos.org/car-logos/studebaker-logo.png
https://www.carlogos.org/car-logos/renault-logo.png
https://www.carlogos.org/car-logos/peugeot-logo.png
https://www.carlogos.org/car-logos/daewoo-logo.png
https://www.carlogos.org/car-logos/hudson-logo.png
https://www.carlogos.org/car-logos/citroen-logo.png
https://www.carlogos.org/car-logos/mg-logo.png"""

img = img.split()
for i in img:
# My image is a 240x180 png
    foo = Image.open(f"../recursos/datasets/images_logo/images/{i.split('/')[4]}")
    # print(foo.size)
    # I downsize the image with an ANTIALIAS filter (gives the highest quality)
    foo = foo.resize((120, 90), Image.ANTIALIAS)
    foo.save(f"../recursos/datasets/images_logo/images/{i.split('/')[4]}", quality=95)
