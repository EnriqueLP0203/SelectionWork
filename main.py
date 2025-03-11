import sys
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from matriz_ui import Ui_Dialog  # Importamos la interfaz generada


class MatrizApp(QDialog):
    def __init__(self, matriz):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

        # Configurar las tablas
        self.ui.tableWidget.setRowCount(self.filas)
        self.ui.tableWidget.setColumnCount(self.columnas)
        self.ui.tableWidget_2.setRowCount(self.filas)
        self.ui.tableWidget_2.setColumnCount(self.columnas)

        # Mostrar la matriz desordenada en la primera tabla
        self.mostrar_matriz(self.ui.tableWidget, self.matriz)

        # Conectar el botón a la función de ordenamiento
        self.ui.pushButton.clicked.connect(self.ordenar_matriz)

    def mostrar_matriz(self, tabla, matriz):

       # Mostrar una matriz en una tabla
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                tabla.setItem(i, j, QTableWidgetItem(str(valor)))

    def algoritmoSort(self, lista):

        n = len(lista)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if lista[j] < lista[min_idx]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]

    def ordenar_matriz(self):

        datos = sum(self.matriz, [])  # Convertir la matriz en una lista plana
        self.algoritmoSort(datos)  # Ordenar la lista plana con Selection Sort
        
        # Reconstruir la matriz ordenada
        matriz_ordenada = [
            datos[i * self.columnas:(i + 1) * self.columnas]
            for i in range(self.filas)
        ]

        # Mostrar la matriz ordenada en la segunda tabla
        self.mostrar_matriz(self.ui.tableWidget_2, matriz_ordenada)

def obtenerDatos():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    matriz = []
    print("Ingrese los datos de la matriz fila por fila (separados por espacios):")
    for i in range(filas):
        fila = list(map(int, input(f"Fila {i + 1}: ").split()))
        if len(fila) != columnas:
            raise ValueError("El número de columnas no coincide con el especificado.")
        matriz.append(fila)

    return matriz


if __name__ == "__main__":
    try:
        matriz_desordenada = obtenerDatos()

        # Iniciar la aplicación PyQt6
        app = QApplication(sys.argv)
        dialog = MatrizApp(matriz_desordenada)
        dialog.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error: {e}")