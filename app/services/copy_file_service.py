from kubernetes import client
from .k8s_auth_service import run_kube_auth_service


def list_pod_all_namespace():
    run_kube_auth_service()
    v1 = client.CoreV1Api()
    print("Listing nodes with their IPs:")
    print(v1.list_node())
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    return "hello"
