import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk
from utils.constructor import Constructor
import os
from tkinter import PhotoImage
from utils.path_manager import PathManager

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reitera orden de compra")
        self.root.geometry("600x300")
        
        self.file_entry = None
        self.output_file_entry = None
        self.output_name_entry = None
        self.dropdown = None
        
        self.path_manager = PathManager()
        image_path = self.path_manager.get_image_path("fondo.png")  # Cambia por la imagen de fondo

        # Cargar la imagen de fondo
        self.bg_image = tk.PhotoImage(file=image_path)  # Ajusta la ruta de la imagen
        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)  # Hacer que el canvas ocupe toda la ventana

        # Colocar la imagen de fondo en el Canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Crear un Frame que estará sobre el Canvas
        self.container = ttk.Frame(self.root)
        self.canvas.create_window(300, 150, window=self.container)  # Centrar los widgets en el Canvas
        # Centrar los widgets

        # Crear los widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Estilo general
        style = ttk.Style()
         # Configurar el estilo de los botones
        style.configure('TButton', 
                        font=('Helvetica', 10), 
                        padding=5, 
                        background='#00692A', 
                        foreground='black')
        style.map('TButton', 
                  background=[('active', '#FFD700')],  # Cambia al hacer clic
                  foreground=[('active', 'white')])   # Texto negro al hacer clic

        # Estilo para las etiquetas
        style.configure('TLabel', 
                        font=('Helvetica', 10), 
                        padding=5, 
                       # background='#44A46B',  # Igual al fondo de la app
                        foreground='#000000')  # Color de texto recomendado

        # Estilo para las entradas de texto
        style.configure('TEntry', 
                        font=('Helvetica', 10), 
                        padding=5, 
                        fieldbackground='#000000',  # Color de fondo para inputs
                        foreground='#222222')  # Texto oscuro

        # Estilo para los combobox
        style.configure('TCombobox', 
                        font=('Helvetica', 10), 
                        padding=5, 
                        fieldbackground='#44A46B', 
                        foreground='#222222')

        self.root.configure(background='#00953A')
        # File selection row (input file)
        file_frame = ttk.Frame(self.root)
        file_frame.pack(pady=10, padx=10, fill='x')
        

        file_label = ttk.Label(file_frame, text="Selecciona un archivo de entrada:")
        file_label.pack(side='left', padx=(0, 10))

        self.file_entry = ttk.Entry(file_frame)
        self.file_entry.pack(side='left', expand=True, fill='x')

        select_button = ttk.Button(file_frame, text="Seleccionar", command=self.select_file)
        select_button.pack(side='left', padx=(10, 0))

        # File selection row (output file)
        output_file_frame = ttk.Frame(self.root)
        output_file_frame.pack(pady=10, padx=10, fill='x')

        output_file_label = ttk.Label(output_file_frame, text="Selecciona ubicación de salida:")
        output_file_label.pack(side='left', padx=(0, 10))

        self.output_file_entry = ttk.Entry(output_file_frame)
        self.output_file_entry.pack(side='left', expand=True, fill='x')

        select_output_button = ttk.Button(output_file_frame, text="Seleccionar", command=self.select_output_file)
        select_output_button.pack(side='left', padx=(10, 0))

        # Output file name entry
        output_name_frame = ttk.Frame(self.root)
        output_name_frame.pack(pady=10, padx=10, fill='x')

        output_name_label = ttk.Label(output_name_frame, text="Nombre del archivo de salida:")
        output_name_label.pack(side='left', padx=(0, 10))

        self.output_name_entry = ttk.Entry(output_name_frame)
        self.output_name_entry.pack(side='left', expand=True, fill='x')

        # Dropdown menu
        dropdown_frame = ttk.Frame(self.root)
        dropdown_frame.pack(pady=10)

        dropdown_label = ttk.Label(dropdown_frame, text="Seleccionar local:")
        dropdown_label.pack(side='left', padx=(0, 10))

        self.data = {
            "ALDUNATE": 21, "ANGOL": 17, "BARROS ARANA": 15, "BULNES": 22,
            "CAJON": 16, "CARAHUE": 2, "CHILLAN": 249, "COLLIPULLI": 9,
            "CUNCO": 3, "CURACAUTIN": 29, "FUTRONO": 345, "GORBEA": 6,
            "IMPERIAL": 10, "LABRANZA": 8, "LANCO": 12, "LAUTARO 2": 27,
            "LLANQUIHUE": 250, "LONCOCHE": 14, "LOS ANGELES": 25, "LOS LAGOS": 271,
            "LUIS DURAND": 5, "MULCHEN": 280, "PADRE LAS CASAS": 20, "PANGUIPULLI": 19,
            "PANGUIPULLI 2": 26, "PINTO": 28, "PITRUFQUEN": 13, "PUREN": 188,
            "RECABARREN": 7, "RUDECINDO ORTEGA": 171, "SAN JOSE": 294,
            "TRAIGUEN": 4, "TRAIGUEN 2": 42, "VALDIVIA SCHNEIDER": 24,
            "VALDIVIA SIMPSON": 23, "VICTORIA": 11, "VICUÑA MACKENNA": 18,
            "VILCUN": 1, "PEDRO DE VALDIVIA": 1065
        }
        
        self.dropdown = ttk.Combobox(dropdown_frame, values=list(self.data.keys()), state="readonly")
        self.dropdown.pack(side='left')
        self.dropdown.set(list(self.data.keys())[0])
        
        # Run button
        run_button = ttk.Button(self.root, text="Iniciar", command=self.run_application)
        run_button.pack(pady=20)
    
    def select_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)
    
    def select_output_file(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_file_entry.delete(0, tk.END)
            self.output_file_entry.insert(0, folder_selected)
    
    def run_application(self):
        # Obtener las rutas de entrada y salida y el local seleccionado
        input_path = self.file_entry.get()
        output_dir = self.output_file_entry.get()
        output_name = self.output_name_entry.get()

        # Asegurarse de que el archivo de salida tenga la extensión .xlsx
        if not output_name.endswith(".xlsx"):
            output_name += ".xlsx"  # Si no tiene, se agrega la extensión

        # Crear la ruta completa del archivo de salida
        output_path = os.path.join(output_dir, output_name)
        output_path = os.path.normpath(output_path)
        
        
        # Obtener el ID del local seleccionado
        id_local = self.data.get(self.dropdown.get())

        # Crear una instancia de la clase Constructor
        constructor = Constructor(input_path, output_path, id_local)

        # Ejecutar el proceso
        constructor.execute()

        # Imprimir información de la ejecución
        print("Archivo de entrada:", input_path)
        print("Ubicación de salida:", output_dir)
        print("Nombre del archivo de salida:", output_name)
        print("Local seleccionado:", self.dropdown.get())

def main():
    root = ThemedTk(theme="arc")
    MenuApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()