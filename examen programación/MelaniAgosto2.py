Tareas = []

while True:

 print("""
 1. Añadir una tarea 
 2. Ver todas las tareas  
 3. Marcar una tarea completada
 4. salir                         
  """)
  
  tarea = int(input("Por favor ingrese el número de lo que desea hacer: "))

  if tarea == 1:
     tarea = input("Escriba aquí la tarea que quiera añadir: ")
     Tareas.append(tarea)

  elif tarea == 2:
    print(Tareas)

  elif tarea == 3:
    print(Tareas)
    TareaCompleta = int(input("Ingrese el número de la tarea completada sabiendo que empieza desde el cero: "))
    Tareas.remove(TareaCompleta)

  else:
    print("Gracias por utilizar nuestra gestion de tareas.")

    break
   