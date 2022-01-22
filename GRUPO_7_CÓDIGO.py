# -*- coding: utf-8 -*-
"""Proyecto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sfQg8lV1qW2gMqBcXP1GfHJ2rXbOOP2q
"""

"""
● Ingresar datos a la base de datos y que se actualicen.
● Filtrar datos por medio de características.
● Solicitar gráficos de análisis entre algunas variables.
● Solicitar datos estadísticos de los datos.
● Generar nuevas características para los datos. (Nuevas columnas)
"""
#Código prueba del trabajo
#pip install pandas
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import subplots

#Diccionario
"""
gtopub_educacion_dicc={'Fecha':[2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999],
                      'Gasto Educación (M.€)':[7638.9,7877.6,7088.0,7451.6,6692.3,6842.0,5627.5,5017.1,4387.1,3265.4,3218.1,2735.9,2373.6,1960.5,1847.8,1694.0,1572.4,1520.2,1609.4,1730.6,1762.0,1573.1],
                      'Gasto Educación (%Gto Pub)':['15.96%','17.76%','17.13%','18.24%','17.87%','17.57%','16.22%','15.22%','14.37%','13.55%','13.56%','14.60%','14.53%','14.14%','14.04%','14.28%','15.27%','14.66%','14.58%','14.80%','15.25%',''],
                      'Gasto Educación (%PIB)':['4.25%','3.82%','3.71%','3.93%','3.81%','3.97%','3.70%','3.30%','2.92%','2.66%','2.87%','3.14%','2.87%','2.63%','2.65%','2.84%','2.96%','2.94%','2.82%','3.04%','3.23%','3.44%'],
                      'Gasto Educación  Per Capita':['234€','245€','225€','241€','220€','228€','190€','171€','151€','113€','112€','96€','84€','70€','66€','61€','57€','56€','60€','65€','67€','60€'],
} 
                          
gtopub_educacion_df= pd.DataFrame(gtopub_educacion_dicc)
gtopub_educacion_df.head(30) #Comando que pertenece al objeto df y que permte visualizar las n filas
"""

#Subiendo datos del excel
#Base de datos
ruta_gtopub_educacion = input('Ingrese la ruta en formato xslx: ')
gtopub_educacion_df=pd.read_excel(ruta_gtopub_educacion)
def usuario_desicion():
  #global __estado
  desicion=input('Desea: a) Ingresar un nuevo dato (escriba "Ingresar"), b) Filtrar datos (escriba "Filtrar"), c) Solicitar gráficos (escriba "Gráficos"), d) Solicitar datos estadísiticos (escriba "Datos", e) Generar nuevas características (escriba "Añadir") o cualquier letra para terminar: ')
  a=['Ingresar','ingresar'] 
  b=['Filtrar', 'filtrar'] 
  c=['Gráficos','gráficos','Graficos','graficos'] 
  d=['Datos','datos'] 
  e=['Añadir','añadir']
  if desicion in a:
    __estado =1
  elif desicion in b:
    __estado=2
  elif desicion in c:
    __estado=3
  elif desicion in d:
    __estado=4
  elif desicion in e:
    __estado=5
  else:
    __estado=6
  return __estado

__estado=usuario_desicion()

while True:     #Python cada vez que termina una línes de código, a menos que el resultado sea False, None, o OL (proposición falsa) da Verdad
  if __estado ==1: #Ingresar un nuevo dato
    def Columns(df):
      columnas =df.columns
      list_columns=list(columnas)
      return list_columns
    df=gtopub_educacion_df
    def añadir_fila():
      global df
      dicc_fila={}
      columnas_df= Columns(df) #Retorna una lista con las columnas
      for columna in columnas_df:
        dicc_fila[columna]=input(f'Ingrese valor de la columna {columna}: ')
      df =df.append(dicc_fila, ignore_index=True)
      df.to_excel(ruta_gtopub_educacion) ###Activarlo para guardar y que se actualicen los datos ingresados
    añadir_fila()
    display(df)
    __estado= usuario_desicion()

  if __estado ==2: #Filtrar búsquedas por medio de características
    question=input('Desea buscar a) Fecha (escribe "F"), b) Gasto Educación (M. €) (escribe "GE") , c) Gasto Educación (%Gto Pub) (escribe "GE%"), d) Gasto Educación (%PIB) escribe("PIB"), e)Gasto Educación Per Capita € (escribe "PC"): ')
    if question == 'F':
      year=input('Ingrese el año: ')
      fecha = gtopub_educacion_df['Fecha'] == year
      fecha_dada = gtopub_educacion_df[fecha]
      display(fecha_dada.head(30))
    elif question == 'GE':
      print('A continuación deberá ingresar un número para filtrar datos menores o iguales ingresados en  Gasto Educación (M. €)')
      procien=input('Ingrese un valor: ')
      GE = gtopub_educacion_df['Gasto Educación (M. €)'] <= porcien
      GE_dada = gtopub_educacion_df[GE]
      display(GE_dada.head(30))
    elif question == 'GE%':
      print('A continuación deberá ingresar un número para filtrar datos mayores iguales ingresados en  Gasto Educación (%Gto Pub)')
      percent=float(input('Ingrese un valor : '))
      GEp= gtopub_educacion_df['Gasto Educación(%Gto Pub)'] >= year
      GEp_dada = gtopub_educacion_df[GEp]
      display(GEp_dada.head(30))
    elif question == 'PIB':
      print('A continuación deberá ingresar un número para filtrar datos menores o iguales ingresados en  Gasto Educación (%PIB)')
      porcent=float(input('Ingrese un valor: '))
      PC = gtopub_educacion_df['Gasto Educación(%PIB)'] <= porcent
      PC_dada = gtopub_educacion_df[PC]
      display(PC_dada.head(30))
    elif question == 'PC':
      print('A continuación deberá ingresar un número para filtrar datos mayores o iguales ingresados en Gasto Educación  Per Capita €')
      cant=float(input('Ingrese una cantidad: '))
      PC = gtopub_educacion_df['Gasto Educación Per Capita €'] >= cant
      PC_dada = gtopub_educacion_df[PC]
      display(PC_dada.head(30))  

    else:
      print('Incorrecto')
    __estado= usuario_desicion()

  if __estado ==3: #Solicitar gráficos de análisis entre algunas variables.
      #choose=input('Escribe "I" para solicitar menú de gráficos: ')
        pregunta=input('¿Qué gráfico desea ver? a) Fecha vs Gasto Educación (M. €)  (escribe "FvsGE"), b) Fecha vs Gasto Educación (%Gto Pub) (escribe "FvsGE%", c) Fecha vs Gasto Educación(%PIB) (escribe "FvsPIB"), d) Fecha vs Gasto Educación Per Cápita ("FvsPC"), e) Comparación entre más de 2 variables (escribe "Otros"): ')
      #while choose== 'I':
        if pregunta == 'FvsGE':
          fig, ax=subplots()
          x_fecha=np.array(gtopub_educacion_df['Fecha'])
          y_gastoME= np.array(gtopub_educacion_df['Gasto Educación(M. €)'])
          ax.plot(x_fecha,y_gastoME,color='r',alpha=1)
          ax.set_title('Fecha vs GE')
          ax.annotate('Maximun', xy = (2019,7877.6), xytext= (2015,2500), 
              arrowprops = dict(arrowstyle = "->",facecolor ='black'))
          ax.grid()
          plt.show()
        elif pregunta == 'FvsGE%':
          fig, ax1=subplots()
          x_fecha=np.array(gtopub_educacion_df['Fecha'])
          y_GE= np.array(gtopub_educacion_df['Gasto Educación(%Gto Pub)'])
          ax1.plot(x_fecha,y_GE,color='b',alpha=1)
          ax1.set_title('Fecha vs GE%')
          ax1.annotate('Maximun', xy = (2017,18.24), xytext= (2015,15.5), 
              arrowprops = dict(arrowstyle = "->",facecolor ='black'))
          ax1.grid()
          plt.show()
        elif pregunta == 'FvsPIB':
          fig, ax2= subplots()
          x_fecha=np.array(gtopub_educacion_df['Fecha'])
          y_PIB= np.array(gtopub_educacion_df['Gasto Educación(%PIB)'])
          ax2.plot(x_fecha,y_PIB,color='y',alpha=1)
          ax2.set_title('Fecha vs %PIB')
          ax2.annotate('Maximun', xy = (2020,4.25), xytext= (2018,2.5), 
              arrowprops = dict(arrowstyle = "->",facecolor ='black'))
          ax2.grid()
          plt.show()
        elif pregunta == 'FvsPC':
          fig, ax3=subplots()
          x_fecha=np.array(gtopub_educacion_df['Fecha'])
          y_PC= np.array(gtopub_educacion_df['Gasto Educación Per Capita €'])
          ax3.plot(x_fecha,y_PC,color='g',alpha=1)
          ax3.set_title('Fecha vs PC')
          ax3.annotate('Maximun', xy = (2019,245), xytext= (2015,60), 
              arrowprops = dict(arrowstyle = "->",facecolor ='black'))
          ax3.grid()
          plt.show()
  
    #Más graficos, comparando más de 2 variables
        elif pregunta == 'Otros':
          fecha_gtopub_educacion = list(gtopub_educacion_df['Fecha'])
          GE_gtopub_educacion = list(gtopub_educacion_df['Gasto Educación(M. €)'])
          GEp_gtopub_educacion = list(20*np.array(gtopub_educacion_df['Gasto Educación(%Gto Pub)'])) #Escalamiento de data
          PIB_gtopub_educacion = list(gtopub_educacion_df['Gasto Educación(%PIB)'])
          plt.scatter(fecha_gtopub_educacion,GE_gtopub_educacion,s=GEp_gtopub_educacion, c=PIB_gtopub_educacion,alpha=0.57,cmap='viridis')
          plt.colorbar()
          print('Gráfico que muestra la comparación entre Fecha, Gasto Educación (M.€), Gasto Educación(%Gto Pub) y Gasto Educación(%PIB)')
          plt.show()
        #choose=input('Escribe "I" para solicitar menú de gráficos u otro comando para finalizar: ')
        #break
        __estado= usuario_desicion()


  if __estado ==4: #Solicitar datos estadísticos de los datos
    #quest=input()
    print('Los datos estadísticos son los siguientes: ')
    display(gtopub_educacion_df.describe())
    __estado= usuario_desicion()


  if __estado ==5: #Generar nuevas características para los datos. (Nuevas columnas)
    elctn=input('Escribe "s" para agregar columnas: ')
    #name_col=input('Ingresa el nombre de la columna: ')
    #m=['s','S']
    lista_col=[]
    if elctn == 's':
    #while elctn =='s':
      name_col=input('Ingresa el nombre de la columna: ')
      for i in range (len(gtopub_educacion_df)):
        lista_col.append(input(f'Ingrese el valor para el ID {i}: '))
      gtopub_educacion_df[name_col]=lista_col
      #elctn=input('"s" para agregar nueva columna columna u otro comando para terminar: ')
      display(gtopub_educacion_df)
      gtopub_educacion_df.to_excel(ruta_gtopub_educacion ) ###Activarlo para guardar y que se actualicen los datos ingresados
      break
    else:
      break
  

  if __estado ==6: #Se ha decidido mostrar la base de datos ingresada por el usuario sin necesidad de preguntarle al momento que elija cerrar el programa
    print('La base de datos es:')
    gtopub_educacion_df=pd.read_excel(ruta_gtopub_educacion)
    gtopub_educacion_df.head(30)
    display(gtopub_educacion_df)
    print('Cerrar')
    break #Cortará el flujo del bucle donde se encuentra
print('Programa finalizado')

from google.colab import drive
drive.mount('/content/drive')