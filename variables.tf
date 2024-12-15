variable "client_id" {
  description = "CrowdStrike API Client ID"
  type        = string
}

variable "client_secret" {
  description = "CrowdStrike API Client Secret"
  type        = string
}

variable "host_tags" {
  description = "List of tags for the dynamic host groups"
  type        = list(string)
  default     = ["aws-instances", "windows", "production-servers"] # Add your tag values as per your configuration

}

