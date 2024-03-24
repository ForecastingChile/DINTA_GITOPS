Construir la imagen
docker build -t gpu_test .

Ejecutar la imagen y ejecutar el comando "nvidia_smi" para probar la funcionalidad dentro del contenedor
docker run --gpus all -it --rm gpu_test nvidia-smi

Ejecutar la imagen y exponer el api en el puerto 8083
docker run --gpus all -it --rm -p 8083:8083 gpu_test
