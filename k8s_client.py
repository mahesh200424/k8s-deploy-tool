from kubernetes import client, config

def initialize_k8s():
    try:
        config.load_kube_config()
        print("✅ Connected to Kubernetes cluster")
    except Exception as e:
        print(f"❌ Failed to connect to Kubernetes: {e}")


