# AquaTrack Namespaces Chart Installation Guide

The AquaTrack Namespaces Chart provides an easy way to set up namespaces for the AquaTrack app, allowing you to manage and isolate different environments for your AquaTrack deployments. This guide will walk you through the steps required to install the `aquatrack-namespaces-chart` on your Kubernetes cluster.

## Prerequisites

Before you begin, ensure that you have the following prerequisites in place:

1. **Kubernetes Cluster**: You should have a Kubernetes cluster up and running, and you should have `kubectl` configured to interact with it.

2. **Helm**: Helm is a package manager for Kubernetes that makes it easy to deploy applications and services. Make sure you have Helm installed. If not, you can follow the installation guide [here](https://helm.sh/docs/intro/install/).

## Installation

Follow these steps to install the `aquatrack-namespaces-chart`:

1. **Install Chart**: Use Helm to install the chart. Provide a release name (e.g., `aquatrack-namespaces`) and specify the path to the chart directory:

    ```bash
    helm install aquatrack-namespaces ./
    ```
2. **Verify Installation**: After the installation is complete, you can use `kubectl` to verify that the namespaces have been created:

    ```bash
    kubectl get namespaces
    ```

## Uninstallation

If you want to remove the AquaTrack Namespaces Chart and delete the namespaces, you can use the following steps:

1. **Uninstall Chart**: Run the following command to uninstall the chart:

    ```bash
    helm uninstall aquatrack-namespaces
    ```
    
## Conclusion

Congratulations! You've successfully installed the AquaTrack Namespaces Chart, which creates namespaces for the AquaTrack app on your Kubernetes cluster. This setup allows you to manage your AquaTrack deployments in isolated environments.
