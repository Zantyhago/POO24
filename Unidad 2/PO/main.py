from gestorclientes import GestorCliente
from gestormovimientos import GestorMovimiento

if __name__ == '__main__':
    gestMov = GestorMovimiento
    gestCli = GestorCliente
    opcion = input("Seleccione una opcion:\na: Actualizar saldo.\nb: Mostrar movomientos.\nc: Ordenar movimientos.\nd: Salir.\n")
    while opcion != 'd':
        if opcion == 'a':
            xdni = input("Ingrese DNI: ")
            apell, nomb, numacc, saldAnt = gestCli.buscasaldOld(xdni)
            print(f"""
                    Cliente: {apell} {nomb}           Numero de Cuenta: {numacc}
                    Saldo Anterior: {saldAnt}
                    Movimientos
                    Fecha           Descripcion             Importe         Tipo De Movimiento""")
            fecha, descr, imp, type = gestMov.actualiza(numacc, saldAnt)
            print(f"""
                    {fecha}         {descr}                 {imp}           {type}
                    Saldo Actualizado: {saldAnt}""")
        elif opcion == 'b':
            xdni = input("Ingrese DNI: ")
            apell, nomb, numacc = gestCli.buscacli(xdni)
            band = gestMov.buscarmov(numacc)
            if band:
                print("El cliente {} {} tuvo movimientos en el mes corriente.".format(apell, nomb))
            else:
                print("El cliente {} {} no tuvo movimientos en el mes corriente.".format(apell, nomb))
        elif opcion == 'c':
                print("Listado de clientes sin ordenar:")
                gestMov.muestra()
                print("Listado de clientes ordenada:")
                gestMov.ordena()
                gestMov.muestra()
        else:
             print("Dale amigo no es tan dificil.")
             opcion = 'd'

    print("See u next time (ojalá no en el extracoso)")