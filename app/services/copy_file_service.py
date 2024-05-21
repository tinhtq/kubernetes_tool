from kubernetes import client, config
from .k8s_auth_service import run_kube_auth_service

run_kube_auth_service()


def list_pod_all_namespace():
    v1 = client.CoreV1Api()
    return v1.list_pod_for_all_namespaces(watch=False)
