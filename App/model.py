"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""


# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

# Funciones para agregar informacion al catalogo
def inicializar_catalogo():
    catalog={"Indice_fechas":None,"Accidentes":None}
    catalog['Accidentes'] = lt.newList('SINGLE_LINKED', compare)
    catalog['Indice_fechas'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    return catalog

def  añadirAccidente(catalog,Accidente):
    lt.addLast(catalog["Accidentes"],Accidente)
    AñadirAccidenteFecha(catalog,Accidente)
    return catalog

def AñadirAccidenteFecha(catalog,Accidente):
    Fecha = Accidente['Start_Time']
    Fecha_accidente = datetime.datetime.strptime(Fecha, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, Fecha_accidente.date())
    if entry is None:
        datentry = newDataEntry()
        om.put(map, Fecha_accidente.date(), datentry)
    else:
        datentry = me.getValue(entry)
    Añadir_Accidente_Tipo(datentry, Accidente)
    return map

def newDataEntry():
    
    entry = {'Severidades': None, 'Accidentes': None}
    entry['Severidades'] = m.newMap(numelements=11,
                                     maptype='PROBING',
                                     comparefunction=compareOffenses)
    entry['Accidentes'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def Añadir_Accidente_Tipo(datentry,Accidente):

    Severidad_Accidentes=datentry["Severidad"]
    Lista_Acci=datentry["Accidentes"]
    lt.addLast(Lista_Acci,Accidente)
    Seventry= m.get(Severidad_Accidentes,Accidente["Severity"])
    if Seventry == None:
        Entry= NuevaSeveridad(Accidente["Severity"],Accidente)
        lt.addLast(Seventry["Accidentes"],Accidente)
        m.put(Severidad_Accidentes,Accidente["Severity"],Entry)
    else:
        Entry= me.getValue(Seventry)
        lt.addLast(Entry["Accidentes"],Accidente)
    return datentry

def NuevaSeveridad(Severidad):
    
    Seventry = {'Severidad': None, 'Lista_Accidentes': None}
    Seventry['Severidad'] = Severidad
    Seventry['Lista_Accidentes'] = lt.newList('SINGLELINKED', compareOffenses)
    return Seventry

# ==============================
# Funciones de consulta
# ==============================
 def Accidente_Fecha_severidad(catalog,fecha):

    Accidentes_fecha= om.get(catalog["Indice_fechas"],fecha)
    if Accidentes_fecha =! None:
        Entry=me.getValue()
        


# ==============================
# Funciones de Comparacion
# ==============================
def compare_accidentes():