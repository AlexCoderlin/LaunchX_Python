def main():
    #except Exception: #Capta todas las excepciones.

    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError): # Agrupamos varias excepciones.
        print("Filesystem under heavy load, can't complete reading configuration file")

    try:
         open("config.txt")
    except OSError as err: # as permite convertir a "err" en una variable que contine mas datos asociados del error.
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")

if __name__ == '__main__':
    main()