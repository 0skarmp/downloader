from pytube import YouTube
import tkinter as tk
from tkinter import Entry, Button, Label, Radiobutton, IntVar, Menu, messagebox




#pytube ===> libreria que nos permite descargar videos de YouTube
#Tkinter ==> Librerua que nos permite crear interfaces graficas

# Función para descargar el video o audio según la opción seleccionada
def descargar():
    url = entry_url.get() # crea variable url => tomando la url 
    video = "descargas/" #variable donde se va alamcenar la descarga
    musica = "musica/"
    try:
        yt = YouTube(url) #instancia de la clase que toma como valores Youtube y la url que se le brindara
        if opcion.get() == 1:  # Descargar video
            video_stream = yt.streams.get_highest_resolution()# obtiene la mejor caliadd del video
            video_stream.download(output_path=video) #descarga el video y lo alamcena en la variable video 
            mensaje.config(text="El video fue descargado correctamente.") 
        elif opcion.get() == 2:  # Descargar audio
            audio_stream = yt.streams.filter(only_audio=True).first() #descarga solamente el audio y en la mejor caliadd
            audio_stream.download(output_path=musica)# descarga el audio y lo alamcena en la varaible musica
            mensaje.config(text="El audio fue descargado correctamente.")
    except Exception as e:
        mensaje.config(text=f"Error: {str(e)}")

def popup():
    messagebox.showinfo("Sobre el autor", "Enlace a mi perfil de Instagram: https://www.instagram.com/mposkar/")
# Crear la ventana tkinter
root = tk.Tk()
root.title("Descargador de Videos/Audio de YouTube")



# Etiqueta y entrada para el enlace del video
label_url = Label(root, text="Ingrese el enlace de YouTube:")
label_url.pack()
entry_url = Entry(root, width=50)
entry_url.pack()

# Opciones para descargar video o audio
opcion = IntVar()
opcion.set(1)  # Por defecto, se selecciona descargar video

#se usa radiobutton(widget, proporcionado por la li biblioteca tkinter)
#para crear botones
radio_video = Radiobutton(root, text="Descargar Video", variable=opcion, value=1)
radio_audio = Radiobutton(root, text="Descargar Audio", variable=opcion, value=2)

#utlizamos el meotodo pack, para colocar botones de opcion y el boton de descarga en ventana
#ajusta  automaticamente la posicion y coloca los widgets de manera ordenada
radio_video.pack()
radio_audio.pack()

# Se crea el botón para descargar/ y tambien se usa el metodo pack
btn_descargar = Button(root, text="Descargar", command=descargar)
btn_descargar.pack()

# Etiqueta para mostrar mensajes cuando el video es mostrado tomando la variable text que ya fue instanciada
#se usa el metodo pack 
mensaje = Label(root, text="")
mensaje.pack()

menubar =Menu(root) # widget menu
root.config(menu=menubar) #configurar dentro de la root el menu
helpmenu=(Menu(menubar, tearoff=0))

#crear estilos para el boton mas informacion
menubar.add_cascade(label="para mas informacion", menu=helpmenu)
#creando el mensaje dentro del menu desplegable 
helpmenu.add_command(label="informacion del autor", command=popup)

#creando estilo boton salir/ se cuerra la ventana
menubar.add_cascade(label="salir", command=root.destroy)

#creando instrucciones, con salto de linea
instrucciones = Label(root, text="Programa creado en python para descargar videos de youtube\n")
#definir posicion
#instrucciones.grid(row=0, column=1)

# Función para cerrar la ventana
def cerrar_ventana():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

#permite que tu aplicación tkinter sea interactiva 
#y responda a las acciones del usuario, como hacer clic en botones, 
#ingresar datos y cerrar la ventana 
root.mainloop()
