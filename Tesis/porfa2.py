import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("App CRUD con Tkinter y CSV")

        # Lista de datos
        self.data = []

        # Botones
        btn_ingresar = tk.Button(self.ventana, text="Ingresar", command=self.ingresar)
        btn_ingresar.grid(row=0, column=0, padx=5, pady=5)

        btn_exportar = tk.Button(self.ventana, text="Exportar CSV", command=self.exportar_csv)
        btn_exportar.grid(row=0, column=1, padx=5, pady=5)

        btn_importar = tk.Button(self.ventana, text="Importar CSV", command=self.importar_csv)
        btn_importar.grid(row=0, column=2, padx=5, pady=5)

        # Vista de los datos
        self.vista_datos = tk.LabelFrame(self.ventana, text="Datos")
        self.vista_datos.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Configurar la expansión de la vista de los datos
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)
        self.vista_datos.columnconfigure(0, weight=1)
        self.vista_datos.rowconfigure(0, weight=1)

        # Ejecutar el loop principal
        self.ventana.mainloop()

    def actualizar_vista_datos(self):
        # Eliminar todos los widgets hijos de la vista de los datos
        for widget in self.vista_datos.winfo_children():
            widget.destroy()

        # Crear los widgets de la vista de los datos
        for row, registro in enumerate(self.data):
            for column, valor in enumerate(registro):
                etiqueta = tk.Label(self.vista_datos, text=valor)
                etiqueta.grid(row=row, column=column, padx=5, pady=5)

    def ingresar(self):
        # Crear la ventana para ingresar un registro nuevo
        ventana_nuevo_registro = tk.Toplevel(self.ventana)

        # Crear los widgets de la ventana de ingreso
        tk.Label(ventana_nuevo_registro, text="Campo 1:").grid(row=0, column=0, padx=5, pady=5)
        input1 = tk.Entry(ventana_nuevo_registro)
        input1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(ventana_nuevo_registro, text="Campo 2:").grid(row=1, column=0, padx=5, pady=5)
        input2 = tk.Entry(ventana_nuevo_registro)
        input2.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventana_nuevo_registro, text="Campo 3:").grid(row=2, column=0, padx=5, pady=5)
        input3 = tk.Entry(ventana_nuevo_registro)
        input3.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(ventana_nuevo_registro, text="Guardar", command=lambda: self.guardar_registro(input1.get(), input2.get(), input3.get(), opcion1.get(), input4.get(), opcion2.get(), input5.get(), opcion3.get(), input6.get(), opcion4.get())).grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def guardar_registro(self, campo1, campo2, campo3, opcion1, campo4, opcion2, campo5, opcion3, campo6, opcion4):
        # Agregar el nuevo registro a la lista de datos
        registro = [campo1, campo2, campo3, opcion1, campo4, opcion2, campo5, opcion3, campo6, opcion4]
        self.data.append(registro)

        # Actualizar la vista de los datos
        self.actualizar_vista_datos()

        # Cerrar la ventana de ingreso de datos
        self.ventana.winfo_children()[0].destroy()

    def exportar_csv(self):
        # Obtener el nombre de archivo del usuario
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])

        if nombre_archivo:
            try:
                # Escribir los datos en el archivo CSV
                with open(nombre_archivo, mode="w", newline="") as archivo:
                    writer = csv.writer(archivo)
                    writer.writerows(self.data)

                messagebox.showinfo("Éxito", "Los datos han sido exportados a CSV.")
            except:
                messagebox.showerror("Error", "Ha ocurrido un error al exportar los datos a CSV.")

def importar_csv(self):
    # Obtener el nombre de archivo del usuario
    nombre_archivo = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])

    if nombre_archivo:
        try:
            # Leer los datos del archivo CSV
            with open(nombre_archivo, mode="r") as archivo:
                reader = csv.reader(archivo)
                self.data = list(reader)

            # Actualizar la vista de los datos
            self.actualizar_vista_datos()

            messagebox.showinfo("Éxito", "Los datos han sido importados desde CSV.")
        except:
            messagebox.showerror("Error", "Ha ocurrido un error al importar los datos desde CSV.")


                messagebox.showinfo("Éxito", "Los datos han sido importados desde CSV.")
            except:
                messagebox.showerror("Error", "Ha ocurrido un error al importar los datos desde CSV.")

app = App()
