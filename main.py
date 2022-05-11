print("1 -> Crear nuevo pedido")
print("2 -> Repartir datos automaticamente")
i = input('Que operacion vas a realizar?\n')
if(i == '1'):
    from nuevopedido.nuevopedido import main
    main()

elif(i == '2'):
    from autorepartir.autorepartidor import main
    main()