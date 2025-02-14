from utils.excel_processor import ExcelProcessor
from models.out_format import OutFormat
from utils.data_processor import DataProcessor

class Constructor:
    def __init__(self, input_path, output_path, id_local):
        self.input_path = input_path
        self.output_path = output_path
        self.id_local = id_local
        self.data_processor = DataProcessor(input_path, output_path)
    
    def execute(self):
        self.data_processor.write_processed_data(self.id_local)
        print("Proceso completado correctamente.")
