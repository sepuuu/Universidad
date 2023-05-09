import tkinter as tk
from tkinter import ttk
import csv

class SportsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports App")

        self.add_button = ttk.Button(self.master, text="Agregar", command=self.open_add_window)
        self.export_button = ttk.Button(self.master, text="Exportar", command=self.export_data)
        self.import_button = ttk.Button(self.master, text="Importar", command=self.import_data)

        self.tree = ttk.Treeview(self.master, columns=("minuto", "jugador_balon", "jugador_marca", "accion", "resultado", "jugador_destino", "jugador_marca_destino", "zona_accion", "zona_destino"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("minuto", text="Minuto")
        self.tree.heading("jugador_balon", text="Jugador con Balón")
        self.tree.heading("jugador_marca", text="Jugador Marca")
        self.tree.heading("accion", text="Acción")
        self.tree.heading("resultado", text="Resultado")
        self.tree.heading("jugador_destino", text="Jugador Destino")
        self.tree.heading("jugador_marca_destino", text="Jugador Marca Destino")
        self.tree.heading("zona_accion", text="Zona Acción")
        self.tree.heading("zona_destino", text="Zona Destino")
        self.tree.column("#0", width=50)

        self.add_button.pack(padx=10, pady=10)
        self.export_button.pack(padx=10, pady=10)
        self.import_button.pack(padx=10, pady=10)
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def open_add_window(self):
        add_window = tk.Toplevel(self.master)

        minute_label = ttk.Label(add_window, text="Minuto:")
        minute_entry = ttk.Entry(add_window)
        player_with_ball_button = ttk.Button(add_window, text="Jugador con Balón", command=lambda: self.open_player_window(add_window))
        player_defender_button = ttk.Button(add_window, text="Jugador Marca", command=lambda: self.open_player_window(add_window))
        action_label = ttk.Label(add_window, text="Acción:")
        action_entry = ttk.Entry(add_window)
        result_label = ttk.Label(add_window, text="Resultado:")
        result_entry = ttk.Entry(add_window)
        player_destination_button = ttk.Button(add_window, text="Jugador Destino", command=lambda: self.open_player_window(add_window))
        player_defender_destination_button = ttk.Button(add_window, text="Jugador Marca Destino", command=lambda: self.open_player_window(add_window))
        action_zone_label = ttk.Label(add_window, text="Zona Acción:")
        action_zone_entry = ttk.Entry(add_window)
        destination_zone_label = ttk.Label(add_window, text="Zona Destino:")
        destination_zone_entry = ttk.Entry(add_window)
        destination_zone_entry = ttk.Entry(add_window)
        submit_button = ttk.Button(add_window, text="Submit", command=lambda: self.save_data(add_window, minute_entry.get(), player_with_ball_button['text'], player_defender_button['text'], action_entry.get(), result_entry.get(), player_destination_button['text'], player_defender_destination_button['text'], action_zone_entry.get(), destination_zone_entry.get()))
        submit_button.pack(padx=10, pady=10)

        minute_label.pack(padx=10, pady=10)
        minute_entry.pack(padx=10, pady=10)
        player_with_ball_button.pack(padx=10, pady=10)
        player_defender_button.pack(padx=10, pady=10)
        action_label.pack(padx=10, pady=10)
        action_entry.pack(padx=10, pady=10)
        result_label.pack(padx=10, pady=10)
        result_entry.pack(padx=10, pady=10)
        player_destination_button.pack(padx=10, pady=10)
        player_defender_destination_button.pack(padx=10, pady=10)
        action_zone_label.pack(padx=10, pady=10)
        action_zone_entry.pack(padx=10, pady=10)
        destination_zone_label.pack(padx=10, pady=10)
        destination_zone_entry.pack(padx=10, pady=10)
        submit_button.pack(padx=10, pady=10)

    def open_player_window(self, parent):
        player_window = tk.Toplevel(parent)
        for i in range(22):
            if i < 11:
                button = ttk.Button(player_window, text="Button {}".format(i+1))
                button.grid(row=i, column=0, padx=5, pady=5)
                entry = ttk.Entry(player_window)
                entry.grid(row=i, column=1, padx=5, pady=5)
            else:
                button = ttk.Button(player_window, text="Button {}".format(i+1))
                button.grid(row=i-11, column=2, padx=5, pady=5)
                entry = ttk.Entry(player_window)
                entry.grid(row=i-11, column=3, padx=5, pady=5)

    def save_data(self, parent, minute, player_with_ball, player_defender, action, result, player_destination, player_defender_destination, action_zone, destination_zone):
        self.tree.insert("", "end", text="1", values=(minute, player_with_ball, player_defender, action, result, player_destination, player_defender_destination, action_zone, destination_zone))
        parent.destroy()

    def export_data(self):
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Minuto", "Jugador con Balón", "Jugador Marca", "Acción", "Resultado", "Jugador Destino", "Jugador Marca Destino", "Zona Acción", "Zona Destino"])
            for item in self.tree.get_children():
                values = self.tree.item(item)["values"]
                writer.writerow([item, values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8]])

    def import_data(self):
        with open("data.csv") as file:
            reader = csv.reader(file)
            next(reader) # skip header
            for row in reader:
                self.tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
root = tk.Tk()
app = SportsApp(root)
root.mainloop()                
