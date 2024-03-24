##Comandos Estándar para trabajar con NVIDIA GPU Container Toolkit
    Construir la imagen
    - docker build -t gpu_test .

    Ejecutar la imagen y ejecutar el comando "nvidia_smi" para probar la funcionalidad dentro del contenedor
    - docker run --gpus all -it --rm gpu_test nvidia-smi

    Ejecutar la imagen y exponer el api en el puerto 8083
    - docker run --gpus all -it --rm -p 8083:8083 gpu_test

##Comandos ARGO (Instalación y ejecución)

- kubectl create namespace argocd
- kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
- kubectl port-forward svc/argocd-server -n argocd 8080:443
- argo admin initial-password -n argocd

##Comandos Tekton (instalación y ejecución)

    kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml

    kubectl get pods --namespace tekton-pipelines --watch (Para monitorear)

##Comandos Tekton para Construir y pushear una imagen:

    1.- Hay que instalar el Tekton Pipelines: kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
    2.- Se requiere tener el CLI instalado en Windows.
    3.- Después de configurar el pipeline.yaml y el pipelinerun.yaml hay que configuruar el repositorio local de imaagenes con el siguiente comando (con almacenamiento persistente)
    4.- docker run -d -p 5000:5000 --restart=always --volume ~/.registry/storage:/var/lib/registry registry:2
    5.- Una vez que está creado el repo local la única forma de ver las imagenes pusheadas a este repo es con: curl -X GET http://localhost:5000/v2/_catalog
    6.- Para establecer la conexión y poder hacer pull del código se necesita un token de acceso a github (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)
    7.- A continuación se crea el secreto en Kubernetes - (kubectl create secret generic github-secret --from-literal=token=YOUR_PERSONAL_ACCESS_TOKEN)
    8.- Se asocia el secreto a una cuenta de servicios y luego se referencia la cuenta de servicio en el pipeline (deploy del "kubectl apply -f serviceaccount.yaml")
    9.- Ahora debería ser posible asociar la cuenta de servicio al pipeline.yaml
    10.- Antes de correr el pipeline, para hacer el git-clone hay que instalarlo usando el tkn (tkn hub install task git-clone)
    11.-Ejecutar el pipeline (kubectl apply -f pipeline.yaml)
    12.-Ejecutar el pipeline run (tkn pipelinerun logs  clone-build-push-run-4kgjr -f) . El output es: pipelinerun.tekton.dev/clone-build-push-run-4kgjr created
    13.-Después se puede usar el comando tkn pipelinerun logs  clone-build-push-run-4kgjr -f para hacer el monitoreo
    14.-El seguimiento se hace a través del comando TKN.
    15.-IMPORTANTE!!: Para la ejecución del pipeline es necesario tener la tarea KANIKO instalada (kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/kaniko/0.4/kaniko.yaml)
    16.-
    17.-
    18.-
    19.-
    20.-
