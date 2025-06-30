import argparse
from deployment_manager import create_deployment
from health_checker import check_health
from keda_installer import install_keda
from k8s_client import initialize_k8s


def main():
    parser = argparse.ArgumentParser(description="K8s Deployment Automation CLI")
    parser.add_argument('--action', choices=['deploy', 'health', 'install-keda'], required=True)
    parser.add_argument('--config', help='Path to deployment config file')
    parser.add_argument('--deployment', help='Deployment name to check health')

    args = parser.parse_args()

    initialize_k8s()

    if args.action == 'install-keda':
        install_keda()
    elif args.action == 'deploy':
        if not args.config:
            print("--config is required for deploy")
            return
        create_deployment(args.config)
    elif args.action == 'health':
        if not args.deployment:
            print("--deployment is required for health check")
            return
        check_health(args.deployment)


if __name__ == '__main__':
    main()
