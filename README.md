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

### Se selecciona el la tabla a la cual usaremos para la prediccion 📄

para esto jalamos los datos de la tabla movimiento para convertirla en un data frames

```python
Tabla_movimiento = "SELECT * FROM movimiento"
df_movimiento = pd.read_sql(Tabla_movimiento, db, )
df_movimiento
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Movimiento_Id</th>
      <th>dMovFecha</th>
      <th>nMovTipoMovimiento_Id</th>
      <th>nMovTipopago</th>
      <th>Almacen_Id</th>
      <th>nMovTipoOrigenDestino</th>
      <th>nMovOrigenDestino_Id</th>
      <th>nMovTipodestino</th>
      <th>Documento_Id</th>
      <th>sMovDocumento</th>
      <th>...</th>
      <th>dMovRetencion</th>
      <th>sMovObservacion</th>
      <th>nMovEstadoSunat</th>
      <th>nMovEstado</th>
      <th>nMovEliminado</th>
      <th>dMovFecha_Act</th>
      <th>Usuario_Id</th>
      <th>nMovClasificador_Id</th>
      <th>nMovMovimiento_Id</th>
      <th>nMovOrdenCampo_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>64</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: M4C-849 / T5Q-998</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-09-11 16:29:38</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:  ANU-925 / TCZ-988</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-09-11 16:54:44</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>91</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:  AFE-904 / TBK-978</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-09-11 17:12:46</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>99</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:  AUG-886 / M3P-989</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2018-09-11 17:18:12</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>100</td>
      <td>2</td>
      <td>1</td>
      <td>5</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:  D4D-796 / M3G-987</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2018-09-11 17:43:06</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>8055</td>
      <td>8058</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>71</td>
      <td>2</td>
      <td>1</td>
      <td>8011</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: APO-886/TDH-974</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-11-30 22:01:09</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8056</td>
      <td>8059</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>74</td>
      <td>2</td>
      <td>1</td>
      <td>8012</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T1E-940/T1C-997</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-11-30 22:43:11</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8057</td>
      <td>8060</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>28</td>
      <td>2</td>
      <td>1</td>
      <td>8013</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: ARC-728/TCW-988</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-11-30 22:46:00</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8058</td>
      <td>8061</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>17</td>
      <td>2</td>
      <td>1</td>
      <td>8014</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: A4W-928/T3Q-981</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-11-30 22:49:01</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8059</td>
      <td>8062</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>166</td>
      <td>2</td>
      <td>1</td>
      <td>8015</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: A3B-857/T2K-970</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-11-30 22:58:52</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>8060 rows × 30 columns</p>
</div>

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
