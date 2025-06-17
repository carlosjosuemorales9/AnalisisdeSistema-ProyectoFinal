import tkinter as tk
from tkinter import messagebox
import json, os

# Funciones generales de archivo
def cargar_datos(nombre):
    if os.path.exists(nombre):
        with open(nombre, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_datos(nombre, datos):
    with open(nombre, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

# Archivos de datos
alumnos = cargar_datos("alumnos.json")
docentes = cargar_datos("docentes.json")
materias = cargar_datos("materias.json")
grupos = cargar_datos("grupos.json")
calificaciones = cargar_datos("calificaciones.json")

# -------------------- Ventanas --------------------
def ventana_alumnos():
    win = tk.Toplevel(root)
    win.title("Gestión de Alumnos")

    def guardar():
        c = e_control.get()
        alumnos[c] = {
            "nombre": e_nombre.get(),
            "apellidos": e_apellidos.get(),
            "direccion": e_direccion.get(),
            "telefono": e_telefono.get(),
            "nacimiento": e_nacimiento.get()
        }
        guardar_datos("alumnos.json", alumnos)
        messagebox.showinfo("Éxito", "Alumno guardado.")

    def buscar():
        c = e_control.get()
        a = alumnos.get(c)
        if a:
            e_nombre.delete(0, tk.END); e_nombre.insert(0, a["nombre"])
            e_apellidos.delete(0, tk.END); e_apellidos.insert(0, a["apellidos"])
            e_direccion.delete(0, tk.END); e_direccion.insert(0, a["direccion"])
            e_telefono.delete(0, tk.END); e_telefono.insert(0, a["telefono"])
            e_nacimiento.delete(0, tk.END); e_nacimiento.insert(0, a["nacimiento"])
        else:
            messagebox.showerror("Error", "No encontrado")

    def eliminar():
        c = e_control.get()
        if c in alumnos:
            del alumnos[c]
            guardar_datos("alumnos.json", alumnos)
            messagebox.showinfo("Listo", "Eliminado")

    labels = ["Control", "Nombre", "Apellidos", "Dirección", "Teléfono", "Nacimiento"]
    entries = []
    for l in labels:
        tk.Label(win, text=l).pack()
        ent = tk.Entry(win)
        ent.pack()
        entries.append(ent)
    e_control, e_nombre, e_apellidos, e_direccion, e_telefono, e_nacimiento = entries

    tk.Button(win, text="Guardar", command=guardar).pack()
    tk.Button(win, text="Buscar", command=buscar).pack()
    tk.Button(win, text="Eliminar", command=eliminar).pack()

def ventana_docentes():
    win = tk.Toplevel(root)
    win.title("Gestión de Docentes")

    def guardar():
        c = e_clave.get()
        docentes[c] = {
            "nombre": e_nombre.get(),
            "apellidos": e_apellidos.get(),
            "categoria": e_categoria.get(),
            "horas": e_horas.get(),
            "horario": e_horario.get()
        }
        guardar_datos("docentes.json", docentes)
        messagebox.showinfo("Guardado", "Docente guardado.")

    def buscar():
        c = e_clave.get()
        d = docentes.get(c)
        if d:
            e_nombre.delete(0, tk.END); e_nombre.insert(0, d["nombre"])
            e_apellidos.delete(0, tk.END); e_apellidos.insert(0, d["apellidos"])
            e_categoria.delete(0, tk.END); e_categoria.insert(0, d["categoria"])
            e_horas.delete(0, tk.END); e_horas.insert(0, d["horas"])
            e_horario.delete(0, tk.END); e_horario.insert(0, d["horario"])
        else:
            messagebox.showerror("Error", "No encontrado")

    def eliminar():
        c = e_clave.get()
        if c in docentes:
            del docentes[c]
            guardar_datos("docentes.json", docentes)
            messagebox.showinfo("Listo", "Docente eliminado")

    labels = ["No. Empleado", "Nombre", "Apellidos", "Categoría", "Horas", "Horario"]
    entries = []
    for l in labels:
        tk.Label(win, text=l).pack()
        ent = tk.Entry(win)
        ent.pack()
        entries.append(ent)
    e_clave, e_nombre, e_apellidos, e_categoria, e_horas, e_horario = entries

    tk.Button(win, text="Guardar", command=guardar).pack()
    tk.Button(win, text="Buscar", command=buscar).pack()
    tk.Button(win, text="Eliminar", command=eliminar).pack()

def ventana_materias():
    win = tk.Toplevel(root)
    win.title("Gestión de Materias")

    def guardar():
        c = e_clave.get()
        materias[c] = {
            "nombre": e_nombre.get(),
            "descripcion": e_descripcion.get(),
            "plan": e_plan.get()
        }
        guardar_datos("materias.json", materias)
        messagebox.showinfo("Guardado", "Materia guardada.")

    def buscar():
        c = e_clave.get()
        m = materias.get(c)
        if m:
            e_nombre.delete(0, tk.END); e_nombre.insert(0, m["nombre"])
            e_descripcion.delete(0, tk.END); e_descripcion.insert(0, m["descripcion"])
            e_plan.delete(0, tk.END); e_plan.insert(0, m["plan"])
        else:
            messagebox.showerror("Error", "No encontrada")

    def eliminar():
        c = e_clave.get()
        if c in materias:
            del materias[c]
            guardar_datos("materias.json", materias)
            messagebox.showinfo("Listo", "Materia eliminada")

    labels = ["Clave", "Nombre", "Descripción", "Plan de estudios"]
    entries = []
    for l in labels:
        tk.Label(win, text=l).pack()
        ent = tk.Entry(win)
        ent.pack()
        entries.append(ent)
    e_clave, e_nombre, e_descripcion, e_plan = entries

    tk.Button(win, text="Guardar", command=guardar).pack()
    tk.Button(win, text="Buscar", command=buscar).pack()
    tk.Button(win, text="Eliminar", command=eliminar).pack()

def ventana_grupos():
    win = tk.Toplevel(root)
    win.title("Agregar Grupo")

    def guardar():
        c = e_clave.get()
        grupos[c] = {
            "docente": e_docente.get(),
            "materia": e_materia.get(),
            "horario": e_horario.get()
        }
        guardar_datos("grupos.json", grupos)
        messagebox.showinfo("Listo", "Grupo guardado.")

    labels = ["Clave Grupo", "Docente (número)", "Materia (clave)", "Horario"]
    entries = []
    for l in labels:
        tk.Label(win, text=l).pack()
        ent = tk.Entry(win)
        ent.pack()
        entries.append(ent)
    e_clave, e_docente, e_materia, e_horario = entries

    tk.Button(win, text="Guardar", command=guardar).pack()

def ventana_calificaciones():
    win = tk.Toplevel(root)
    win.title("Registrar Calificaciones")

    tk.Label(win, text="Clave grupo:").pack()
    e_grupo = tk.Entry(win); e_grupo.pack()

    tk.Label(win, text="Clave materia:").pack()
    e_materia = tk.Entry(win); e_materia.pack()

    tk.Label(win, text="Horario:").pack()
    e_horario = tk.Entry(win); e_horario.pack()

    def guardar():
        for c, a in alumnos.items():
            cal = simpledialog.askstring("Nota", f"Calificación de {a['nombre']} {a['apellidos']}")
            calificaciones[c] = {
                "grupo": e_grupo.get(),
                "materia": e_materia.get(),
                "horario": e_horario.get(),
                "calificacion": cal
            }
        guardar_datos("calificaciones.json", calificaciones)
        messagebox.showinfo("Listo", "Calificaciones guardadas.")

    from tkinter import simpledialog
    tk.Button(win, text="Registrar Calificaciones", command=guardar).pack(pady=10)

# -------------------- Ventana Principal --------------------
root = tk.Tk()
root.title("Sistema Escolar")
root.geometry("300x400")

tk.Label(root, text="SISTEMA ESCOLAR", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Gestión de Alumnos", width=25, command=ventana_alumnos).pack(pady=5)
tk.Button(root, text="Gestión de Docentes", width=25, command=ventana_docentes).pack(pady=5)
tk.Button(root, text="Gestión de Materias", width=25, command=ventana_materias).pack(pady=5)
tk.Button(root, text="Agregar Grupos", width=25, command=ventana_grupos).pack(pady=5)
tk.Button(root, text="Calificar Alumnos", width=25, command=ventana_calificaciones).pack(pady=5)

tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=30)

root.mainloop()
