#!/usr/bin/env python
# coding: utf-8

# ## Conexion a base de datos

# In[115]:


import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[64]:


db = pymysql.connect("localhost","darkted","upaom1","hormigui")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : {0}".format(data))


# ## Convertir tablas en DataFrames ##

# In[3]:


Tabla_activo = "SELECT * FROM activo"
df_activo = pd.read_sql(Tabla_activo, db, )
df_activo


# In[4]:


Tabla_almc = "SELECT * FROM almacen"
df_almc = pd.read_sql(Tabla_almc, db, )
df_almc


# In[5]:


Tabla_bitacorausuario = "SELECT * FROM bitacorausuario"
df_bitacorausuario = pd.read_sql(Tabla_bitacorausuario, db, )
df_bitacorausuario


# In[6]:


Tabla_clasificador = "SELECT * FROM clasificador"
df_clasificador = pd.read_sql(Tabla_clasificador, db, )
df_clasificador


# In[7]:


Tabla_conceptofijo = "SELECT * FROM conceptofijo"
df_conceptofijo = pd.read_sql(Tabla_conceptofijo, db, )
df_conceptofijo


# In[8]:


Tabla_cotizacion = "SELECT * FROM cotizacion"
df_cotizacion = pd.read_sql(Tabla_cotizacion, db, )
df_cotizacion


# In[9]:


Tabla_cotizaciondetalle = "SELECT * FROM cotizaciondetalle"
df_cotizaciondetalle = pd.read_sql(Tabla_cotizaciondetalle, db, )
df_cotizaciondetalle


# In[10]:


Tabla_documento = "SELECT * FROM documento"
df_documento = pd.read_sql(Tabla_documento, db, )
df_documento


# In[11]:


Tabla_familia = "SELECT * FROM familia"
df_familia = pd.read_sql(Tabla_familia, db, )
df_familia


# In[12]:


Tabla_moneda = "SELECT * FROM moneda"
df_moneda = pd.read_sql(Tabla_moneda, db, )
df_moneda


# In[68]:


Tabla_movimiento = "SELECT * FROM movimiento"
df_movimiento = pd.read_sql(Tabla_movimiento, db, )
df_movimiento


# In[14]:


Tabla_movidet = "SELECT * FROM movimientodetalle"
df_movidet = pd.read_sql(Tabla_movidet, db, )
df_movidet


# In[15]:


Tabla_movimientodetalleconsumo = "SELECT * FROM movimientodetalleconsumo"
df_movimientodetalleconsumo = pd.read_sql(Tabla_movimientodetalleconsumo, db, )
df_movimientodetalleconsumo


# In[16]:


Tabla_origendestino = "SELECT * FROM origendestino"
df_origendestino = pd.read_sql(Tabla_origendestino, db, )
df_origendestino


# In[17]:


Tabla_pago = "SELECT * FROM pago"
df_pago = pd.read_sql(Tabla_pago, db, )
df_pago


# In[18]:


Tabla_parametros = "SELECT * FROM parametros"
df_parametros = pd.read_sql(Tabla_parametros, db, )
df_parametros


# In[19]:


Tabla_personal = "SELECT * FROM personal"
df_personal = pd.read_sql(Tabla_personal, db, )
df_personal


# In[20]:


Tabla_precioventa = "SELECT * FROM precioventa"
df_precioventa = pd.read_sql(Tabla_precioventa, db, )
df_precioventa


# In[21]:


Tabla_prodserv = "SELECT * FROM prodserv"
df_prodserv = pd.read_sql(Tabla_prodserv, db, )
df_prodserv


# In[22]:


Tabla_productolote = "SELECT * FROM productolote"
df_productolote = pd.read_sql(Tabla_productolote, db, )
df_productolote


# In[23]:


Tabla_tipomovimiento = "SELECT * FROM tipomovimiento"
df_tipomovimiento = pd.read_sql(Tabla_tipomovimiento, db, )
df_tipomovimiento


# In[24]:


Tabla_ubigeo = "SELECT * FROM ubigeo"
df_ubigeo = pd.read_sql(Tabla_ubigeo, db, )
df_ubigeo


# In[25]:


Tabla_unidadmedida = "SELECT * FROM unidadmedida"
df_unidadmedida = pd.read_sql(Tabla_unidadmedida, db, )
df_unidadmedida


# In[26]:


Tabla_usuario = "SELECT * FROM usuario"
df_usuario = pd.read_sql(Tabla_usuario, db, )
df_usuario


# ## Limpieza de DATOS

# In[27]:


print (df_movimiento.shape) ##ver cantidad de registros


# In[28]:


print (df_movimiento.info()) ##ver los tipos de datos


# In[32]:


print (pd.isnull(df_movimiento).sum()) ##ver si tenemos caracteres nulos


# In[49]:


print (df_movimiento.describe(include='all'))


# In[52]:


df_movimiento.drop([736, 967],axis=0)


# In[69]:


df_movimiento


# In[66]:


cursor.execute ("""delete from movimiento where movimiento.Movimiento_Id = 737""")


# In[70]:


cursor.execute ("""delete from movimiento where movimiento.Movimiento_Id = 968""")


# In[83]:


consulta4 = "SELECT * FROM `movimiento` where dMovFecha >='2018-09-11' and dMovFecha <='2018-10-31'"
df_train= pd.read_sql(consulta4, db, )
print (df_train.shape)


# In[84]:


consulta5 = "SELECT * FROM `movimiento` where dMovFecha >='2018-11-01' and dMovFecha <='2018-11-15'"
df_test= pd.read_sql(consulta5, db, )
print (df_test.shape)


# In[85]:


consulta6 = "SELECT * FROM `movimiento` where dMovFecha >='2018-11-16' and dMovFecha <='2018-11-30'"
df_vali= pd.read_sql(consulta6, db, )
print (df_vali.shape)


# ## Consultas

# In[58]:


consulta1 = "select m.Movimiento_Id, dmovfecha, smovdocumento, documento_id, mdc.Movimiento_Id as id_mdc from movimiento m left join movimientodetalleconsumo mdc on m.movimiento_id= mdc.movimiento_id where documento_id <>5 and mdc.Movimiento_Id is null"
df_consulta1= pd.read_sql(consulta1, db, )
df_consulta1


# In[27]:


consulta2 = "SELECT * FROM hormigui.movimiento WHERE nMovEstadoSunat = 0 and nMovEstado = 0"
df_consulta2= pd.read_sql(consulta2, db, )
df_consulta2


# In[74]:


consulta3 = "SELECT * FROM `movimiento`  ORDER BY `movimiento`.`dMovFecha`"
df_consulta3= pd.read_sql(consulta3, db, )
df_consulta3


# ## PROCESAMIENTO

# In[86]:


from sklearn import linear_model


# In[88]:


print ('Informacion en el dataframe')
print (df_movimiento.keys())


# In[114]:


df_movimiento.head()


# In[121]:


fig = plt.figure(figsize=(14,14))
plt.scatter(df_movimiento['dMovFecha'],df_movimiento['nMovTotal'])
plt.plot(df_movimiento['Image Number'],df_movimiento['nMovTotal'])
plt.xlabel('Fechas')
plt.ylabel('precio con IGV')
plt.grid()


# ## GRAFICOS
# 

# In[72]:


df_movimiento.groupby('nMovEstadoSunat')['Movimiento_Id'].plot(kind='line',legend='prueba')


# In[73]:


df_movimiento.groupby(df_movimiento.Usuario_Id).plot(kind='scatter',x='Usuario_Id',y='nMovEstadoSunat',color='red')


# In[95]:


df = pd.read_csv('movimiento.csv')
df.columns = ['Movimiento_Id','dMovFecha','nMovTipoMovimiento_Id','nMovTipopago','Almacen_Id','nMovTipoOrigenDestino','nMovOrigenDestino_Id','nMovTipodestino','Documento_Id','sMovDocumento','sMovDocReferencia','Moneda_Id','nMovTipoCambio','nMovImporte','nMovIGV','nMovTotal','nMovSaldo','nMovTotalCancelado','dMovDetraccion','dMovPercepcion','dMovRetencion','sMovObservacion','nMovEstadoSunat','nMovEstado','nMovEliminado','dMovFecha_Act','Usuario_Id','nMovClasificador_Id','nMovMovimiento_Id','nMovOrdenCampo_Id']
df


# In[106]:


df_movimiento.to_csv(r'/home/darkted/movimiento.csv')

