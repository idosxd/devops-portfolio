## Deploying Jenkins on Kubernetes with Helm

This tutorial will guide you through the process of deploying Jenkins on Kubernetes using Helm.

### Prerequisites

Before proceeding, make sure you have the following prerequisites in place:

- Helm installed on your system.
- Kubernetes cluster set up and configured.
- Download the [values.yaml](https://gitlab.com/sela-1090/students/ido_zarfati/infrastructures/jenkins/-/raw/feture_1_jenkins/values.yaml?inline=false) file.


### Step 1: Adding the Jenkins repository to Helm

First, add the Jenkins Helm repository and update the local repository cache by running the following commands:

```shell
helm repo add jenkins https://charts.jenkins.io
helm repo update
```

### Step 2: Creating a namespace

Before deploying Jenkins, let's create a namespace for Jenkins using `kubectl`:

```shell
kubectl create namespace jenkins
```

### Step 3: Installing additional Jenkins plugins (Optional)

If you want to install additional Jenkins plugins along with the default ones, you can do so by modifying the `values.yaml` file. Locate the `additionalPlugins` section in the file and add the names and versions of the plugins you want to install. The section will look something like this:

```yaml
additionalPlugins:
  - plugin-name:version
```

### Step 4: Deploying Jenkins using Helm

To deploy Jenkins, use the `helm install` command with the specified values and assign a release name. Run the following command:

```shell
helm install --namespace jenkins -f values.yaml myjenkins jenkins/jenkins
```

This command will install Jenkins in the `jenkins` namespace using the configuration from the `values.yaml` file.

### Step 5: Retrieving the Jenkins admin password

To retrieve the Jenkins admin password, execute the following command to access the `myjenkins` service using `kubectl`:

```shell
kubectl exec --namespace jenkins -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password
```

The output will display the Jenkins admin password, which you can use to log in to the Jenkins UI.

### Step 6: Verifying the deployment

Once the deployment is complete, you can verify that Jenkins has been successfully deployed. Here are a few steps you can follow:

1. Access the Jenkins UI using the service's external IP or domain.
2. Enter the admin username (default: `admin`) and the password obtained in the previous step.
3. Complete the initial Jenkins setup process.

## Step 7 Changing the Jenkins Logo (Optional)

If you'd like to customize the Jenkins logo displayed in the UI, you can follow these steps:

1. Go to **Manage Jenkins** > **System** > **Theme**.
2. Click on **Add** and then select **Extra CSS**.
3. Paste the following code in the provided text area:

```css
/* Custom style for Jenkins */
.logo img {
  content: url(https://gitlab.com/sela-1090/students/ido_zarfati/infrastructures/jenkins/-/raw/feture_1_jenkins/logo.jpg?ref_type=heads);
  /* Change the path to your logo's URL */
}

#jenkins-name-icon {
  display: none;
}

.logo:after {
  content: 'Production IT Automations';
  font-weight: bold;
  font-size: 40px;
  font-family: "Brush Script MT", cursive;
  margin-left: 200px;
  margin-right: 12px;
  color: Aqua;
  line-height: 40px;
}
```

Make sure to change the `content` URL to the path of your desired logo image.

### Conclusion

You have successfully deployed Jenkins on Kubernetes using Helm. You can now start utilizing Jenkins for your continuous integration and delivery workflows.

---

### Cleaning Up

To clean up and delete the Jenkins deployment, follow these steps:

### Step 1: Delete the Jenkins release

To delete the Jenkins release created with Helm, use the following command:

```shell
helm delete myjenkins --namespace jenkins
```

This command will remove the Jenkins deployment and all related resources from the `jenkins` namespace.

### Step 2: Delete the namespace

Next, delete the Jenkins namespace using the following command:

```shell
kubectl delete namespace jenkins
```

This command will delete the entire namespace along with all the resources associated with Jenkins.

### Step 3: Optional - Remove Jenkins Helm repository

If you no longer need the Jenkins Helm repository, you can remove it from Helm:

```shell
helm repo remove jenkins
```

This step is optional but can be performed if you want to clean up unused Helm repositories.

By following these steps, you have successfully cleaned up and removed Jenkins and its associated resources from the Kubernetes cluster.

Remember that cleaning up will permanently delete the Jenkins deployment and all its data, including jobs, configurations, and plugins. Make sure to back up any critical data before performing the cleanup if you intend to reinstall Jenkins later.

---

For more advanced configuration options or troubleshooting, refer to the official [Jenkins Helm chart documentation](https://github.com/jenkinsci/helm-charts/tree/main/charts/jenkins).
