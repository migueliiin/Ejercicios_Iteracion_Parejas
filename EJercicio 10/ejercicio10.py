class persona:
        edad=0
        id = -1
        id_padre=0
        id_madre=0
        def __init__(self, nombre,edad,id,id_padre,id_madre):
            self.nombre=nombre
            self.edad = edad
            self.id = id
            self.id_padre=id_padre
            self.id_madre=id_madre

personas=[]
for i in range (0,1000):
    personas.append(persona)

def crear_persona():
    acabado=False
    n=str(input('Elija un nombre:'))
    e=int(input('Cual es su edad:'))
    id_p=int(input('Id del padre (si no tiene introduzca el valor 0):'))
    id_m=int(input('Id de la madre (si no tiene introduzca el valor 0):'))
    while(acabado==False):
        id=int(input('Introduzca el id que desea:'))
        if(id!=persona.id or persona.id==-1):
            personas.append(persona(n,e,id,id_p,id_m))
            acabado=True
        else:
            print('Elija un id nuevo')

def sumar_edad():
    for i in range (0,1000):
        if(persona.id!=-1):
            persona.edad=persona.edad+1
        else:
            i=i+1


fin=False
while(fin==False):
    r1=str(input('Quieres crear una  nueva persona?:'))
    if(r1=='s'or r1=='S'):
        crear_persona()
    if(r1=='n'or r1=='N'):
        fin=True
    else:
        print('Introduzca una S o una N')

fin2=False
while(fin2==False):
    r2=str(input('Quieres sumarle 1 año a todas las personas de la lista?:'))
    if(r2=='s'or r2=='S'):
        sumar_edad()
    if(r2=='n'or r2=='N'):
        fin=True
    else:
        print('Introduzca una S o una N')