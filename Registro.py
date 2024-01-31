import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.definir_patrones_validaciones()

    def inicializar_gui(self):
        self.title('Validación de Datos')
        self.minsize(400,350)

        lbl_titulo = tk.Label(self, text='FORMULARIO DE REGISTRO')
        lbl_titulo.grid(row=0, column=1, pady=10)

        frm_principal = tk.Frame(self, bd=7, relief='groove')
        frm_principal.grid(row=1, column=1, padx=10, pady=10)

        lbl_nombre = tk.Label(frm_principal, text='Nombre:')
        lbl_nombre.grid(row=0, column=0, sticky=tk.W)
        self.txt_nombre = tk.Entry(frm_principal, width=20)
        self.txt_nombre.grid(row=0, column=1)

        lbl_apellido = tk.Label(frm_principal, text='Apellido:')
        lbl_apellido.grid(row=1, column=0, sticky=tk.W)
        self.txt_apellido = tk.Entry(frm_principal, width=20)
        self.txt_apellido.grid(row=1, column=1)

        lbl_fecha_nacimiento = tk.Label(frm_principal, text='Fecha de Nacimiento:')
        lbl_fecha_nacimiento.grid(row=2, column=0, sticky=tk.W)
        self.txt_fecha_nacimiento = tk.Entry(frm_principal, width=20)
        self.txt_fecha_nacimiento.grid(row=2, column=1)

        lbl_pais = tk.Label(frm_principal, text='País:')
        lbl_pais.grid(row=3, column=0, sticky=tk.W)
        self.cbx_pais = ttk.Combobox(frm_principal, width=20)
        paises = ('Argentina', 'Bolivia', 'Brasil', 'Colombia', 'Ecuador', 'Paraguay', 'Perú', 'Uruguay', 'Venezuela')
        self.cbx_pais['values'] = paises
        self.cbx_pais.current(0)
        self.cbx_pais.grid(row=3, column=1)

        lbl_email = tk.Label(frm_principal, text='Email:')
        lbl_email.grid(row=4, column=0, sticky=tk.W)
        self.txt_email = tk.Entry(frm_principal, width=20)
        self.txt_email.grid(row=4, column=1)

        lbl_numero_telefono = tk.Label(frm_principal, text='Número de Teléfono:')
        lbl_numero_telefono.grid(row=5, column=0, sticky=tk.W)
        self.txt_numero_telefono = tk.Entry(frm_principal, width=20)
        self.txt_numero_telefono.grid(row=5, column=1)

        lbl_contrasenna = tk.Label(frm_principal, text='Contraseña:')
        lbl_contrasenna.grid(row=6, column=0, sticky=tk.W)
        self.txt_contrasenna = tk.Entry(frm_principal, width=20)
        self.txt_contrasenna.grid(row=6, column=1)

        lbl_repetir_contrasenna = tk.Label(frm_principal, text='Repetir Contraseña:')
        lbl_repetir_contrasenna.grid(row=7, column=0, sticky=tk.W)
        self.txt_repetir_contrasenna = tk.Entry(frm_principal, width=20)
        self.txt_repetir_contrasenna.grid(row=7, column=1)

        btn_guardar = tk.Button(frm_principal, text='Guardar', command=self.guardar)
        btn_guardar.grid(row=7, column=2)

        btn_limpiar = tk.Button(frm_principal, text='Limpiar', command=self.limpiar)
        btn_limpiar.grid(row=7, column=3)

        btn_salir = tk.Button(frm_principal, text='Salir', command=self.salir)
        btn_salir.grid(row=7, column=4)

        
    def definir_patrones_validaciones(self):

        patron_nombre = r'(^[A-ZÁÉÍÓÚ]{1}([a-zñáéíóú]+){2,})(\s[A-ZÁÉÍÓÚ]{1}([a-zñáéíóú]+){2,})?$'
        self.regex_nombre = re.compile(patron_nombre)

        patron_apellido = r'(^[A-ZÁÉÍÓÚ]{1}([a-zñáéíóú]+){2,})(\s[A-ZÁÉÍÓÚ]{1}([a-zñáéíóú]+){2,})?$'
        self.regex_apellido = re.compile(patron_apellido)

        patron_fecha_nacimiento = r'^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$'
        self.regex_fecha_nacimiento = re.compile(patron_fecha_nacimiento) 

        patron_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.regex_email = re.compile(patron_email)

        patron_numero_telefono = r'^\+?58?[0-9]{10}$'
        self.regex_numero_telefono = re.compile(patron_numero_telefono)

        patron_contrasenna = r'^[a-zA-Z0-9]{8,16}$'
        self.regex_contrasenna = re.compile(patron_contrasenna)


    def guardar(self):
        nombre = self.txt_nombre.get().strip()
        if re.match(self.regex_nombre, nombre) is None:
            messagebox.showwarning('Mensaje', 'El campo Nombre debe incluir un nombre válido')
            return
        
        apellido = self.txt_apellido.get()
        if re.match(self.regex_apellido, apellido) is None:
            messagebox.showwarning('Mensaje', 'El campo Apellido debe incluir un apellido válido')
            return
        
        fecha_nacimiento = self.txt_fecha_nacimiento.get()
        if re.match(self.regex_fecha_nacimiento, fecha_nacimiento) is None:
            messagebox.showwarning('Mensaje', 'El campo Fecha de nacimiento debe incluir un formato válido')
            return
        
        email = self.txt_email.get()
        if re.match(self.regex_email, email) is None:
            messagebox.showwarning('Mensaje', 'El campo Email debe incluir un formato válido')
            return
        
        numero_telefono = self.txt_numero_telefono.get()
        if re.match(self.regex_numero_telefono, numero_telefono) is None:
            messagebox.showwarning('Mensaje', 'El campo debe incluir un Número de teléfono válido')
            return

        contrasenna = self.txt_contrasenna.get()
        if re.match(self.regex_contrasenna, contrasenna) is None:
            messagebox.showwarning('Mensaje', 'El campo Contraseña debe incluir mínimo 8 carácteres, máximo 16')
            return
        
        repetir_contrasenna = self.txt_repetir_contrasenna.get()
        if re.match(self.regex_contrasenna, repetir_contrasenna) is None:
            messagebox.showwarning('Mensaje', 'El campo Repetir Contraseña debe incluir mínimo 8 carácteres, máximo 16')
            return
        
        if contrasenna != repetir_contrasenna:
            messagebox.showwarning('Mensaje', 'Las Contraseñas deben ser iguales')
            return
        
        messagebox.showinfo('Mensaje', 'El Registro se realizó exitosamente.')
        self.limpiar()


    def limpiar(self):
        self.txt_nombre.delete(0, 'end')
        self.txt_apellido.delete(0, 'end')
        self.txt_fecha_nacimiento.delete(0, 'end')
        self.cbx_pais.current(0)
        self.txt_email.delete(0, 'end')
        self.txt_numero_telefono.delete(0, 'end')
        self.txt_contrasenna.delete(0, 'end')
        self.txt_repetir_contrasenna.delete(0, 'end')

    def salir(self):
        self.destroy()

def main():
    app = FormularioRegistro()
    app.mainloop()

if __name__ == '__main__':
    main()

