# Proyecto de analisis de datos

Este proyecto es creo con la finalidad de hacer un analisis de datos en la base de datos del sistema hormiguita 

## Comenzando 🚀

Se utilizo una maquina virtual para alojar todo lo que utilizaremos 


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Maquina virtual
iso Ubuntu Server 18.04
```

### Instalación 🔧

[Video de Instalacion](https://youtu.be/-dgNj3HRzyc)

[Lista de comandos usados](https://drive.google.com/file/d/1QtP3Sm6ZB1hYIHcEJa3v_uyW1PSPchEM/view)

## Ejecutando el analisis ⚙️

### Se comprueba si los datos estan limpios 🔩

ver cantidad de registros

```
print (df_movimiento.shape)
```
ver los tipos de datos

```
print (df_movimiento.info())
```
ver si hay datos nulos

```
print (pd.isnull(df_movimiento).sum())
```

### Dividimos los datos en datos para ENTRENAR, PROBAR y VALIDAR ⌨️

la base de datos cuenta con los datos desde el 11-09-2018 hasta el 30-11-2018(8060 Registros )

*Para entrenar se usaran los datos desde 11-09-2018 hasta 31-10-2018
```
Da un ejemplo
```
*Para entrenar se usaran los datos desde 1-11-2018 hasta 15-11-2018
```
Da un ejemplo
```
*Para entrenar se usaran los datos desde 16-11-2018 hasta 30-11-2018
```
Da un ejemplo
```
## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
