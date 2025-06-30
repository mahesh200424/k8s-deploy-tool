from kubernetes import client

def check_health(deployment_name, namespace='default'):
    v1 = client.CoreV1Api()
    apps_v1 = client.AppsV1Api()

    try:
        deployment = apps_v1.read_namespaced_deployment(deployment_name, namespace)
        pods = v1.list_namespaced_pod(namespace, label_selector=f"app={deployment_name}")

        print(f"Deployment '{deployment_name}': {deployment.status.replicas} replicas")
        for pod in pods.items:
            print(f"Pod {pod.metadata.name} - Status: {pod.status.phase}")
    except Exception as e:
        print(f"❌ Error retrieving health status: {e}")
