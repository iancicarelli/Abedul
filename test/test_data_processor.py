import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils.excel_processor import ExcelProcessor
from utils.data_processor import DataProcessor


class TestData(unittest.TestCase):
    def setUp(self):
        # Rutas de los archivos de entrada
        input_path = r"C:\Users\HP\Desktop\Reiterar orden de compra\OC.xlsx"
        output_path = r"C:\Users\HP\Desktop\Reiterar orden de compra\a.xlsx"
        
        # Crear una instancia de CostProcessor con el path de BD_ILA
        self.data_processor = DataProcessor(input_path,output_path)

    def test_compare_with_json(self):
        processed_data = self.data_processor.get_processed_data()
        for values in processed_data:
            print(f"Código: {values['codigo']}, Amount: {values['amount']}")

            
if __name__ == "__main__":
    unittest.main()