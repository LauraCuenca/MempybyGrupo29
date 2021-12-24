# Juego de la memoria. Mempy -byGrupo29

<p align="center">
    <img  src="src/recursos/images/pikachu.gif" width="180" height="180">
</p>
Juego de la memoria, creado en python, tiene 3 niveles de dificultad, con distintos temarios para jugar dependiendo de la hora que quieras utilizarlo.

Permite elegir entre 3 gamas de colores: Dark, Light, G29.

Se realizo en el Seminario de Lenguajes, de la Facultad de Informatica UNLP

## Instalación

```
pip install -r requirements.txt
```


## Ejecutar el Juego

```
python run.py
```

## Licencia de los recursos

#### Sonidos

[click.wav](https://opengameart.org/content/menu-selection-click) CC-BY 3.0


#### Datos

[dataset pokemon](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types)

[dataset fifa](https://www.kaggle.com/balaaje/fifa-20-complete-player-dataset-for-manager-mode)

[dataset logo autos](https://www.kaggle.com/yamaerenay/100-images-of-top-50-car-brands)

#### Iconos

[flaticon.es](https://www.flaticon.es/packs/computer-programming/2?word=programming)


## Tabla de criterios

|Día  | Mañana - criterio  | Tarde - criterio |
|--|--|--|
| Lunes  | Pokemones tipo Grass y Poison | Pokemones tipo Normal y Volador |
| Martes | Pokemones tipo Bug y diferentes a Poison o Flying | Pokemones tipo Dragon y que no tengan segundo tipo |
| Miercoles | Pokemones que contengan la letra k en su nombre, que la longitud de su nombre sea mayor a 8 y que solo tengan 1 tipo | Pokemones que terminen su nombre en on |
| Jueves | Jugadores con imagen, pais==Argentina, edad entre 30 y 35 años que sean zurdos y pesen menos de 170lbs | Jugadores con imagen, edad menos a 18 años y jueguen de arquero |
| Viernes | Jugadores con imagen, edad==23, Overall==Potential y que sean zurdos | Jugadores con imagen, cuyos nombres sean mas de 18 caracteres y contengan las letras k,z y w |
| Sabado | Jugadores con imagen, edad menor a 25 y equipo barcelona | Jugadores con imagen, extranjeros jugando en Boca o River |
| Domingo | Logos con imagen, con origen distinto a estados unidos o reino unido | Logos con imagen, y segment igual a Mass-Market Cars |


## Tests

Para ejecutar los tests:

```python -m unittest discover```
