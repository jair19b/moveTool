import os
import shutil

# Obtine la ubiccion actual
current_dir_os = os.getcwd()
print("[!] Ruta actual: ", current_dir_os)
current_dir = input("[?] Ingrese la ruta origen de los archivosa mover (incluyendo la unidad): ")

# Preguntar la ubicacion para mover los archivos
destination_dir = input("[?] Ingrese la ruta del directorio de destino: ")

# Preguntar la extencion de archivo al usuario
extention = input("[?] Ingrese la extencion de los archivos a mover: (.jpg, .png, .gif) ")

# Pregunta si incluir subdirectorios
subdirs = input("[?] Incluir subdirectorios: [1] si [2] No ")

# control de seguridad del script
limite = int(input("[?] Limite máximo de archivos a mover por ejecucion: "))
if limite and (limite > 100 and limite < 5000):
   limit = limite
else:
   limit = 100

# Comprueba si el directorio existe y lo crea si no existe
if not os.path.exists(destination_dir):
   os.makedirs(destination_dir)

# validar procedimiento de acuerdo a decicion de usuario
control = 0
if subdirs == 0:
   for filename in os.listdir(current_dir):
      if control > limit:
         break
      
      if filename.endswith(extention):
         source_file = os.path.join(current_dir, filename)
         destination_file = os.path.join(destination_dir, filename)
         shutil.move(source_file, destination_file)
         control = control +1
         print(f"File: {filename} moved to {destination_dir}")
else:
   for root, dirs, files in os.walk(current_dir):
      for filename in files:
         if control > limit:
            break
         if filename.endswith(extention):
            source_file = os.path.join(root, filename)
            destination_file = os.path.join(destination_dir, filename)
            shutil.move(source_file, destination_file)
            control = control +1
            print(f"File: {filename} moved to {destination_dir}")

print(f"\nSE HAN MOVIDO TODOS LOS ARCHIVOS CON EXTENCION {extention} CORRRECTAMENTE")