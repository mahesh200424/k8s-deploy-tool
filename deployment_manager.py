import yaml
from kubernetes import client

def create_deployment(config_path):
    with open(config_path, 'r') as f:
        config_data = yaml.safe_load(f)

    name = config_data['name']
    namespace = config_data.get('namespace', 'default')
    image = config_data['image']
    ports = config_data.get('ports', [80])

    container = client.V1Container(
        name=name,
        image=image,
        ports=[client.V1ContainerPort(container_port=p) for p in ports]
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": name}),
        spec=client.V1PodSpec(containers=[container])
    )

    spec = client.V1DeploymentSpec(
        replicas=1,
        template=template,
        selector={'matchLabels': {'app': name}}
    )

    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=name),
        spec=spec
    )

    api = client.AppsV1Api()
    api.create_namespaced_deployment(namespace=namespace, body=deployment)
    print(f"✅ Deployment '{name}' created in namespace '{namespace}'")


