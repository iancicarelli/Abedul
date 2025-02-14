from utils.excel_processor import ExcelProcessor
from utils.data_processor import DataProcessor  # Asegúrate de importar correctamente tu clase
from visuals.menu import MenuApp
from ttkthemes import ThemedTk


def main():
    root = ThemedTk()
    MenuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()