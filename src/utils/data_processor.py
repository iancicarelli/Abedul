from models.out_format import OutFormat
from utils.excel_processor import ExcelProcessor

class DataProcessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.excel_processor = ExcelProcessor(input_path)
        

    
    def get_processed_data(self):
        # Leer el archivo Excel
        self.excel_processor.read_excel()
        sheet = self.excel_processor.get_sheet()
        processed_data = []  # Lista para almacenar los datos procesados
        # Iterar sobre las filas del archivo Excel (comenzando desde la fila 2 para saltar los encabezados)
        for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row):
            codigo = row[1].value  # Columna B (Código)
            amount = row[5].value  # Columna F (amount)
            processed_data.append({"codigo": codigo, "amount": amount})
        return processed_data
    
    def write_processed_data(self,id_local):
        processed_data = self.get_processed_data()
        
        # Usar la clase ExcelProcessor para escribir los datos
        self.excel_processor.write_excel(
            [OutFormat(data["codigo"], data["amount"], id_local) for data in processed_data], 
            self.output_path
        )
        print(f"Datos procesados guardados en {self.output_path}")
