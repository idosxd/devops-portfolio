Sure, here's the updated guide with the additional step to create the namespace:

# Installing PostgreSQL with Helm

This guide will walk you through the process of installing PostgreSQL using Helm, a package manager for Kubernetes applications.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- [Helm](https://helm.sh/docs/intro/install/) - The Helm CLI tool.
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) - The Kubernetes command-line tool.
- Access to a Kubernetes cluster.

## Installation Steps

Follow these steps to install PostgreSQL using Helm:

### 1. Create a Namespace

If the desired namespace doesn't exist, create it using the following command:

```bash
kubectl create namespace database
```

### 2. Add Bitnami Helm Repository

If you haven't added the Bitnami Helm repository before, you need to do it once:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### 3. Install PostgreSQL

Run the following Helm command to install PostgreSQL using the Bitnami Helm chart:

```bash
helm install my-release -n database oci://registry-1.docker.io/bitnamicharts/postgresql
```

### 4. Retrieve PostgreSQL Password

After the installation is complete, you can retrieve the PostgreSQL password using the following command:

```bash
export POSTGRES_PASSWORD=$(kubectl get secret --namespace database my-release-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)
echo $POSTGRES_PASSWORD
```

### 5. Connect to PostgreSQL

Use the following commands to connect to the PostgreSQL instance using the PostgreSQL client:

```bash
kubectl run my-release-postgresql-client --rm --tty -i --restart='Never' --namespace database --image docker.io/bitnami/postgresql:15.3.0-debian-11-r77 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
  --command -- psql --host my-release-postgresql -U postgres -d postgres -p 5432
```

This will open an interactive PostgreSQL session.

## Cleanup

If you want to uninstall the PostgreSQL instance, you can use the following Helm command:

```bash
helm uninstall my-release -n database
```

## Conclusion

You've successfully installed PostgreSQL using Helm and connected to it using the PostgreSQL client. Helm makes it easier to manage and deploy complex applications like databases on Kubernetes clusters.

For more information and customization options, you can refer to the [Bitnami PostgreSQL Helm Chart documentation](https://bitnami.com/stack/postgresql/helm).
