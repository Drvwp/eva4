import requests

def get_items():
    response = requests.get('http://localhost:8000/get_items/')
    if response.status_code == 200:
        programmers = response.json()
        for programmer in programmers:
            print(f"ID: {programmer['id']}, Nombre: {programmer['fullname']}, Apodo: {programmer['nickname']}, Edad: {programmer['age']}, Activo: {programmer['is_active']}")
    else:
        print("Error al obtener los programadores.")

def create_item():
    fullname = input("Ingrese el nombre completo del programador: ")
    nickname = input("Ingrese el apodo del programador: ")
    age = int(input("Ingrese la edad del programador: "))
    is_active = input("¿Está activo? (sí/no): ").strip().lower() == 'sí'
    response = requests.post('http://localhost:8000/create_item/', json={
        'fullname': fullname,
        'nickname': nickname,
        'age': age,
        'is_active': is_active
    })
    if response.status_code == 201:
        print("Item creado exitosamente.")
    else:
        print("Error al crear el item.")

def update_item():
    item_id = int(input("Ingrese el ID del programador a actualizar: "))
    fullname = input("Ingrese el nuevo nombre completo del programador: ")
    nickname = input("Ingrese el nuevo apodo del programador: ")
    age = int(input("Ingrese la nueva edad del programador: "))
    is_active = input("¿Está activo? (sí/no): ").strip().lower() == 'sí'
    response = requests.put(f'http://localhost:8000/update_item/{item_id}/', json={
        'fullname': fullname,
        'nickname': nickname,
        'age': age,
        'is_active': is_active
    })
    if response.status_code == 200:
        print("Item actualizado exitosamente.")
    else:
        print("Error al actualizar el item.")

def delete_item():
    item_id = int(input("Ingrese el ID del programador a eliminar: "))
    response = requests.delete(f'http://localhost:8000/delete_item/{item_id}/')
    if response.status_code == 204:
        print("Item eliminado exitosamente.")
    else:
        print("Error al eliminar el item.")

def menu():
    while True:
        print("\nMenú CRUD")
        print("1. Leer todos los programadores")
        print("2. Crear un programador")
        print("3. Actualizar un programador")
        print("4. Eliminar un programador")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            get_items()
        elif choice == '2':
            create_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
