#!/bin/bash

# Directorio donde están los scripts
SCRIPT_DIR="/root/Dashproject/dbscripts/sociodemografico"

# Base de Datos a la que se hace conexion
DATABASE="sociodemografico"

# Usuario asignado para entrar a MySQL
USER="root"

# Pedir la contraseña una vez
echo -n "Ingresa tu password de MySQL: "
read -s PASSWORD
echo

# Importa todos los scripts alojados en el directorio
for script in $SCRIPT_DIR/*.sql; do
    echo "Importando $script en la base de datos $DATABASE..."
    mysql -u $USER -p$PASSWORD $DATABASE < $script
    if [ $? -eq 0 ]; then
        echo "$script importado exitosamente."
    else
        echo "Error importando $script."
    fi
done

echo "Todos los scripts han sido importados."
