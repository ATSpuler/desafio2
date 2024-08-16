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
def elimina_tarea(idtarea:int):
    t = Tarea.objects.get(id=idtarea) 
    t.eliminada = True
    t.save()

def elimina_sub_tarea(idsubtarea:int):
    st = SubTarea.objects.get(id=idsubtarea) 
    st.eliminada = True
    st.save()

def matar_tarea(idtarea:int):
    t = Tarea.objects.get(id=idtarea)
    t.delete()