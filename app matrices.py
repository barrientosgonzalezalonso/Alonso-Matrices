import streamlit as st
import numpy as np
import os

# Espacio para matrices
if "matrices" not in st.session_state:
    st.session_state.matrices = {"A": None, "B": None, "C": None, "D": None}

def capturar_matriz(nombre):
    filas = st.number_input("Número de filas", min_value=1, step=1)
    columnas = st.number_input("Número de columnas", min_value=1, step=1)
    datos = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = st.number_input(f"Valor ({i},{j})", value=0.0, key=f"{nombre}_{i}_{j}")
            fila.append(valor)
        datos.append(fila)
    st.session_state.matrices[nombre] = np.array(datos)
    st.success(f"Matriz {nombre} capturada")

def guardar_matriz(nombre, archivo):
    if st.session_state.matrices[nombre] is None:
        st.error(f"La matriz {nombre} está vacía")
        return
    np.savetxt(archivo, st.session_state.matrices[nombre], fmt="%.2f")
    st.success(f"Matriz {nombre} guardada en {archivo}")

def leer_matriz(nombre, archivo):
    if not os.path.exists(archivo):
        st.error("El archivo no existe")
        return
    st.session_state.matrices[nombre] = np.loadtxt(archivo)
    st.success(f"Matriz {nombre} leída desde {archivo}")

def sumar_matrices(m1, m2, destino):
    try:
        st.session_state.matrices[destino] = st.session_state.matrices[m1] + st.session_state.matrices[m2]
        st.success(f"Suma guardada en {destino}")
    except:
        st.error("Error al sumar matrices")

def multiplicar_matrices(m1, m2, destino):
    try:
        st.session_state.matrices[destino] = np.dot(st.session_state.matrices[m1], st.session_state.matrices[m2])
        st.success(f"Multiplicación guardada en {destino}")
    except:
        st.error("Error al multiplicar matrices")

def multiplicar_por_factor(nombre, factor, destino):
    try:
        st.session_state.matrices[destino] = st.session_state.matrices[nombre] * factor
        st.success(f"Multiplicación por factor guardada en {destino}")
    except:
        st.error("Error al aplicar factor")

def inversa_matriz(nombre, destino):
    try:
        st.session_state.matrices[destino] = np.linalg.inv(st.session_state.matrices[nombre])
        st.success(f"Inversa guardada en {destino}")
    except:
        st.error("La matriz no es invertible")

def mostrar_matriz(nombre):
    if st.session_state.matrices[nombre] is not None:
        st.write(f"Matriz {nombre}:")
        st.write(st.session_state.matrices[nombre])
    else:
        st.warning(f"Matriz {nombre} está vacía")

# --- Interfaz Streamlit ---
st.title("🧮 Laboratorio de Matrices")

opcion = st.sidebar.selectbox("Selecciona una operación", [
    "Capturar matriz", "Guardar matriz", "Leer matriz",
    "Sumar matrices", "Multiplicar matrices",
    "Multiplicar por factor", "Inversa de matriz",
    "Mostrar matrices"
])

if opcion == "Capturar matriz":
    nombre = st.selectbox("Selecciona matriz", ["A","B","C","D"])
    capturar_matriz(nombre)

elif opcion == "Guardar matriz":
    nombre = st.selectbox("Selecciona matriz", ["A","B","C","D"])
    archivo = st.text_input("Nombre de archivo", "Matriz001.txt")
    if st.button("Guardar"):
        guardar_matriz(nombre, archivo)

elif opcion == "Leer matriz":
    nombre = st.selectbox("Selecciona matriz", ["A","B","C","D"])
    archivo = st.text_input("Nombre de archivo", "Matriz001.txt")
    if st.button("Leer"):
        leer_matriz(nombre, archivo)

elif opcion == "Sumar matrices":
    m1 = st.selectbox("Primera matriz", ["A","B","C","D"])
    m2 = st.selectbox("Segunda matriz", ["A","B","C","D"])
    destino = st.selectbox("Destino", ["A","B","C","D"])
    if st.button("Sumar"):
        sumar_matrices(m1, m2, destino)

elif opcion == "Multiplicar matrices":
    m1 = st.selectbox("Primera matriz", ["A","B","C","D"])
    m2 = st.selectbox("Segunda matriz", ["A","B","C","D"])
    destino = st.selectbox("Destino", ["A","B","C","D"])
    if st.button("Multiplicar"):
        multiplicar_matrices(m1, m2, destino)

elif opcion == "Multiplicar por factor":
    nombre = st.selectbox("Matriz", ["A","B","C","D"])
    factor = st.number_input("Factor", value=1.0)
    destino = st.selectbox("Destino", ["A","B","C","D"])
    if st.button("Aplicar"):
        multiplicar_por_factor(nombre, factor, destino)

elif opcion == "Inversa de matriz":
    nombre = st.selectbox("Matriz", ["A","B","C","D"])
    destino = st.selectbox("Destino", ["A","B","C","D"])
    if st.button("Calcular inversa"):
        inversa_matriz(nombre, destino)

elif opcion == "Mostrar matrices":
    for nombre in ["A","B","C","D"]:
        mostrar_matriz(nombre)
