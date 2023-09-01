## Deploying Prometheus and Grafana on Kubernetes with Helm

This guide will walk you through the process of deploying Prometheus and Grafana on Kubernetes using Helm. Prometheus is a monitoring and alerting toolkit, while Grafana is a visualization and analytics platform. Together, they form a powerful monitoring and observability solution for your Kubernetes cluster.

### Prerequisites

Before proceeding, ensure you have the following prerequisites in place:

- Helm installed on your system.
- Kubernetes cluster set up and configured.

### Step 1: Adding the Helm repositories

First, add the Helm repositories for Prometheus and Grafana and update the local repository cache by running the following commands:

```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

### Step 2: Creating a Kubernetes Namespace

To keep all the resources organized, create a Kubernetes namespace for the Prometheus and Grafana deployment. Run the following command:

```shell
kubectl create namespace observation
```

### Step 3: Deploying Prometheus using Helm

Next, deploy Prometheus to the Kubernetes cluster in the `observation` namespace using Helm:

```shell
helm install prometheus prometheus-community/prometheus --namespace observation
```

### Step 4: Deploying Grafana using Helm

Now, deploy Grafana to the Kubernetes cluster in the `observation` namespace using Helm:

```shell
helm install grafana grafana/grafana --namespace observation
```

### Step 5: Exposing Prometheus and Grafana Services

To access Prometheus and Grafana externally, we need to expose them using Kubernetes Services of type `LoadBalancer`. Run the following commands:

```shell
kubectl expose service prometheus-server -n observation --type=LoadBalancer --name=prometheus-loadbalancer --port=9090 --target-port=9090
kubectl expose service grafana -n observation --type=LoadBalancer --name=grafana-loadbalancer --port=3000 --target-port=3000
```

### Step 6: Retrieving Grafana Admin Password

To access Grafana's web interface, you need the admin password. Run the following command to retrieve it:

```shell
kubectl get secret --namespace observation grafana -o jsonpath="{.data.admin-password}" | base64 --decode
```

The output will display the Grafana admin password.

### Step 7: Configuring Prometheus Data Source in Grafana

Now that Prometheus and Grafana are deployed, let's configure Prometheus as a data source in Grafana:

1. Open your web browser and navigate to the Grafana UI using the external IP or domain provided by the LoadBalancer service (e.g., http://<grafana-external-ip>:3000).
2. Log in to Grafana using the admin username (default: `admin`) and the password obtained in the previous step.
3. Once logged in, click on the gear icon (Configuration) in the left sidebar and select "Data Sources."
4. Click on "Add data source" and select "Prometheus."
5. In the "HTTP" section, set the URL to `http://prometheus-loadbalancer:9090`.
6. Click "Save & Test" to verify the connection to Prometheus.

### Step 8: Creating Dashboards and Alerts

With Prometheus as the data source, you can now create Grafana dashboards and set up alerting rules based on the metrics collected by Prometheus. This step is highly customizable and depends on your specific monitoring needs.

### Conclusion

You have successfully deployed Prometheus and Grafana on Kubernetes using Helm. You can now start monitoring and visualizing your Kubernetes cluster's metrics using Grafana dashboards and utilize Prometheus for alerting and monitoring purposes.

---

### Cleaning Up

To clean up and delete the Prometheus and Grafana deployment, follow these steps:

### Step 1: Delete the Helm releases

To delete the Prometheus and Grafana releases created with Helm, use the following commands:

```shell
helm delete prometheus --namespace observation
helm delete grafana --namespace observation
```

These commands will remove the Prometheus and Grafana deployments along with all related resources from the `observation` namespace.

### Step 2: Delete the observation namespace

Next, delete the dedicated `observation` namespace using the following command:

```shell
kubectl delete namespace observation
```

This command will delete the entire namespace along with all the resources associated with Prometheus and Grafana.

### Step 3: Optional - Remove Helm repositories

If you no longer need the Prometheus and Grafana Helm repositories, you can remove them from Helm:

```shell
helm repo remove prometheus-community
helm repo remove grafana
```

This step is optional but can be performed if you want to clean up unused Helm repositories.

Remember that cleaning will permanently delete the Prometheus and Grafana deployment and all their data. Be sure to back up critical data before performing the cleanup if you intend to reinstall Prometheus and Grafana later.

---

For more advanced configuration options or troubleshooting, refer to the official Helm chart documentation for [Prometheus](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus) and [Grafana](https://github.com/grafana/helm-charts/tree/main/charts/grafana).
