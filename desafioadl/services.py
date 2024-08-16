from desafioadl.models import Tarea, SubTarea

def crear_nueva_tarea(texto:str):
    tarea = Tarea(descripcion=texto)
    tarea.save()
    # imprimir en pantalla

def crear_sub_tarea(texto:str, idtarea:int):
    tarea_encontrada = Tarea.objects.get(id=idtarea)
    subtarea = SubTarea(descripcion=texto, tarea=tarea_encontrada)
    subtarea.save()
    # imprimir en pantalla
