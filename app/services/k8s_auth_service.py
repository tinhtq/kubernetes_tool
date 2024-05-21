from kubernetes import client, config
from app.core.config import configs


def run_kube_auth_service():
    environment = configs.ENV
    if environment == "local":
        config.load_kube_config(config_file="kubeconfig")
    else:
        config.load_incluster_config()
