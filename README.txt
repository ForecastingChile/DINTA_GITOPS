Construir la imagen
- docker build -t gpu_test .

Ejecutar la imagen y ejecutar el comando "nvidia_smi" para probar la funcionalidad dentro del contenedor
- docker run --gpus all -it --rm gpu_test nvidia-smi

Ejecutar la imagen y exponer el api en el puerto 8083
- docker run --gpus all -it --rm -p 8083:8083 gpu_test

Comandos ARGO Comandos

- kubectl create namespace argocd
- kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
- kubectl port-forward svc/argocd-server -n argocd 8080:443

- argo admin initial-password -n argocd

