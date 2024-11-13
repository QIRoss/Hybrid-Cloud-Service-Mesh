# Service Mesh across Hybrid Cloud

Studies based in day 87-88 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 81–90: Advanced Networking and Content Delivery

Day 87–88: Implement a service mesh across a hybrid cloud environment.

## Project Overview

This project aims to explore the implementation of a service mesh in a hybrid cloud architecture, using Consul as a service discovery tool and FastAPI services for API communication. The setup involves:

* An on-premises environment with multiple FastAPI services and a Consul agent for service registration and discovery.

* A cloud environment hosted on AWS with multiple FastAPI services and a Consul agent.

* Aiming to enable service-to-service communication across environments.

### Components

1. Consul:

* Used for service discovery, running as agents in both the cloud and on-premises environments.

2. FastAPI Services:

* Services A, B, F in the on-premises environment.

* Services C, D, E in the cloud environment.

### Current Status

1. Individual Setup:

* On-premises FastAPI services are correctly registering with the on-premises Consul agent and functioning as expected.

* Cloud-based FastAPI services are correctly registering with the cloud Consul agent and functioning as expected.

2. Cross-Environment Connectivity:

* Cross-environment communication between on-premises and cloud services is currently not established due to network connectivity issues.

* Consul agents can successfully form LAN clusters within their own environments but fail to connect via WAN federation.

## How to Use

### Prerequisites

* Docker and Docker Compose installed on the on-premises environment.

* Terraform installed for provisioning cloud resources.

* SSH access to the cloud environment if using reverse SSH tunnels.

* Consul configuration files (consul-config.hcl) for both environments with appropriate datacenter and retry_join settings.

### Setup Steps

1. On-Premises Setup:

* Navigate to the on-premises project folder.

* Use Docker Compose to bring up the services:

```
docker-compose up --build
```

* Ensure that the on-premises Consul agent is running and the services register correctly.

2. Cloud Setup:

* Navigate to the Terraform directory for your cloud resources.

* Initialize Terraform:

```
terraform init
```

* Generate and review the execution plan:

```
terraform plan -out=tfplan
```

* Apply the Terraform plan:

```
terraform apply tfplan
```

* This will provision the necessary AWS resources and deploy the Docker containers for the cloud services.

3. Testing:

* Verify individual service registration and connectivity through the Consul UI on port 8500.

* Test communication between FastAPI services in the same environment.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"