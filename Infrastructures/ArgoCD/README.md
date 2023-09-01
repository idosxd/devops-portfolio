## Deploying Argo CD on Kubernetes

This tutorial will guide you through the process of deploying Argo CD on Kubernetes.

### Prerequisites

Before proceeding, make sure you have the following prerequisites in place:

- Kubernetes cluster set up and configured.
- Argo CD CLI installed. Refer to the [Argo CD documentation](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd-cli) for installation instructions.

### Step 1: Creating a Kubernetes namespace for Argo CD

Start by creating a Kubernetes namespace called `argocd` and deploying Argo CD within that namespace. Run the following commands:

```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Step 2: Configuring the Argo CD service

Next, update the `argocd-server` service in the `argocd` namespace to change its type to `LoadBalancer` using JSON patching. Run the following command:

```shell
kubectl patch svc argocd-server -n argocd --type='json' -p='[{"op": "replace", "path": "/spec/type", "value": "LoadBalancer"}]'
```

### Step 3: Retrieving the initial admin password

To access the Argo CD UI, you need the initial admin password. Retrieve it by running the following command:

```shell
argocd admin initial-password -n argocd
```

### Step 4: Verifying the deployment

Once the deployment is complete, you can verify that Argo CD has been successfully deployed. Here are a few steps you can follow:

1. Access the Argo CD UI using the service's external IP or domain.
2. Enter the admin username and the password obtained in the previous step.
3. Explore the Argo CD UI and confirm that it is functioning correctly.

### Conclusion
Congratulations! You have successfully deployed Argo CD on Kubernetes. Argo CD provides a powerful continuous delivery and GitOps solution for managing your Kubernetes deployments.

---

### Cleaning Up

To clean up and delete the Argo CD deployment, follow these steps:

### Step 1: Delete the Argo CD installation

To delete the Argo CD installation and all related resources from the `argocd` namespace, use the following command:

```shell
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

This command will remove all the Argo CD resources from the `argocd` namespace.

### Step 2: Delete the Argo CD namespace

Next, delete the dedicated Argo CD namespace using the following command:

```shell
kubectl delete namespace argocd
```

This command will delete the entire namespace along with all the resources associated with Argo CD.

### Step 3: Optional - Remove Argo CD CLI

If you no longer need the Argo CD CLI, you can remove it from your system.

By following these steps, you have successfully cleaned up and removed Argo CD and its associated resources from the Kubernetes cluster.

Remember that cleaning up will permanently delete the Argo CD deployment and all its data. Make sure to back up any critical data before performing the cleanup if you intend to reinstall Argo CD later.

---

For more information and advanced configuration options, refer to the official [Argo CD documentation](https://argoproj.github.io/argo-cd/).
