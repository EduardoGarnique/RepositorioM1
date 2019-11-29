## Conexion a base de datos


```python
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```


```python
db = pymysql.connect("localhost","darkted","upaom1","hormigui")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : {0}".format(data))
```

    Database version : ('5.7.28-0ubuntu0.18.04.4',)


## Convertir tablas en DataFrames ##


```python
Tabla_activo = "SELECT * FROM activo"
df_activo = pd.read_sql(Tabla_activo, db, )
df_activo
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
      <th>Activo_Id</th>
      <th>sActDescripcion</th>
      <th>nActEstado</th>
      <th>nActEliminado</th>
      <th>dActFecha_Act</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>N/A</td>
      <td>0</td>
      <td>0</td>
      <td>2015-10-12</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_almc = "SELECT * FROM almacen"
df_almc = pd.read_sql(Tabla_almc, db, )
df_almc
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
      <th>Almacen_Id</th>
      <th>sAlmNombre</th>
      <th>sAlmUbicacion</th>
      <th>nAlmEstado</th>
      <th>nAlmEliminado</th>
      <th>dAlmFecha_Act</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>PACASMAYO</td>
      <td>PACASMAYO</td>
      <td>1</td>
      <td>0</td>
      <td>2018-05-12</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_bitacorausuario = "SELECT * FROM bitacorausuario"
df_bitacorausuario = pd.read_sql(Tabla_bitacorausuario, db, )
df_bitacorausuario
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
      <th>nBiusuTipoModulo</th>
      <th>nBiusuUsuario_Id</th>
      <th>dBiusuFechaHora</th>
      <th>sBiusuDescripcion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>2019-03-19 23:28:32</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2019-03-19 23:52:13</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>2019-03-20 00:02:30</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1</td>
      <td>33</td>
      <td>2019-03-20 00:02:54</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1</td>
      <td>33</td>
      <td>2019-03-20 00:06:41</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>2846</td>
      <td>1</td>
      <td>44</td>
      <td>2019-11-16 11:00:18</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>2847</td>
      <td>1</td>
      <td>39</td>
      <td>2019-11-16 11:16:33</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>2848</td>
      <td>1</td>
      <td>39</td>
      <td>2019-11-16 12:02:38</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>2849</td>
      <td>1</td>
      <td>39</td>
      <td>2019-11-16 12:22:41</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
    <tr>
      <td>2850</td>
      <td>1</td>
      <td>39</td>
      <td>2019-11-16 13:28:01</td>
      <td>Cerro SessiÃ³n</td>
    </tr>
  </tbody>
</table>
<p>2851 rows × 4 columns</p>
</div>




```python
Tabla_clasificador = "SELECT * FROM clasificador"
df_clasificador = pd.read_sql(Tabla_clasificador, db, )
df_clasificador
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
      <th>Clasificador_Id</th>
      <th>sClaDescripcion</th>
      <th>nClaEliminado</th>
      <th>dClaFecha_Act</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>N/A</td>
      <td>0</td>
      <td>2015-11-02</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_conceptofijo = "SELECT * FROM conceptofijo"
df_conceptofijo = pd.read_sql(Tabla_conceptofijo, db, )
df_conceptofijo
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
      <th>Concepto_Id</th>
      <th>sConNombre</th>
      <th>nConValor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>IGV</td>
      <td>18.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_cotizacion = "SELECT * FROM cotizacion"
df_cotizacion = pd.read_sql(Tabla_cotizacion, db, )
df_cotizacion
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
      <th>Cotizacion_Id</th>
      <th>dCotFecha</th>
      <th>Documento_Id</th>
      <th>sCotDocSerie</th>
      <th>sCotDocNumero</th>
      <th>nCotTipoOrigenDestino</th>
      <th>nCotOrigenDestino_Id</th>
      <th>nCotTipodestino</th>
      <th>Moneda_Id</th>
      <th>nCotTipopago</th>
      <th>dCotDiasCredito</th>
      <th>sCotDocumentoReferencia</th>
      <th>nCotEstado</th>
      <th>dCotFecha_Act</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
Tabla_cotizaciondetalle = "SELECT * FROM cotizaciondetalle"
df_cotizaciondetalle = pd.read_sql(Tabla_cotizaciondetalle, db, )
df_cotizaciondetalle
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
      <th>Cotizaciondetalle_Id</th>
      <th>ExoneradoIGV</th>
      <th>UndMedida_Id</th>
      <th>sCotUndMedidaAlias</th>
      <th>dCotPrecioUnitario</th>
      <th>nCotCantidad</th>
      <th>Usuario_Id</th>
      <th>dCotFecha_Act</th>
      <th>Cotizacion_Id</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
Tabla_documento = "SELECT * FROM documento"
df_documento = pd.read_sql(Tabla_documento, db, )
df_documento
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
      <th>Documento_Id</th>
      <th>sDocCodigoSunat</th>
      <th>Almacen_Id</th>
      <th>nDocTipoMovimiento_Id</th>
      <th>sDocNombre</th>
      <th>sDocNombreCorto</th>
      <th>nDocNomAutomatico</th>
      <th>sDocSiguiente</th>
      <th>nDocAfectoIGV</th>
      <th>nDocEstado</th>
      <th>isFE</th>
      <th>nDocEliminado</th>
      <th>dDocFecha_Act</th>
      <th>Usuario_Id</th>
      <th>nDocTipoImprimir</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td></td>
      <td>1</td>
      <td>2</td>
      <td>FACTURA ELECTRONICA</td>
      <td>F001</td>
      <td>1</td>
      <td>43500</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2019-04-24 14:14:56</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td></td>
      <td>1</td>
      <td>2</td>
      <td>BOLETA VENTA ELECTRONICA</td>
      <td>B001</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2019-04-24 14:15:16</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>FACTURA</td>
      <td>FT</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2016-03-31 17:58:56</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>BOLETA VENTA</td>
      <td>BV</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2015-10-12 13:04:14</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td></td>
      <td>0</td>
      <td>0</td>
      <td>ANULACION</td>
      <td>ANUL</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2015-10-12 13:05:03</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td></td>
      <td>0</td>
      <td>0</td>
      <td>ACTUALIZACION</td>
      <td>ACT</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2015-10-12 13:08:27</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td></td>
      <td>1</td>
      <td>2</td>
      <td>NOTA DE VENTA</td>
      <td>NV</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2017-08-22 11:30:32</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td></td>
      <td>1</td>
      <td>3</td>
      <td>NOTA DE INGRESO</td>
      <td>NI</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2018-06-04 19:34:40</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>NOTA DE COMPRA</td>
      <td>NC</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2017-08-22 11:29:28</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td></td>
      <td>1</td>
      <td>4</td>
      <td>NOTA DE SALIDA</td>
      <td>NS</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2018-06-04 19:34:59</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>11</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>NOTA DE CREDITO</td>
      <td>F100</td>
      <td>1</td>
      <td>17</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-11 00:00:00</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>11</td>
      <td>12</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>NOTA DE CREDITO BOLETA</td>
      <td>B100</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2019-04-29 00:00:00</td>
      <td>2</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_familia = "SELECT * FROM familia"
df_familia = pd.read_sql(Tabla_familia, db, )
df_familia
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
      <th>Familia_Id</th>
      <th>sFamCodigo</th>
      <th>sFamDescripcion</th>
      <th>nFamPadre</th>
      <th>nFamTipo</th>
      <th>nFamEstado</th>
      <th>nFamEliminado</th>
      <th>dFamFecha_Act</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td></td>
      <td>FAMILIAS</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-05-12</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>PRODUCTOS</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2018-05-12</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>SERVICIOS</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>2018-05-12</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_moneda = "SELECT * FROM moneda"
df_moneda = pd.read_sql(Tabla_moneda, db, )
df_moneda
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
      <th>Moneda_Id</th>
      <th>sMonDescripcion</th>
      <th>sMonAlias</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>Soles</td>
      <td>S/</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>Dolares</td>
      <td>US$</td>
    </tr>
  </tbody>
</table>
</div>




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




```python
df_movimiento.groupby('nMovEstadoSunat')['Movimiento_Id'].plot(kind='line',legend='prueba')
```




    nMovEstadoSunat
    -1    AxesSubplot(0.125,0.125;0.775x0.755)
     0    AxesSubplot(0.125,0.125;0.775x0.755)
     1    AxesSubplot(0.125,0.125;0.775x0.755)
     2    AxesSubplot(0.125,0.125;0.775x0.755)
     3    AxesSubplot(0.125,0.125;0.775x0.755)
     4    AxesSubplot(0.125,0.125;0.775x0.755)
    Name: Movimiento_Id, dtype: object




![png](output_15_1.png)



```python
df_movimiento.groupby(df_movimiento.Usuario_Id).plot(kind='scatter',x='Usuario_Id',y='nMovEstadoSunat',color='red')
```




    Usuario_Id
    9     AxesSubplot(0.125,0.125;0.775x0.755)
    17    AxesSubplot(0.125,0.125;0.775x0.755)
    18    AxesSubplot(0.125,0.125;0.775x0.755)
    19    AxesSubplot(0.125,0.125;0.775x0.755)
    20    AxesSubplot(0.125,0.125;0.775x0.755)
    21    AxesSubplot(0.125,0.125;0.775x0.755)
    22    AxesSubplot(0.125,0.125;0.775x0.755)
    23    AxesSubplot(0.125,0.125;0.775x0.755)
    24    AxesSubplot(0.125,0.125;0.775x0.755)
    32    AxesSubplot(0.125,0.125;0.775x0.755)
    33    AxesSubplot(0.125,0.125;0.775x0.755)
    dtype: object




![png](output_16_1.png)



![png](output_16_2.png)



![png](output_16_3.png)



![png](output_16_4.png)



![png](output_16_5.png)



![png](output_16_6.png)



![png](output_16_7.png)



![png](output_16_8.png)



![png](output_16_9.png)



![png](output_16_10.png)



![png](output_16_11.png)



```python
Tabla_movidet = "SELECT * FROM movimientodetalle"
df_movidet = pd.read_sql(Tabla_movidet, db, )
df_movidet
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
      <th>Mmovimientodetalle_Id</th>
      <th>Movimiento_Id</th>
      <th>ProductoLote_Id</th>
      <th>nMovDetUnidad_Id</th>
      <th>nMovDetCantidad</th>
      <th>nMovDetPrecioLista</th>
      <th>nMovDetPorcDescuento1</th>
      <th>nMovDetPorcDecuento2</th>
      <th>nMovDetPrecioUnitario</th>
      <th>nMovDetImporte</th>
      <th>nMovDetPrecioFlete</th>
      <th>nMovDetSaldoAnteriorLote</th>
      <th>nMovDetSaldoPosteriorLote</th>
      <th>nMovDetSaldoAnterior</th>
      <th>nMovDetSaldoPosterior</th>
      <th>nMovDetIncluyeIGV</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
Tabla_movimientodetalleconsumo = "SELECT * FROM movimientodetalleconsumo"
df_movimientodetalleconsumo = pd.read_sql(Tabla_movimientodetalleconsumo, db, )
df_movimientodetalleconsumo
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
      <th>Movimientodetalleconsumo_Id</th>
      <th>Movimiento_Id</th>
      <th>Producto_Id</th>
      <th>nMovDetConUnidad_Id</th>
      <th>sMovDetConCantidad</th>
      <th>nMovDetConPrecioLista</th>
      <th>nMovDetConPorcDescuento1</th>
      <th>nMovDetConPorcDescuento2</th>
      <th>nMovDetConPrecioUnitario</th>
      <th>nMovDetConImporte</th>
      <th>nMovDetConPrecioFlete</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>2</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>6</td>
      <td>3</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>7</td>
      <td>4</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>8</td>
      <td>5</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
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
    </tr>
    <tr>
      <td>8008</td>
      <td>8013</td>
      <td>8058</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8009</td>
      <td>8014</td>
      <td>8059</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8010</td>
      <td>8015</td>
      <td>8060</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8011</td>
      <td>8016</td>
      <td>8061</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8012</td>
      <td>8017</td>
      <td>8062</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>8013 rows × 11 columns</p>
</div>




```python
Tabla_origendestino = "SELECT * FROM origendestino"
df_origendestino = pd.read_sql(Tabla_origendestino, db, )
df_origendestino
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
      <th>OrigenDestino_Id</th>
      <th>nODTipo</th>
      <th>sODRucDni</th>
      <th>sODNombre</th>
      <th>sODNombreComercial</th>
      <th>sODDireccion</th>
      <th>sODTelefono</th>
      <th>sODCorreo</th>
      <th>sODContacto</th>
      <th>nODDiasCredito</th>
      <th>nODEstado</th>
      <th>nProcliDepId</th>
      <th>nProcliDepName</th>
      <th>nProcliProvId</th>
      <th>nProcliProvName</th>
      <th>nProcliDistId</th>
      <th>nProcliDistName</th>
      <th>dODFechaActualizacion</th>
      <th>nODUsuario_Id</th>
      <th>nODEliminado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>20601095310</td>
      <td>INNOVEK SAC.</td>
      <td>INNOVEK SAC.</td>
      <td>Av. Enrique Valenzuela 459 - Pacasmayo</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>05</td>
      <td>PACASMAYO</td>
      <td>06</td>
      <td>PACASMAYO</td>
      <td>2018-09-07 16:35:03</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>20419387658</td>
      <td>CEMENTOS PACASMAYO S.A.A.</td>
      <td>CEMENTOS PACASMAYO S.A.A.</td>
      <td>Panamericana Norte Km. 666 - Pacasmayo -  La L...</td>
      <td>n/a</td>
      <td>facturacion.innovek@gmail.com</td>
      <td>n/a</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>05</td>
      <td>PACASMAYO</td>
      <td>06</td>
      <td>PACASMAYO</td>
      <td>2018-11-30 08:41:34</td>
      <td>22</td>
      <td>0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>20480582561</td>
      <td>TRANSPORTES PAKATNAMU SAC.</td>
      <td>TRANSPORTES PAKATNAMU SAC.</td>
      <td>CAR.CARRETERA A LAMBAYEQUE MZA. A LOTE. 6 (CAR...</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0</td>
      <td>1</td>
      <td>13</td>
      <td>LAMBAYEQUE</td>
      <td>03</td>
      <td>LAMBAYEQUE</td>
      <td>01</td>
      <td>LAMBAYEQUE</td>
      <td>2018-09-07 17:03:04</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>20440120149</td>
      <td>JJ CANCINO S.R.L.</td>
      <td>JJ CANCINO S.R.L.</td>
      <td>CAL.SILVA SANTISTEBAN NRO. 394 LA LIBERTAD - P...</td>
      <td>n/a</td>
      <td>heinny.ct@jjcancino.com</td>
      <td>n/a</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>05</td>
      <td>PACASMAYO</td>
      <td>06</td>
      <td>PACASMAYO</td>
      <td>2018-10-15 14:00:00</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>10192277740</td>
      <td>PAZ CUEVA LEONARDO SALOMON</td>
      <td>PAZ CUEVA LEONARDO SALOMON</td>
      <td>-AV.Antonio Raimondy #595 Pacasmayo</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>05</td>
      <td>PACASMAYO</td>
      <td>06</td>
      <td>PACASMAYO</td>
      <td>2018-09-07 16:42:05</td>
      <td>9</td>
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
    </tr>
    <tr>
      <td>214</td>
      <td>216</td>
      <td>2</td>
      <td>20479753793</td>
      <td>TRANSPORTES TERAN HERMANOS S.R.L</td>
      <td>TRANSPORTES TERAN HERMANOS S.R.L</td>
      <td>AV.CIRCUNVALACION NÂ° 570 AMAZONAS DE LA PECA ...</td>
      <td>980361144</td>
      <td>NO</td>
      <td>NO</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>05</td>
      <td>PACASMAYO</td>
      <td>06</td>
      <td>PACASMAYO</td>
      <td>2019-09-14 02:29:16</td>
      <td>44</td>
      <td>0</td>
    </tr>
    <tr>
      <td>215</td>
      <td>217</td>
      <td>2</td>
      <td>20559700682</td>
      <td>CARGO TURISMO SERVIS CRUZ DE CHALPON E.I.R.L</td>
      <td>CARGO TURISMO SERVIS CRUZ DE CHALPON E.I.R.L</td>
      <td>CALCAYETANO HEREDIA NÂ° 12 BBRS</td>
      <td>958567691</td>
      <td>n/a</td>
      <td>JOSE ABANTO</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>05</td>
      <td>PACASMAYO</td>
      <td>06</td>
      <td>PACASMAYO</td>
      <td>2019-10-01 23:40:00</td>
      <td>39</td>
      <td>0</td>
    </tr>
    <tr>
      <td>216</td>
      <td>218</td>
      <td>2</td>
      <td>20600915852</td>
      <td>COMERCIO Y NEGOCIOS ANITA EMPRESA INDIVIDUAL ...</td>
      <td>COMERCIO Y NEGOCIOS ANITA EMPRESA INDIVIDUAL ...</td>
      <td>MZA. B LOTE. 16 URB. NOR ORIENTE (FRENTE A EMP...</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>ARISTERES</td>
      <td>0</td>
      <td>1</td>
      <td>13</td>
      <td>LAMBAYEQUE</td>
      <td>01</td>
      <td>CHICLAYO</td>
      <td>01</td>
      <td>CHICLAYO</td>
      <td>2019-11-09 00:53:31</td>
      <td>44</td>
      <td>0</td>
    </tr>
    <tr>
      <td>217</td>
      <td>219</td>
      <td>2</td>
      <td>20601345898</td>
      <td>DISTRIBUIDORA CHOTANITO J &amp; J E.I.R.L.</td>
      <td>DISTRIBUIDORA CHOTANITO J &amp; J E.I.R.L.</td>
      <td>AV. AUGUSTO B LEGUIA NRO. 1598 URB. SAN LORENZ...</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>JOSE</td>
      <td>0</td>
      <td>1</td>
      <td>13</td>
      <td>LAMBAYEQUE</td>
      <td>01</td>
      <td>CHICLAYO</td>
      <td>01</td>
      <td>CHICLAYO</td>
      <td>2019-11-12 02:30:21</td>
      <td>44</td>
      <td>0</td>
    </tr>
    <tr>
      <td>218</td>
      <td>220</td>
      <td>2</td>
      <td>20481784132</td>
      <td>SAN RAMON SAC</td>
      <td>SAN RAMON SAC</td>
      <td>CAL.JUAN CORRAL 992 URB. EL BOSQUE TRUJILLO</td>
      <td>959671101</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>LA LIBERTAD</td>
      <td>01</td>
      <td>TRUJILLO</td>
      <td>01</td>
      <td>TRUJILLO</td>
      <td>2019-11-12 23:16:25</td>
      <td>39</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>219 rows × 20 columns</p>
</div>




```python
Tabla_pago = "SELECT * FROM pago"
df_pago = pd.read_sql(Tabla_pago, db, )
df_pago
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
      <th>Pago_Id</th>
      <th>Movimiento_Id</th>
      <th>dPagFecha</th>
      <th>nPagTipoPago_Id</th>
      <th>sPagDocumento</th>
      <th>nPagImporte</th>
      <th>nPagLetra_Id</th>
      <th>dPagFecha_Act</th>
      <th>nPagUsuario_Id</th>
      <th>nPagEliminado</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
Tabla_parametros = "SELECT * FROM parametros"
df_parametros = pd.read_sql(Tabla_parametros, db, )
df_parametros
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
      <th>Parametro_Id</th>
      <th>sParDescripcion</th>
      <th>sParValor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>Tiempo de conexiÃ³n Activa|(Minutos)</td>
      <td>15</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>Valor del IGV| (Impuesto General a las Ventas)</td>
      <td>18</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>Movimiento por Defecto | Compra/Venta/Ingreso/...</td>
      <td>VENTA|2</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>Destino por Defecto| Bienes / Servicios</td>
      <td>SERVICIOS|2</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>Observaciones movimientos</td>
      <td>PLACA:</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>DetracciÃ³n|%</td>
      <td>12</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>Tipo de Pago por defecto| Contado=1/Credito=2</td>
      <td>CONTADO|1</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>Tipo de Documento por defecto| FACTURA/BOLETA/...</td>
      <td>FACTURA ELECTRONICA|1</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>Envio automatico|Si=1,No=0</td>
      <td>Si|1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_personal = "SELECT * FROM personal"
df_personal = pd.read_sql(Tabla_personal, db, )
df_personal
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
      <th>Personal_Id</th>
      <th>sPerApePaterno</th>
      <th>sPerApeMaterno</th>
      <th>sPerNombres</th>
      <th>sPerDNI</th>
      <th>sPerCargo</th>
      <th>nPerEliminado</th>
      <th>nPerEstado</th>
      <th>dPerFecha_Act</th>
      <th>nPerUsuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>COTRINA</td>
      <td>OYARSE</td>
      <td>SANTIAGO</td>
      <td>27041613</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:31:43</td>
      <td>9</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>OCÃ“N</td>
      <td>GRADOS</td>
      <td>JUAN</td>
      <td>43096162</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:32:45</td>
      <td>9</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>ARIAS</td>
      <td>SUAREZ</td>
      <td>ALEXANDER</td>
      <td>45532219</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:34:06</td>
      <td>9</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>MANTILLA</td>
      <td>QUISPE</td>
      <td>JAIME</td>
      <td>28073751</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:34:38</td>
      <td>9</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>CONTRINA</td>
      <td>CACHI</td>
      <td>MANUEL</td>
      <td>47813932</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:35:05</td>
      <td>9</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>OCON</td>
      <td>GRADOS</td>
      <td>JULIO</td>
      <td>80229171</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:35:52</td>
      <td>9</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>REYES</td>
      <td>DIAZ</td>
      <td>ROGGER</td>
      <td>42991000</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:36:24</td>
      <td>9</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>HERNANDEZ</td>
      <td>HILARIO</td>
      <td>JOSE</td>
      <td>19189429</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:37:16</td>
      <td>9</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>ABANTO</td>
      <td>OLIVA</td>
      <td>CARLOS</td>
      <td>80542424</td>
      <td>ENCARPADOR</td>
      <td>1</td>
      <td>1</td>
      <td>2019-06-24 18:37:58</td>
      <td>9</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>REYES</td>
      <td>DIAZ</td>
      <td>ROBERTO</td>
      <td>46159637</td>
      <td>ENCARPADOR</td>
      <td>1</td>
      <td>1</td>
      <td>2019-06-24 18:38:36</td>
      <td>9</td>
    </tr>
    <tr>
      <td>10</td>
      <td>11</td>
      <td>HERNANDEZ</td>
      <td>CHAVEZ</td>
      <td>WILMER</td>
      <td>45999310</td>
      <td>ENCARPADOR</td>
      <td>1</td>
      <td>1</td>
      <td>2019-06-24 18:40:08</td>
      <td>9</td>
    </tr>
    <tr>
      <td>11</td>
      <td>12</td>
      <td>SANCHEZ</td>
      <td>ROMERO</td>
      <td>LEONIDAS</td>
      <td>45446319</td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-06-24 18:40:58</td>
      <td>9</td>
    </tr>
    <tr>
      <td>12</td>
      <td>13</td>
      <td>DIAZ</td>
      <td>RICHARD</td>
      <td>REYES</td>
      <td>76969031</td>
      <td>ENCARPADOR</td>
      <td>1</td>
      <td>1</td>
      <td>2019-06-24 18:41:40</td>
      <td>9</td>
    </tr>
    <tr>
      <td>13</td>
      <td>14</td>
      <td>SOTO</td>
      <td></td>
      <td>MOISES</td>
      <td>42392914</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>2019-09-02 19:09:16</td>
      <td>9</td>
    </tr>
    <tr>
      <td>14</td>
      <td>15</td>
      <td>PEREZ</td>
      <td>SANCHEZ</td>
      <td>ANDY</td>
      <td>56789457</td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>2019-09-03 22:18:05</td>
      <td>9</td>
    </tr>
    <tr>
      <td>15</td>
      <td>16</td>
      <td>CABANILLAS</td>
      <td>RODRIGUEZ</td>
      <td>JHONNY</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>2019-09-09 20:39:40</td>
      <td>9</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17</td>
      <td>CABANILLAS</td>
      <td>RODRIGUEZ</td>
      <td>JHONNY</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>2019-09-09 20:39:43</td>
      <td>9</td>
    </tr>
    <tr>
      <td>17</td>
      <td>18</td>
      <td>RIVAS</td>
      <td></td>
      <td>JORGE</td>
      <td></td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>2019-09-17 14:23:09</td>
      <td>9</td>
    </tr>
    <tr>
      <td>18</td>
      <td>19</td>
      <td></td>
      <td></td>
      <td>GARAY VOLANTE</td>
      <td></td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-09-24 00:13:35</td>
      <td>9</td>
    </tr>
    <tr>
      <td>19</td>
      <td>20</td>
      <td></td>
      <td></td>
      <td>LLASAC - VOLANTE</td>
      <td></td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>2019-09-24 00:14:43</td>
      <td>9</td>
    </tr>
    <tr>
      <td>20</td>
      <td>21</td>
      <td>CASTRO</td>
      <td></td>
      <td>LUIS</td>
      <td></td>
      <td>ENCARPADOR</td>
      <td>0</td>
      <td>1</td>
      <td>2019-10-30 00:43:18</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_precioventa = "SELECT * FROM precioventa"
df_precioventa = pd.read_sql(Tabla_precioventa, db, )
df_precioventa
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
      <th>PrecioVenta_Id</th>
      <th>ProdServ_Id</th>
      <th>UnidadMedida_Id</th>
      <th>Moneda_Id</th>
      <th>PreVenPrecio</th>
      <th>dPreVenFechaAct</th>
      <th>nPreVenEliminado</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>9</td>
      <td>1</td>
      <td>15.00</td>
      <td>2018-08-21 00:10:52</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>9</td>
      <td>1</td>
      <td>15.00</td>
      <td>2018-08-21 00:11:09</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>1</td>
      <td>20.00</td>
      <td>2018-08-21 00:11:27</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>9</td>
      <td>1</td>
      <td>7464.31</td>
      <td>2018-08-21 00:11:53</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>20.00</td>
      <td>2018-09-10 17:15:46</td>
      <td>0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_prodserv = "SELECT * FROM prodserv"
df_prodserv = pd.read_sql(Tabla_prodserv, db, )
df_prodserv
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
      <th>ProdServ_Id</th>
      <th>sProSrvCodigo</th>
      <th>sProSrvCodigo2</th>
      <th>sProSrvCodigoOriginal</th>
      <th>sProSrvNombre</th>
      <th>sProSrvNombreComercial</th>
      <th>sProSrvMarca</th>
      <th>sProSrvMarcaOriginal</th>
      <th>ProSrvEspecificacion</th>
      <th>sProSrvCodigoBarras</th>
      <th>...</th>
      <th>Activo_Id</th>
      <th>nProSrvExoneradoIGV</th>
      <th>nProSrvEstado</th>
      <th>nProSrvEliminado</th>
      <th>dProSrvFecha_Act</th>
      <th>Usuario_Id</th>
      <th>ProSrvNomImagen</th>
      <th>ProSrvNomImagen2</th>
      <th>ProSrvNomImagen3</th>
      <th>ProSrvNomImagen4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>2-1</td>
      <td></td>
      <td></td>
      <td>ENCARPADO DE BOLSAS CEMENTO 42.5 kg</td>
      <td>ENCARPADO DE BOLSAS CEMENTO 42.5 kg</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-21 00:05:18</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>2-2</td>
      <td></td>
      <td></td>
      <td>ENCARPADO DE BOLSONES DE CEMENTO</td>
      <td>ENCARPADO DE BOLSONES DE CEMENTO</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-21 00:06:16</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>2-3</td>
      <td></td>
      <td></td>
      <td>ENCARPADO DE BOLSONES DE CAL</td>
      <td>ENCARPADO DE BOLSONES DE CAL</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-21 00:06:40</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>2-4</td>
      <td></td>
      <td></td>
      <td>SUPERVISIÃ“N DE ENCARPADO, VERIFICACIÃ“N Y CON...</td>
      <td>SUPERVISIÃ“N DE ENCARPADO, VERIFICACIÃ“N Y CON...</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-21 00:08:00</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>2-5</td>
      <td></td>
      <td></td>
      <td>HORAS EXTRAS</td>
      <td>HORAS EXTRAS</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-21 00:08:23</td>
      <td>1</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>2-6</td>
      <td></td>
      <td></td>
      <td>ENCARPADO DE TOLVA</td>
      <td>ENCARPADO DE TOLVA</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-10 16:25:02</td>
      <td>9</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 22 columns</p>
</div>




```python
Tabla_productolote = "SELECT * FROM productolote"
df_productolote = pd.read_sql(Tabla_productolote, db, )
df_productolote
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
      <th>ProductoLote_Id</th>
      <th>ProdServ_Id</th>
      <th>Almacen_Id</th>
      <th>sProLNombreLote</th>
      <th>nProLStockReal</th>
      <th>dProLFechaVencimiento</th>
      <th>nProLPrecioL</th>
      <th>nProLPrecioC</th>
      <th>nProLTipoPrecio</th>
      <th>nProLPorc1</th>
      <th>nProLPrecioV</th>
      <th>nProLPorc2</th>
      <th>nProLPrecioV2</th>
      <th>nProLPorc3</th>
      <th>nProLPrecioV3</th>
      <th>dProLFecha_Act</th>
      <th>nProLUsuario_Id</th>
      <th>nProLMonedaCompra_Id</th>
      <th>nProLDescuentoCompra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>20180907041201</td>
      <td>0.0</td>
      <td>1969-12-31</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>None</td>
      <td>0.0</td>
      <td>None</td>
      <td>0.0</td>
      <td>2018-09-07 16:12:01</td>
      <td>9</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>NaN</td>
      <td>20180907043304</td>
      <td>0.0</td>
      <td>1969-12-31</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>None</td>
      <td>0.0</td>
      <td>None</td>
      <td>0.0</td>
      <td>2018-09-07 16:33:04</td>
      <td>9</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>0.0</td>
      <td>20180907043913</td>
      <td>0.0</td>
      <td>2018-09-07</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>NaN</td>
      <td>2018-09-07 16:39:13</td>
      <td>9</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_tipomovimiento = "SELECT * FROM tipomovimiento"
df_tipomovimiento = pd.read_sql(Tabla_tipomovimiento, db, )
df_tipomovimiento
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
      <th>TipoMovimiento_Id</th>
      <th>sTMovNombre</th>
      <th>nTMovTipoOD</th>
      <th>nTMovSentido</th>
      <th>nTMovVisible</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>COMPRA</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>VENTA</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>INGRESO</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>SALIDA</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_ubigeo = "SELECT * FROM ubigeo"
df_ubigeo = pd.read_sql(Tabla_ubigeo, db, )
df_ubigeo
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
      <th>id</th>
      <th>dep</th>
      <th>prov</th>
      <th>dist</th>
      <th>nombre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>01</td>
      <td>00</td>
      <td>00</td>
      <td>AMAZONAS</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>01</td>
      <td>01</td>
      <td>00</td>
      <td>CHACHAPOYAS</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>01</td>
      <td>01</td>
      <td>01</td>
      <td>CHACHAPOYAS</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>01</td>
      <td>01</td>
      <td>02</td>
      <td>ASUNCION</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>01</td>
      <td>01</td>
      <td>03</td>
      <td>BALSAS</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>2054</td>
      <td>2055</td>
      <td>25</td>
      <td>03</td>
      <td>02</td>
      <td>TAHUANIA</td>
    </tr>
    <tr>
      <td>2055</td>
      <td>2056</td>
      <td>25</td>
      <td>03</td>
      <td>03</td>
      <td>YURUA</td>
    </tr>
    <tr>
      <td>2056</td>
      <td>2057</td>
      <td>25</td>
      <td>03</td>
      <td>04</td>
      <td>SEPAHUA</td>
    </tr>
    <tr>
      <td>2057</td>
      <td>2058</td>
      <td>25</td>
      <td>04</td>
      <td>00</td>
      <td>PURUS</td>
    </tr>
    <tr>
      <td>2058</td>
      <td>2059</td>
      <td>25</td>
      <td>04</td>
      <td>01</td>
      <td>PURUS</td>
    </tr>
  </tbody>
</table>
<p>2059 rows × 5 columns</p>
</div>




```python
Tabla_unidadmedida = "SELECT * FROM unidadmedida"
df_unidadmedida = pd.read_sql(Tabla_unidadmedida, db, )
df_unidadmedida
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
      <th>UnidadMedida_Id</th>
      <th>sUndDescripcion</th>
      <th>sUndAlias</th>
      <th>nUndPadre_Id</th>
      <th>nUndFac_Cnv</th>
      <th>sUndCodeSunat</th>
      <th>nUndEstado</th>
      <th>nUndEliminado</th>
      <th>dUndFecha_Act</th>
      <th>Usuario_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>Unidades de medida</td>
      <td></td>
      <td>0</td>
      <td>0.0</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>2018-05-13 00:00:00</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>Unidade(s)</td>
      <td>UND</td>
      <td>1</td>
      <td>1.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-05-13 00:00:00</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>Kilogramo</td>
      <td>Kg</td>
      <td>1</td>
      <td>0.0</td>
      <td>KGM</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td>Gramos</td>
      <td>Gr</td>
      <td>1</td>
      <td>0.0</td>
      <td>GRM</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5</td>
      <td>Litros</td>
      <td>Lt</td>
      <td>1</td>
      <td>0.0</td>
      <td>LTR</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>6</td>
      <td>Envase Uno</td>
      <td>EU</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>7</td>
      <td>Jabas</td>
      <td>J</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>Sacos</td>
      <td>S</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>8</td>
      <td>9</td>
      <td>Unidad Servicio</td>
      <td>Und</td>
      <td>1</td>
      <td>0.0</td>
      <td>ZZ</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>Caja x 10</td>
      <td>Caj10</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>11</td>
      <td>Caja x 12</td>
      <td>Caj12</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>11</td>
      <td>12</td>
      <td>Paquete x 100</td>
      <td>Paq100</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>12</td>
      <td>13</td>
      <td>Sacos T1</td>
      <td>Sa</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>13</td>
      <td>14</td>
      <td>Ejemplo</td>
      <td>S</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>14</td>
      <td>15</td>
      <td>Gramosx</td>
      <td>grm</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>15</td>
      <td>16</td>
      <td>Libras</td>
      <td>Lb</td>
      <td>1</td>
      <td>0.0</td>
      <td>LBR</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17</td>
      <td>Micro Gramos</td>
      <td>ugr</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>17</td>
      <td>18</td>
      <td>Mili Gramos</td>
      <td>mgr</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>18</td>
      <td>19</td>
      <td>Onzas</td>
      <td>Oz</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>19</td>
      <td>20</td>
      <td>Sacos Polyetileno</td>
      <td>Saco</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>20</td>
      <td>21</td>
      <td>Bolsa de Papel</td>
      <td>BP</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>21</td>
      <td>22</td>
      <td>Granel</td>
      <td>Grn</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>22</td>
      <td>23</td>
      <td>Cilindro PlÃ¡stico</td>
      <td>CP</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>23</td>
      <td>24</td>
      <td>Cilindro de Metal</td>
      <td>CilMe</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>24</td>
      <td>25</td>
      <td>Jaba Plastica</td>
      <td>Jb</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>25</td>
      <td>26</td>
      <td>0.94Litros</td>
      <td>Lts</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>26</td>
      <td>27</td>
      <td>1 Galon x 1.991Kgs</td>
      <td>Glns</td>
      <td>1</td>
      <td>0.0</td>
      <td></td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>27</td>
      <td>28</td>
      <td>1Litro x 0.892 Kilos</td>
      <td>Ltrs</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>28</td>
      <td>29</td>
      <td>Big Bags PP</td>
      <td>BigBa</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>29</td>
      <td>30</td>
      <td>Saco Premix</td>
      <td>SP</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>30</td>
      <td>31</td>
      <td>Balde Premix</td>
      <td>BP</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>31</td>
      <td>32</td>
      <td>Bolson 1T</td>
      <td>BL1T</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>32</td>
      <td>33</td>
      <td>1 Galon x 2.10Kgs</td>
      <td>Galon</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>33</td>
      <td>34</td>
      <td>Caja por 20</td>
      <td>caj20</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>34</td>
      <td>35</td>
      <td>Caja por 200</td>
      <td>Caj20</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>35</td>
      <td>36</td>
      <td>Ejmplo 1</td>
      <td>EJ</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>36</td>
      <td>37</td>
      <td>GalÃ³n</td>
      <td>Gal</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>37</td>
      <td>38</td>
      <td>Block</td>
      <td>Blk</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>38</td>
      <td>39</td>
      <td>Millar</td>
      <td>Mil</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>39</td>
      <td>40</td>
      <td>Paquete</td>
      <td>Pqt</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>40</td>
      <td>41</td>
      <td>Cilindro</td>
      <td>Cil</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>41</td>
      <td>42</td>
      <td>Metro</td>
      <td>M</td>
      <td>1</td>
      <td>0.0</td>
      <td>MTR</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>42</td>
      <td>43</td>
      <td>Metro Cuadrado</td>
      <td>M2</td>
      <td>1</td>
      <td>0.0</td>
      <td>MTK</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>43</td>
      <td>44</td>
      <td>Juego</td>
      <td>Jgo</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>44</td>
      <td>45</td>
      <td>Tonelada MÃ©trica</td>
      <td>Tm</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>45</td>
      <td>46</td>
      <td>Pares</td>
      <td>Par</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>46</td>
      <td>47</td>
      <td>CentÃ­metro</td>
      <td>Cm</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>CentÃ­metro Cuadrado</td>
      <td>Cm2</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>48</td>
      <td>49</td>
      <td>CentÃ­metro</td>
      <td>Cm</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>49</td>
      <td>50</td>
      <td>Litros</td>
      <td>Lt</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>50</td>
      <td>51</td>
      <td>Litros</td>
      <td>Lt</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
    <tr>
      <td>51</td>
      <td>52</td>
      <td>Horas</td>
      <td>Hr</td>
      <td>1</td>
      <td>0.0</td>
      <td>None</td>
      <td>1</td>
      <td>0</td>
      <td>2018-09-01 17:56:45</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
Tabla_usuario = "SELECT * FROM usuario"
df_usuario = pd.read_sql(Tabla_usuario, db, )
df_usuario
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
      <th>Usuario_Id</th>
      <th>sUsuNombre</th>
      <th>sUsuLogin</th>
      <th>sUsuContrasena</th>
      <th>nUsuTipo</th>
      <th>nUsuEstado</th>
      <th>nUsuEliminado</th>
      <th>dUsuFecha_Act</th>
      <th>nUsuUsuarioOwn_Id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>Administrador</td>
      <td>Administrador</td>
      <td>20482092897</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-20 23:50:56</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>5</td>
      <td>VICTOR CHAVEZ</td>
      <td>victor.chavez</td>
      <td>vic*2018</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-20 23:49:47</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>6</td>
      <td>ANA LUCIA TIRADO ABANTO</td>
      <td>ana.tirado</td>
      <td>analu2018</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>2018-08-20 23:50:33</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Limpieza de DATOS


```python
print (df_movimiento.shape) ##ver cantidad de registros
```

    (8060, 30)



```python
print (df_movimiento.info()) ##ver los tipos de datos
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



```python
print (pd.isnull(df_movimiento).sum()) ##ver si tenemos caracteres nulos
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
    
    [8 rows x 25 columns]


## Consultas


```python
consulta1 = "select m.Movimiento_Id, dmovfecha, smovdocumento, documento_id, mdc.Movimiento_Id as id_mdc from movimiento m left join movimientodetalleconsumo mdc on m.movimiento_id= mdc.movimiento_id where documento_id <>5 and mdc.Movimiento_Id is null"
df_consulta1= pd.read_sql(consulta1, db, )
df_consulta1
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




```python
consulta2 = "SELECT * FROM hormigui.movimiento WHERE nMovEstadoSunat = 0 and nMovEstado = 0"
df_consulta2= pd.read_sql(consulta2, db, )
df_consulta2
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
      <td>32</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>64</td>
      <td>2</td>
      <td>1</td>
      <td>32</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T5F-861/T7Y-991</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-09-11 22:47:17</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2110</td>
      <td>2018-10-01</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>54</td>
      <td>2</td>
      <td>1</td>
      <td>2093</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T4K-936/T6P-999</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-01 18:50:18</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2114</td>
      <td>2018-10-01</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>54</td>
      <td>2</td>
      <td>1</td>
      <td>2097</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-01 19:17:03</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2149</td>
      <td>2018-10-02</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>6</td>
      <td>2</td>
      <td>1</td>
      <td>2130</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-02 01:06:24</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2341</td>
      <td>2018-10-04</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>96</td>
      <td>2</td>
      <td>1</td>
      <td>2321</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-04 04:56:27</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2409</td>
      <td>2018-10-04</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>1</td>
      <td>2387</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T6G 898 - T8M 976</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-04 23:52:44</td>
      <td>19</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>3444</td>
      <td>2018-10-16</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>1</td>
      <td>3418</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-16 22:48:13</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>3708</td>
      <td>2018-10-19</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>90</td>
      <td>2</td>
      <td>1</td>
      <td>3681</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-19 00:12:28</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>3910</td>
      <td>2018-10-20</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>101</td>
      <td>2</td>
      <td>1</td>
      <td>3882</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T3V-889/T6R-971</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-20 23:54:45</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>9</td>
      <td>4672</td>
      <td>2018-10-28</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>124</td>
      <td>2</td>
      <td>1</td>
      <td>4641</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: B7O-974/T6W-990</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-10-28 05:27:18</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>6848</td>
      <td>2018-11-20</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>125</td>
      <td>2</td>
      <td>1</td>
      <td>6806</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T3R-827/T6I-972</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-11-20 01:34:18</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>11</td>
      <td>7968</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>31</td>
      <td>2</td>
      <td>1</td>
      <td>7924</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: AXC-935  TFG-975</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-11-30 07:31:58</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>12</td>
      <td>7969</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>31</td>
      <td>2</td>
      <td>1</td>
      <td>7925</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: AXC-935  TFG-975</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-11-30 07:31:58</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>13</td>
      <td>7984</td>
      <td>2018-11-30</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>62</td>
      <td>2</td>
      <td>1</td>
      <td>7937</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA: T4U-933  T7G-982</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2018-11-30 08:49:13</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>14 rows × 30 columns</p>
</div>




```python
consulta3 = "SELECT * FROM `movimiento`  ORDER BY `movimiento`.`dMovFecha`"
df_consulta3= pd.read_sql(consulta3, db, )
df_consulta3
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
      <td>737</td>
      <td>1969-12-31</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td></td>
      <td>...</td>
      <td>0.0</td>
      <td></td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-09-18 02:16:48</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>968</td>
      <td>1969-12-31</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td></td>
      <td>...</td>
      <td>0.0</td>
      <td></td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>2018-09-20 06:49:46</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>2</td>
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
      <td>3</td>
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
      <td>4</td>
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




```python

```

## GRAFICOS



```python

```


```python
df = pd.read_csv('movimiento.csv')
df.columns = ['Movimiento_Id','dMovFecha','nMovTipoMovimiento_Id','nMovTipopago','Almacen_Id','nMovTipoOrigenDestino','nMovOrigenDestino_Id','nMovTipodestino','Documento_Id','sMovDocumento','sMovDocReferencia','Moneda_Id','nMovTipoCambio','nMovImporte','nMovIGV','nMovTotal','nMovSaldo','nMovTotalCancelado','dMovDetraccion','dMovPercepcion','dMovRetencion','sMovObservacion','nMovEstadoSunat','nMovEstado','nMovEliminado','dMovFecha_Act','Usuario_Id','nMovClasificador_Id','nMovMovimiento_Id','nMovOrdenCampo_Id']
df
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
      <td>1</td>
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
      <td>2</td>
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
      <td>3</td>
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
      <td>4</td>
      <td>6</td>
      <td>2018-09-11</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>1</td>
      <td>6</td>
      <td>...</td>
      <td>0.0</td>
      <td>PLACA:  T6G-873 / TFG-972</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2018-09-11 17:45:29</td>
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
      <td>8054</td>
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
      <td>8055</td>
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
      <td>8056</td>
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
      <td>8057</td>
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
      <td>8058</td>
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
<p>8059 rows × 30 columns</p>
</div>


