import requests

"Herramienta para descargar las imagenes que se usan en el dataset"

i = ['https://cdn.sofifa.com/players/158/023/20_120.png', 'https://cdn.sofifa.com/players/183/898/20_120.png',
     'https://cdn.sofifa.com/players/184/144/20_120.png', 'https://cdn.sofifa.com/players/212/541/20_120.png',
     'https://cdn.sofifa.com/players/170/719/20_120.png', 'https://cdn.sofifa.com/players/206/152/20_120.png',
     'https://cdn.sofifa.com/players/199/940/20_120.png', 'https://cdn.sofifa.com/players/172/019/20_120.png',
     'https://cdn.sofifa.com/players/188/791/20_120.png', 'https://cdn.sofifa.com/players/202/069/20_120.png',
     'https://cdn.sofifa.com/players/226/797/20_120.png', 'https://cdn.sofifa.com/players/178/565/20_120.png',
     'https://cdn.sofifa.com/players/186/745/20_120.png', 'https://cdn.sofifa.com/players/186/550/20_120.png',
     'https://cdn.sofifa.com/players/235/451/20_120.png', 'https://cdn.sofifa.com/players/179/698/20_120.png',
     'https://cdn.sofifa.com/players/165/515/20_120.png', 'https://cdn.sofifa.com/players/252/179/20_120.png',
     'https://cdn.sofifa.com/players/242/879/20_120.png', 'https://cdn.sofifa.com/players/245/865/20_120.png',
     'https://cdn.sofifa.com/players/255/485/20_120.png', 'https://cdn.sofifa.com/players/253/497/20_120.png',
     'https://cdn.sofifa.com/players/253/028/20_120.png', 'https://cdn.sofifa.com/players/251/752/20_120.png',
     'https://cdn.sofifa.com/players/245/787/20_120.png', 'https://cdn.sofifa.com/players/255/303/20_120.png',
     'https://cdn.sofifa.com/players/254/300/20_120.png', 'https://cdn.sofifa.com/players/253/291/20_120.png',
     'https://cdn.sofifa.com/players/243/585/20_120.png', 'https://cdn.sofifa.com/players/250/753/20_120.png',
     'https://cdn.sofifa.com/players/248/478/20_120.png', 'https://cdn.sofifa.com/players/254/580/20_120.png',
     'https://cdn.sofifa.com/players/252/552/20_120.png', 'https://cdn.sofifa.com/players/255/151/20_120.png',
     'https://cdn.sofifa.com/players/244/483/20_120.png', 'https://cdn.sofifa.com/players/248/329/20_120.png',
     'https://cdn.sofifa.com/players/254/502/20_120.png', 'https://cdn.sofifa.com/players/255/811/20_120.png',
     'https://cdn.sofifa.com/players/255/301/20_120.png', 'https://cdn.sofifa.com/players/255/433/20_120.png',
     'https://cdn.sofifa.com/players/255/989/20_120.png', 'https://cdn.sofifa.com/players/255/991/20_120.png',
     'https://cdn.sofifa.com/players/243/294/20_120.png', 'https://cdn.sofifa.com/players/253/371/20_120.png',
     'https://cdn.sofifa.com/players/247/020/20_120.png', 'https://cdn.sofifa.com/players/254/468/20_120.png',
     'https://cdn.sofifa.com/players/252/583/20_120.png', 'https://cdn.sofifa.com/players/252/160/20_120.png',
     'https://cdn.sofifa.com/players/255/266/20_120.png', 'https://cdn.sofifa.com/players/256/045/20_120.png',
     'https://cdn.sofifa.com/players/252/789/20_120.png', 'https://cdn.sofifa.com/players/251/815/20_120.png',
     'https://cdn.sofifa.com/players/252/406/20_120.png', 'https://cdn.sofifa.com/players/247/033/20_120.png',
     'https://cdn.sofifa.com/players/255/498/20_120.png', 'https://cdn.sofifa.com/players/250/804/20_120.png',
     'https://cdn.sofifa.com/players/253/398/20_120.png', 'https://cdn.sofifa.com/players/255/713/20_120.png',
     'https://cdn.sofifa.com/players/255/976/20_120.png', 'https://cdn.sofifa.com/players/239/594/20_120.png',
     'https://cdn.sofifa.com/players/247/839/20_120.png', 'https://cdn.sofifa.com/players/256/315/20_120.png',
     'https://cdn.sofifa.com/players/254/550/20_120.png', 'https://cdn.sofifa.com/players/254/079/20_120.png',
     'https://cdn.sofifa.com/players/252/420/20_120.png', 'https://cdn.sofifa.com/players/255/563/20_120.png',
     'https://cdn.sofifa.com/players/247/164/20_120.png', 'https://cdn.sofifa.com/players/252/839/20_120.png',
     'https://cdn.sofifa.com/players/255/423/20_120.png', 'https://cdn.sofifa.com/players/245/991/20_120.png',
     'https://cdn.sofifa.com/players/253/171/20_120.png', 'https://cdn.sofifa.com/players/250/930/20_120.png',
     'https://cdn.sofifa.com/players/248/683/20_120.png', 'https://cdn.sofifa.com/players/252/783/20_120.png',
     'https://cdn.sofifa.com/players/243/060/20_120.png', 'https://cdn.sofifa.com/players/246/648/20_120.png',
     'https://cdn.sofifa.com/players/252/838/20_120.png', 'https://cdn.sofifa.com/players/243/685/20_120.png',
     'https://cdn.sofifa.com/players/256/234/20_120.png', 'https://cdn.sofifa.com/players/252/151/20_120.png',
     'https://cdn.sofifa.com/players/248/182/20_120.png', 'https://cdn.sofifa.com/players/230/269/20_120.png',
     'https://cdn.sofifa.com/players/230/453/20_120.png', 'https://cdn.sofifa.com/players/230/165/20_120.png',
     'https://cdn.sofifa.com/players/230/468/20_120.png', 'https://cdn.sofifa.com/players/230/341/20_120.png',
     'https://cdn.sofifa.com/players/230/381/20_120.png', 'https://cdn.sofifa.com/players/230/487/20_120.png',
     'https://cdn.sofifa.com/players/230/420/20_120.png', 'https://cdn.sofifa.com/players/230/330/20_120.png',
     'https://cdn.sofifa.com/players/230/353/20_120.png', 'https://cdn.sofifa.com/players/236/075/20_120.png',
     'https://cdn.sofifa.com/players/230/231/20_120.png', 'https://cdn.sofifa.com/players/230/319/20_120.png',
     'https://cdn.sofifa.com/players/230/333/20_120.png', 'https://cdn.sofifa.com/players/230/181/20_120.png',
     'https://cdn.sofifa.com/players/236/071/20_120.png', 'https://cdn.sofifa.com/players/230/292/20_120.png',
     'https://cdn.sofifa.com/players/230/386/20_120.png', 'https://cdn.sofifa.com/players/230/387/20_120.png',
     'https://cdn.sofifa.com/players/230/472/20_120.png', 'https://cdn.sofifa.com/players/230/506/20_120.png',
     'https://cdn.sofifa.com/players/230/190/20_120.png', 'https://cdn.sofifa.com/players/234/004/20_120.png',
     'https://cdn.sofifa.com/players/234/022/20_120.png', 'https://cdn.sofifa.com/players/236/072/20_120.png',
     'https://cdn.sofifa.com/players/230/210/20_120.png', 'https://cdn.sofifa.com/players/236/074/20_120.png',
     'https://cdn.sofifa.com/players/230/214/20_120.png', 'https://cdn.sofifa.com/players/230/471/20_120.png',
     'https://cdn.sofifa.com/players/230/261/20_120.png', 'https://cdn.sofifa.com/players/236/192/20_120.png',
     'https://cdn.sofifa.com/players/230/264/20_120.png', 'https://cdn.sofifa.com/players/197/242/20_120.png',
     'https://cdn.sofifa.com/players/162/280/20_120.png', 'https://cdn.sofifa.com/players/210/333/20_120.png',
     'https://cdn.sofifa.com/players/215/502/20_120.png', 'https://cdn.sofifa.com/players/164/994/20_120.png',
     'https://cdn.sofifa.com/players/184/457/20_120.png', 'https://cdn.sofifa.com/players/219/496/20_120.png',
     'https://cdn.sofifa.com/players/212/138/20_120.png', 'https://cdn.sofifa.com/players/201/114/20_120.png',
     'https://cdn.sofifa.com/players/213/949/20_120.png', 'https://cdn.sofifa.com/players/252/675/20_120.png',
     'https://cdn.sofifa.com/players/243/497/20_120.png', 'https://cdn.sofifa.com/players/216/449/20_120.png',
     'https://cdn.sofifa.com/players/234/747/20_120.png', 'https://cdn.sofifa.com/players/224/962/20_120.png',
     'https://cdn.sofifa.com/players/238/775/20_120.png', 'https://cdn.sofifa.com/players/222/164/20_120.png',
     'https://cdn.sofifa.com/players/231/535/20_120.png', 'https://cdn.sofifa.com/players/256/460/20_120.png',
     'https://cdn.sofifa.com/players/243/185/20_120.png', 'https://cdn.sofifa.com/players/242/512/20_120.png',
     'https://cdn.sofifa.com/players/251/500/20_120.png', 'https://cdn.sofifa.com/players/223/305/20_120.png',
     'https://cdn.sofifa.com/players/211/290/20_120.png', 'https://cdn.sofifa.com/players/185/187/20_120.png',
     'https://cdn.sofifa.com/players/247/073/20_120.png', 'https://cdn.sofifa.com/players/230/698/20_120.png',
     'https://cdn.sofifa.com/players/229/706/20_120.png', 'https://cdn.sofifa.com/players/245/465/20_120.png',
     'https://cdn.sofifa.com/players/244/018/20_120.png', 'https://cdn.sofifa.com/players/241/480/20_120.png',
     'https://cdn.sofifa.com/players/252/509/20_120.png', 'https://cdn.sofifa.com/players/252/222/20_120.png',
     'https://cdn.sofifa.com/players/228/702/20_120.png', 'https://cdn.sofifa.com/players/220/440/20_120.png',
     'https://cdn.sofifa.com/players/230/658/20_120.png', 'https://cdn.sofifa.com/players/231/443/20_120.png',
     'https://cdn.sofifa.com/players/241/184/20_120.png', 'https://cdn.sofifa.com/players/253/004/20_120.png',
     'https://cdn.sofifa.com/players/242/816/20_120.png', 'https://cdn.sofifa.com/players/229/337/20_120.png',
     'https://cdn.sofifa.com/players/240/683/20_120.png', 'https://cdn.sofifa.com/players/230/800/20_120.png',
     'https://cdn.sofifa.com/players/237/823/20_120.png', 'https://cdn.sofifa.com/players/226/103/20_120.png',
     'https://cdn.sofifa.com/players/253/163/20_120.png', 'https://cdn.sofifa.com/players/242/999/20_120.png',
     'https://cdn.sofifa.com/players/246/139/20_120.png', 'https://cdn.sofifa.com/players/241/810/20_120.png',
     'https://cdn.sofifa.com/players/237/522/20_120.png', 'https://cdn.sofifa.com/players/239/247/20_120.png',
     'https://cdn.sofifa.com/players/210/513/20_120.png', 'https://cdn.sofifa.com/players/220/883/20_120.png',
     'https://cdn.sofifa.com/players/214/040/20_120.png', 'https://cdn.sofifa.com/players/240/699/20_120.png',
     'https://cdn.sofifa.com/players/220/334/20_120.png', 'https://cdn.sofifa.com/players/246/914/20_120.png',
     'https://cdn.sofifa.com/players/220/332/20_120.png', 'https://cdn.sofifa.com/players/220/337/20_120.png',
     'https://cdn.sofifa.com/players/233/959/20_120.png', 'https://cdn.sofifa.com/players/214/436/20_120.png',
     'https://cdn.sofifa.com/players/187/132/20_120.png', 'https://cdn.sofifa.com/players/242/267/20_120.png',
     'https://cdn.sofifa.com/players/225/964/20_120.png', 'https://cdn.sofifa.com/players/213/974/20_120.png',
     'https://cdn.sofifa.com/players/245/149/20_120.png', 'https://cdn.sofifa.com/players/214/606/20_120.png',
     'https://cdn.sofifa.com/players/246/690/20_120.png', 'https://cdn.sofifa.com/players/227/549/20_120.png']

i = """https://www.carlogos.org/car-logos/toyota-logo.png
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

#print(len(i))
for a in i:
    r = requests.get(a, allow_redirects=True)
    open(f'../recursos/datasets/images_fifa/images/{(a.split("/")[4])}-{(a.split("/")[5])}-20_60.png', 'wb').write(
        r.content)
