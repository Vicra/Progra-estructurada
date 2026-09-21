def mostrar_resumen(ordenes):
  print("RESUMEN")
  print("Total de Ordenes:", len(ordenes.keys()))
  totalVentas = 0

  for value in ordenes.values():
    totalVentas = totalVentas + value["total"]

  print("Total Ventas:", totalVentas)