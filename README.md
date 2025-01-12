Here with this Terraform Configuration we are using Crowdstrike provider to create host_groups and policies

A)First provide your client_id and client_secret details in terraform.tfvars file

B)Give the appropriate READ and WRITE permissions for the API Requests

C)Make sure python, pip, falconpy are installed in the system

d)here our code only creates host_groups (static and dynamic). for defining prevention_policies, we need to hardcode the host_groups values, we can implement the logic later if the rules for creating host_groups based on our requirement

e)run below command to see the host group names 
terraform output -json static_host_groups > static_host_groups.json
terraform output -json dynamic_host_groups > dynamic_host_groups.json



# Terraform Configuration for CrowdStrike Policies and Host Groups

## Overview
This Terraform module automates the creation of CrowdStrike resources, including host groups, prevention policies, sensor update policies, and FileVantage rule groups. The configuration dynamically adapts based on the platform and provided variables.

## Prerequisites
1. **Terraform Installed:** Ensure Terraform is installed on your system.
2. **CrowdStrike API Access:** Obtain CrowdStrike API credentials with appropriate permissions.
3. **Python Environment:** The `fetch_hostnames.py` script requires Python 3.
4. **Platform-Specific Details:** Define platform host maps and host tags as required.

## Features
- Fetches and processes hostnames dynamically.
- Creates static and dynamic host groups.
- Configures prevention policies for Linux, macOS, and Windows.
- Sets up sensor update policies with scheduling.
- Defines FileVantage rule groups and policies.

## File Structure
```
.
├── fetch_hostnames.py           # Python script to generate platform_host_map.json
├── platform_host_map.json      # JSON file generated by fetch_hostnames.py
├── main.tf                     # Core Terraform configuration
├── variables.tf                # Variable definitions
├── outputs.tf                  # Output definitions
├── README.md                   # Documentation (this file)
```

## Usage

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Configure Variables
Define the necessary variables in `variables.tf` or via `terraform.tfvars`.
Example:
```hcl
variable "host_tags" {
  type = list(string)
  default = ["tag1", "tag2"]
}
```

### 3. Fetch Hostnames
Run the Python script to generate the `platform_host_map.json` file:
```bash
python3 fetch_hostnames.py
```

### 4. Initialize Terraform
Initialize the Terraform environment:
```bash
terraform init
```

### 5. Plan and Apply Changes
Review and apply the Terraform configuration:
```bash
terraform plan
terraform apply
```

## Configuration Details

### Host Groups
- **Static Host Groups:** Automatically created based on `platform_host_map`.
- **Dynamic Host Groups:** Created based on tags defined in `var.host_tags`.

### Prevention Policies
- Policies are defined for Linux, macOS, and Windows platforms.
- Specify host groups for each platform within the `host_groups` field.

### Sensor Update Policies
- Policies include scheduling options and platform-specific build numbers.
- Modify build numbers and host group IDs as required.

### FileVantage Rule Groups and Policies
- Define file integrity rules for Windows and macOS platforms.
- Specify schedules for FileVantage rule execution.

## Customization

### Variables
Adjust the following variables as required:
- `host_tags`: List of host tags for dynamic groups.
- `platform_host_map`: Map of platforms and corresponding host IDs.

### Files to Modify
- `fetch_hostnames.py`: Update the script logic to fetch platform-specific hostnames.
- `main.tf`: Add or modify resource definitions as needed.
- `variables.tf`: Update default values or add new variables.

## Example Outputs
The module will generate outputs such as:
- Host group names
- Policies created for each platform
- FileVantage rule group IDs

## Troubleshooting
- **Error in `fetch_hostnames.py`:** Ensure Python dependencies are installed and script permissions are set.
- **Terraform errors:** Validate the `platform_host_map.json` and ensure all required variables are defined.

## References
- [Terraform Documentation](https://www.terraform.io/docs)
- [CrowdStrike API Documentation](https://developer.crowdstrike.com)

## License
This module is licensed under the MIT License. See the LICENSE file for details.
