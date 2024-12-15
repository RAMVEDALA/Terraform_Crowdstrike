terraform {
  required_providers {
    crowdstrike = {
      source = "registry.terraform.io/crowdstrike/crowdstrike"
    }
  }
}

provider "crowdstrike" {

  cloud         = "us-2"
  client_id     = var.client_id
  client_secret = var.client_secret

}
