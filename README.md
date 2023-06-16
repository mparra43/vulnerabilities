# vulnerabilities

El objetivo de la aplicación es gestionar la seguridad de los diferentes sistemas que se encuentran desplegados en la infraestructura Cloud mediante el
cruce de información con los CVEs del NIST con los reportes que se encuentran de manera local

## iniciar sesión 
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/97afdbe1-021f-436c-8f99-2b30499583c5)
#visualización de todos los registros 
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/4dd95061-c7d0-458f-a0cb-fcac92df49ab)

#visualización de todos los registros NIST
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/5024a520-17b8-432a-9140-02474a4c338a)

#visualización de las vulnerabilidades gestionadas 
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/d5601827-b562-4021-bdce-82605601e330)

#filtros 
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/35161bd4-55bd-40c7-97cf-e477e30e0755)
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/8fe57825-b2ee-4426-ad6a-8962cfbf3e8e)
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/22c5dfe5-9e71-4395-b626-20d60d8f50cc)

#registro de vulnerabilidades 
![image](https://github.com/mparra43/vulnerabilities/assets/66500440/e3103975-9034-46fe-adab-fe92476940fd)


 ## Requisitos previos
 Asegúrate de tener instalados los siguientes requisitos previos antes de ejecutar la aplicación:
 
 ## Instalación
 
 1. Clona el repositorio de la aplicación en tu máquina local

## Ejecución
```bash
 2. crear archivo .env de acuerdo al ejemplo y agregar la url de la api externa 
 3. docker build -t {{nombre_de_la_imagen}} .
 4. docker run -p 8080:8080 {{nombre_de_la_imagen}}
 5. docker run -d -v $PWD/.env:/app/.env {{nombre_de_la_imagen}}
 6. docker run -d -v {{ruta_local}}:{{ruta_contenedor}} -p 8080:8080 {{nombre_de_la_imagen}}
 7. docker exect -it {{id_contenerdor }} /bin/sh
 8. python manage.py migrate 

```

## Diagrama de la solución utilizando servicios del Cloud
```bash

+-----------------------+
|    Cloud Provider     |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Load Balancer       |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Auto Scaling Group  |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Virtual Machines    |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Database Service    |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Cloud Storage       |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Container Service   |
+-----------------------+
         |
         |
         v
+-----------------------+
|   Application         |
+-----------------------+
```
