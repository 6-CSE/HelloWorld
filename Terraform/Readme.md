# Terraform - Infrastructure as Code

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

## Installation

[Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)


## How to run 

1. Create a Terraform configuration file

    ```bash
    $ touch main.tf
    ```

2. Initialize a working directory containing Terraform configuration files

    ```bash
    $ terraform init
    ```

3. Validate the configuration files in a directory, referring only to the configuration and not accessing any remote services such as remote state, provider APIs, etc.

    ```bash
    $ terraform validate
    ```

4. Generate and show an execution plan

    ```bash
    $ terraform plan
    ```

5. Builds or changes infrastructure

    ```bash
    $ terraform apply
    ```

6. Destroy Terraform-managed infrastructure

    ```bash
    $ terraform destroy
    ```
