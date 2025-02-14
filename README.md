# Abedul

**Abedul** es una aplicación desarrollada en Python junto con `ttkthemes`, diseñada para procesar y reestructurar órdenes de compra de manera eficiente.

## 📌 Funcionalidad

El proceso de Abedul es simple e intuitivo:

1. **Selección de la orden de compra**: Se elige un archivo descargado desde Orion.
2. **Configuración de salida**: Se especifica la ubicación y el nombre del archivo de salida.
3. **Selección de la sucursal**: Se define la sucursal correspondiente.
4. **Procesamiento**: La aplicación extrae los valores de las columnas **B** y **F** (código del producto y cantidad) y los combina con el ID de la sucursal seleccionada.

Por ejemplo, si la **sucursal N°5** tiene un identificador **5**, el archivo generado contendrá tres columnas:

- **Código del producto**
- **Cantidad**
- **ID de la sucursal**

El resultado es un nuevo archivo Excel listo para su uso.

## 🚀 Tecnologías utilizadas

- **Python**
- **Tkinter** y `ttkthemes` para la interfaz gráfica
- **Pandas** para la manipulación de archivos Excel

## 📷 Capturas de formato junto con interfaz 

### Entrada

![imagen](https://github.com/iancicarelli/Abedul/blob/main/img/Entrada.png)

### Interfaz 

![imagen](https://github.com/iancicarelli/Abedul/blob/main/img/IDE.png)

### Salida

![imagen](https://github.com/iancicarelli/Abedul/blob/main/img/Salida.png)

