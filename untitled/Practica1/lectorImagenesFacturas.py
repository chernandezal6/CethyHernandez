import cv2
import pytesseract
import openpyxl
from openpyxl.styles import PatternFill

# Cargar la imagen de la factura usando OpenCV
image_path = 'ruta/a/imagen_de_factura.jpg'
image = cv2.imread(image_path)

# Definir regiones de interés (ROI) para extraer datos
roi_numero_factura = image[100:150, 200:400]  # Ejemplo: (fila_inicio:fila_fin, columna_inicio:columna_fin)
roi_fecha = image[200:250, 200:400]
roi_total = image[300:350, 200:400]

# Aplicar OCR a las ROIs para extraer texto
numero_factura = pytesseract.image_to_string(roi_numero_factura, config='--psm 7')
fecha = pytesseract.image_to_string(roi_fecha, config='--psm 7')
total = pytesseract.image_to_string(roi_total, config='--psm 7')

# Crear un nuevo archivo de Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Agregar los datos extraídos a la hoja de cálculo de Excel
sheet['A1'] = 'Número de Factura'
sheet['A2'] = numero_factura
sheet['B1'] = 'Fecha'
sheet['B2'] = fecha
sheet['C1'] = 'Total'
sheet['C2'] = total

# Guardar el archivo de Excel
excel_file_path = 'ruta/a/guardar/factura_avanzado.xlsx'
workbook.save(excel_file_path)

print(f"Datos de factura extraídos y guardados en '{excel_file_path}'")
