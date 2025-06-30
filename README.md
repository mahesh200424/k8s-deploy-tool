# 🚀 k8s-deploy-tool

A modular CLI tool to automate Kubernetes deployments, health checks, and KEDA-based autoscaling. Designed for DevOps workflows and infrastructure automation tasks.

## 🔧 Features

- ✅ Connects to a local or remote Kubernetes cluster
- 📦 Installs [KEDA](https://keda.sh) via Helm for event-driven autoscaling
- 🚀 Deploys containerized apps from a YAML config
- 📊 Checks deployment health (pods, replicas, resource usage)
- 📁 Easy to extend with modular Python components

---

## 📂 Project Structure

k8s-deploy-tool/
├── cli.py # Main CLI handler
├── k8s_client.py # K8s cluster connection logic
├── keda_installer.py # Installs KEDA using Helm
├── deployment_manager.py # Handles Kubernetes Deployment creation
├── health_checker.py # Fetches pod and deployment status
├── config/
│ └── deployment_config.yaml
├── requirements.txt # Python dependencies
└── README.md 

---

## ⚙️ Requirements

- Python 3.8+
- Kubernetes Cluster (e.g., Rancher Desktop, Minikube, EKS, GKE)
- `kubectl` configured
- `helm` installed

Install Python dependencies:

```bash
pip install -r requirements.txt

#Install KEDA
python cli.py --action install-keda

#Deploy an APP
python cli.py --action deploy --config config/deployment_config.yaml

#CHECK HEALTH
python cli.py --action health --deployment my-app

