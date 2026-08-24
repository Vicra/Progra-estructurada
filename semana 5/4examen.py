class Song:
  # Constructor
  def __init__(self, title, artist, genre, duration, year):
    self.title = title
    self.artist = artist
    self.genre = genre
    self.duration = duration
    self.year = year

class Playlist:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c


songs = [
  Song("I Want you back", "MJ", "Pop", 200, 1980),
  Song("Thriller", "MJ", "Pop", 200, 1982),
  Song("Beat it", "MJ", "RnB", 200, 1982),
]

while True:
  print("")
  print("MENU")
  print("1. Mostrar todas las canciones")
  print("2. Agregar cancion")
  print("3. Borrar cancion")
  print("4. Buscar cancion")
  print("5. Mostrar duracion total")
  print("0. SALIR")

  option = int(input("Ingrese una opcion: "))

  match option:
    case 1:
      print("")
      print("---- LISTA DE CANCIONES ----")
      for i in range(len(songs)):
        print(i+1, songs[i].title, songs[i].artist, songs[i].genre, songs[i].duration, songs[i].year)

    case 2:
      print("")
      print("AGREGAR UNA NUEVA CANCION")
      title = input("Ingrese el titulo: ")
      artista = input("Ingrese el artista: ")
      genero = input("Ingrese el genero: ")
      duracion = int(input("Ingrese la duracion (en segs): "))
      year = int(input("Ingrese el ańo: "))

      if duracion <= 0:
        print("Duracion tiene que ser mayor a 0")
      elif year < 1900 or year > 2026:
        print("Año tiene que estar entre 1900-2026")
      else:
        songs.append(
          Song(
            title, artista, genero, duracion, year
          )
        )

    case 3:
      if(len(songs) <= 0):
        print("")
        print("No hay canciones por borrar")
      else:
        print("")
        print("BORRAR UNA CANCION")
        for i in range(len(songs)):
                print(i+1, songs[i].title, songs[i].artist, songs[i].genre, songs[i].duration, songs[i].year)
        indiceABorrar = int(input("Ingrese el indice de la cancion a borrar: "))

        if indiceABorrar < 0 or indiceABorrar > len(songs):
          print("Indice incorrecto, no se borro")
        else:
          cancionBorrada = songs.pop(indiceABorrar-1)
          print("Borrado con exito: ", cancionBorrada.title)

    case 4:
      print("")
      print("BUSCAR")
      filtro = input("Ingrese el genero a buscar:")

      for i in range(len(songs)):
        if(songs[i].genre == filtro):
          print(songs[i].title, songs[i].artist, songs[i].genre)

    case 5:
      print("")
      duracionTotal = 0
      for i in range(len(songs)):
        duracionTotal = duracionTotal + songs[i].duration
      print("Duracion total de canciones en segundos: ", duracionTotal)
    case 0:
      print("")
      print("Goodbye...")
      break

    case _:
      print("Opcion invalida")