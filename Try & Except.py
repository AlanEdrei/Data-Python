aceptado = False

while aceptado == False:
    try:
        monto = float(input("Ingrese el monto deseado "))
        if monto < 0:
            raise Exception("No pongas numeros negativos my friend")
        pagos = int(input("Inica el numero de pagos "))
        if pagos < 0:
            raise Exception("No pongas numeros negativos amix")
        elif pagos > 12:
            raise Exception("El plazo máximo son 12 meses my friend")#Aun usando el error genérico, el argumento varía según cuando se presente
        pagoMen = monto/pagos
        print("Ok, entonces el pago mensual será ", pagoMen)
        aceptado = True
    except ZeroDivisionError:
        print("No podemos aceptar ésto, alguna vez tendrás que pagar")
    except ValueError:
        print("Ingresa el plazo en numero")
    except Exception as un_error:
        print(un_error.args[0]) #Exception es inncesario, solo señala que el error genérico viene a esta variable, luego imprimie solo el argumento definido arriba
