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

### Se comprueba si los datos estan limpios(Pre-Procesamiento) 🔩

ver cantidad de registros

```python
print (df_movimiento.shape) 
```
    (8060, 30)
    
ver los tipos de datos

```python
print (df_movimiento.info())
```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8060 entries, 0 to 8059
    Data columns (total 30 columns):
    Movimiento_Id            8060 non-null int64
    dMovFecha                8060 non-null object
    nMovTipoMovimiento_Id    8060 non-null int64
    nMovTipopago             8060 non-null int64
    Almacen_Id               8060 non-null int64
    nMovTipoOrigenDestino    8060 non-null int64
    nMovOrigenDestino_Id     8060 non-null int64
    nMovTipodestino          8060 non-null int64
    Documento_Id             8060 non-null int64
    sMovDocumento            8060 non-null object
    sMovDocReferencia        8060 non-null object
    Moneda_Id                8060 non-null int64
    nMovTipoCambio           8060 non-null float64
    nMovImporte              8060 non-null float64
    nMovIGV                  8060 non-null float64
    nMovTotal                8060 non-null float64
    nMovSaldo                8060 non-null float64
    nMovTotalCancelado       8060 non-null float64
    dMovDetraccion           8060 non-null float64
    dMovPercepcion           8060 non-null float64
    dMovRetencion            8060 non-null float64
    sMovObservacion          8060 non-null object
    nMovEstadoSunat          8060 non-null int64
    nMovEstado               8060 non-null int64
    nMovEliminado            8060 non-null int64
    dMovFecha_Act            8060 non-null datetime64[ns]
    Usuario_Id               8060 non-null int64
    nMovClasificador_Id      8060 non-null int64
    nMovMovimiento_Id        8060 non-null int64
    nMovOrdenCampo_Id        8060 non-null int64
    dtypes: datetime64[ns](1), float64(9), int64(16), object(4)
    memory usage: 1.8+ MB
    None

ver si hay datos nulos

```python
print (pd.isnull(df_movimiento).sum())
```
    Movimiento_Id            0
    dMovFecha                0
    nMovTipoMovimiento_Id    0
    nMovTipopago             0
    Almacen_Id               0
    nMovTipoOrigenDestino    0
    nMovOrigenDestino_Id     0
    nMovTipodestino          0
    Documento_Id             0
    sMovDocumento            0
    sMovDocReferencia        0
    Moneda_Id                0
    nMovTipoCambio           0
    nMovImporte              0
    nMovIGV                  0
    nMovTotal                0
    nMovSaldo                0
    nMovTotalCancelado       0
    dMovDetraccion           0
    dMovPercepcion           0
    dMovRetencion            0
    sMovObservacion          0
    nMovEstadoSunat          0
    nMovEstado               0
    nMovEliminado            0
    dMovFecha_Act            0
    Usuario_Id               0
    nMovClasificador_Id      0
    nMovMovimiento_Id        0
    nMovOrdenCampo_Id        0
    dtype: int64
ver estadísticas descriptivas que resumen la tendencia central, la dispersión y la forma de la distribución de un conjunto de datos.
```python
print (df_movimiento.describe())
```

           Movimiento_Id  nMovTipoMovimiento_Id  nMovTipopago  Almacen_Id  \
    count    8060.000000            8060.000000   8060.000000      8060.0   
    mean     4032.475434               1.999504      1.023945         1.0   
    std      2326.907957               0.031503      0.152889         0.0   
    min         1.000000               0.000000      1.000000         1.0   
    25%      2017.750000               2.000000      1.000000         1.0   
    50%      4032.500000               2.000000      1.000000         1.0   
    75%      6047.250000               2.000000      1.000000         1.0   
    max      8062.000000               2.000000      2.000000         1.0   
    
           nMovTipoOrigenDestino  nMovOrigenDestino_Id  nMovTipodestino  \
    count                 8060.0           8060.000000      8060.000000   
    mean                     2.0             70.913400         1.999752   
    std                      0.0             41.726762         0.015751   
    min                      2.0              0.000000         1.000000   
    25%                      2.0             39.000000         2.000000   
    50%                      2.0             66.000000         2.000000   
    75%                      2.0            105.000000         2.000000   
    max                      2.0            184.000000         2.000000   
    
           Documento_Id  Moneda_Id  nMovTipoCambio  ...  dMovDetraccion  \
    count   8060.000000     8060.0          8060.0  ...          8060.0   
    mean       1.022333        1.0             1.0  ...             0.0   
    std        0.298064        0.0             0.0  ...             0.0   
    min        1.000000        1.0             1.0  ...             0.0   
    25%        1.000000        1.0             1.0  ...             0.0   
    50%        1.000000        1.0             1.0  ...             0.0   
    75%        1.000000        1.0             1.0  ...             0.0   
    max        5.000000        1.0             1.0  ...             0.0   
    
           dMovPercepcion  dMovRetencion  nMovEstadoSunat   nMovEstado  \
    count          8060.0         8060.0      8060.000000  8060.000000   
    mean              0.0            0.0         2.983499     2.083499   
    std               0.0            0.0         0.281542     0.449567   
    min               0.0            0.0        -1.000000     0.000000   
    25%               0.0            0.0         3.000000     2.000000   
    50%               0.0            0.0         3.000000     2.000000   
    75%               0.0            0.0         3.000000     2.000000   
    max               0.0            0.0         4.000000     5.000000   
    
           nMovEliminado   Usuario_Id  nMovClasificador_Id  nMovMovimiento_Id  \
    count         8060.0  8060.000000               8060.0             8060.0   
    mean             0.0    21.772333                  0.0                0.0   
    std              0.0     5.487131                  0.0                0.0   
    min              0.0     9.000000                  0.0                0.0   
    25%              0.0    18.000000                  0.0                0.0   
    50%              0.0    20.000000                  0.0                0.0   
    75%              0.0    22.000000                  0.0                0.0   
    max              0.0    33.000000                  0.0                0.0   
    
           nMovOrdenCampo_Id  
    count             8060.0  
    mean                 0.0  
    std                  0.0  
    min                  0.0  
    25%                  0.0  
    50%                  0.0  
    75%                  0.0  
    max                  0.0
Al relizar una consulta para poder ver cuales cabezeras no contaban con detalle(era lo primero que pensaba enfocar el proyecto) me boto 2 fechas raras
```python
consulta1 = "select m.Movimiento_Id, dmovfecha, smovdocumento, documento_id, mdc.Movimiento_Id as id_mdc from movimiento m left join movimientodetalleconsumo mdc on m.movimiento_id= mdc.movimiento_id where documento_id <>5 and mdc.Movimiento_Id is null"
df_consulta1= pd.read_sql(consulta1, db, )
df_consulta1
```
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Movimiento_Id</th>
      <th>dmovfecha</th>
      <th>smovdocumento</th>
      <th>documento_id</th>
      <th>id_mdc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>326</td>
      <td>2018-09-14</td>
      <td>322</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>1</td>
      <td>491</td>
      <td>2018-09-15</td>
      <td>486</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>2</td>
      <td>566</td>
      <td>2018-09-16</td>
      <td>561</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>3</td>
      <td>737</td>
      <td>1969-12-31</td>
      <td></td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>4</td>
      <td>755</td>
      <td>2018-09-18</td>
      <td>747</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>5</td>
      <td>881</td>
      <td>2018-09-19</td>
      <td>872</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>6</td>
      <td>968</td>
      <td>1969-12-31</td>
      <td></td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>7</td>
      <td>1429</td>
      <td>2018-09-25</td>
      <td>1417</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1951</td>
      <td>2018-09-30</td>
      <td>1936</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>9</td>
      <td>2909</td>
      <td>2018-10-11</td>
      <td>2885</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>10</td>
      <td>3414</td>
      <td>2018-10-16</td>
      <td>3388</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>11</td>
      <td>6848</td>
      <td>2018-11-20</td>
      <td>6806</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>12</td>
      <td>7968</td>
      <td>2018-11-30</td>
      <td>7924</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>13</td>
      <td>7969</td>
      <td>2018-11-30</td>
      <td>7925</td>
      <td>1</td>
      <td>None</td>
    </tr>
    <tr>
      <td>14</td>
      <td>7984</td>
      <td>2018-11-30</td>
      <td>7937</td>
      <td>1</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>

Al momento de ordenar por fechas se encontro 2 fechas que eran de 1969-12-31 que al consultar sobre ellas me dijeron que esas 2 eran porque se habian registrado mal, asi que como eran las unicas pase a eliminarlas con:
```python
cursor.execute ("""delete from movimiento where movimiento.Movimiento_Id = 737""")
``` 
```python
cursor.execute ("""delete from movimiento where movimiento.Movimiento_Id = 968""")
```
Quedando ahora 8058 registro
```python
print (df_movimiento.shape) 
```
    (8058, 30)
    
### Dividimos los datos en datos para ENTRENAR, PROBAR y VALIDAR ⌨️

la base de datos cuenta con los datos desde el 11-09-2018 hasta el 30-11-2018(8058 Registros )

*Para entrenar se usaran los datos desde 11-09-2018 hasta 31-10-2018
```python
consulta4 = "SELECT * FROM `movimiento` where dMovFecha >='2018-09-11' and dMovFecha <='2018-10-31'"
df_train= pd.read_sql(consulta4, db, )
print (df_train.shape)
```
    (5004, 30)
    
*Para provar se usaran los datos desde 1-11-2018 hasta 15-11-2018
```python
consulta5 = "SELECT * FROM `movimiento` where dMovFecha >='2018-11-01' and dMovFecha <='2018-11-15'"
df_test= pd.read_sql(consulta5, db, )
print (df_test.shape)
```
    (1390, 30)
    
*Para validar se usaran los datos desde 16-11-2018 hasta 30-11-2018
```python
consulta6 = "SELECT * FROM `movimiento` where dMovFecha >='2018-11-16' and dMovFecha <='2018-11-30'"
df_vali= pd.read_sql(consulta6, db, )
print (df_vali.shape)
```
    (1664, 30)
    
## Despliegue 📦



## Construido con 🛠️

Librerias usadas

* [pandas](https://pandas.pydata.org/) 
* [pymysql](https://pypi.org/project/PyMySQL/) 
* [matplotlib.pyplot](https://matplotlib.org/)
* [numpy](https://numpy.org/)

🖇️

📖
📌

## Autor ✒️

* **Eduardo Garnique** - *Trabajo Inicial*, *Documentación* - [Eduardo Garnique](https://github.com/EduardoGarnique)


 📄

## Expresiones de Gratitud 🎁

⌨️ ❤️  😊
