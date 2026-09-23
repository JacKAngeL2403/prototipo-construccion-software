def juego_ingeniero():
    print("=== SIMULADOR: UN DIA EN LA VIDA DEL INGENIERO DE SISTEMAS ===")
    print("Es martes, 4:00 PM. Tu jefe te pide limpiar registros antiguos de la base de datos principal.")
    print("El sistema esta lento y la direccion presiona para resolverlo antes de salir.\n")

    print("Opcion 1: Ejecutar la limpieza directo en produccion para terminar rapido.")
    print("Opcion 2: Generar un respaldo completo antes de tocar cualquier tabla.")

    eleccion1 = input("\n¿Que decides hacer? (Escribe 1 o 2): ").strip()

    if eleccion1 == "1":
        print("\nEjecutas el comando de borrado de registros...")
        print("¡ERROR GRAVE! Por las prisas olvidaste la clausula WHERE en la consulta SQL.")
        print("Acabas de borrar toda la base de datos de clientes y transacciones.\n")

        print("Opcion A: Informar de inmediato a tu jefe y al equipo de infraestructura.")
        print("Opcion B: Intentar disimular y restaurar datos inventados antes de que se den cuenta.")

        eleccion2 = input("\n¿Cual es tu respuesta ante la crisis? (Escribe A o B): ").strip().upper()

        if eleccion2 == "A":
            print("\nTu jefe entra en panico. Aunque fuiste honesto, la perdida monetaria es millonaria.")
            print("RESULTADO: Te entregan la carta de despido inmediato y Seguridad te acompaña a la salida.")
        elif eleccion2 == "B":
            print("\nUn cliente intenta ingresar, todo colapsa y descubren tu intento de ocultarlo.")
            print("RESULTADO: Despedido por negligencia grave y la empresa evalua tomar acciones legales.")
        else:
            print("\nQuedaste en shock. El director de TI descubre el fallo y te despiden en el acto.")

    elif eleccion1 == "2":
        print("\nGeneras el respaldo correctamente. Durante la limpieza, un script pide permisos de acceso.")

        print("Opcion A: Darle permisos totales de administrador (GRANT ALL) para no perder tiempo.")
        print("Opcion B: Configurar unicamente los permisos minimos requeridos para esa tarea.")

        eleccion2 = input("\n¿Que solucion aplicas? (Escribe A o B): ").strip().upper()

        if eleccion2 == "A":
            print("\nLa limpieza termina, pero dejaste una vulnerabilidad critica de seguridad.")
            print("En la madrugada, un ciberataque vulnera esa cuenta y filtran los datos de la empresa.")
            print("RESULTADO: Despedido al dia siguiente tras la auditoria de seguridad.")
        elif eleccion2 == "B":
            print("\nEl proceso se ejecuta de forma segura. El rendimiento de la base de datos mejora un 40%.")
            print("RESULTADO: Tu jefe felicita tu prudencia y profesionalismo. Mantienes tu trabajo.")
        else:
            print("\nNo elegiste una solucion a tiempo. El proceso colgo el servidor y fuiste sancionado.")
    else:
        print("\nOpcion invalida. No tomaste ninguna decision y el tiempo expiró.")

if __name__ == "__main__":
    juego_ingeniero()