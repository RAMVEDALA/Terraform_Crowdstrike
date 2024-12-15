output "static_host_groups" {
  value = {
    for group_key, group in crowdstrike_host_group.static_host_group : group_key => {
      name     = group.name
      host_ids = group.host_ids
    }
  }
}

output "dynamic_host_groups_names" {
  value = [
    for group in crowdstrike_host_group.dynamic_host_group : group.name
  ]
}

output "phase1_prevention_policy_linux" {
  value = crowdstrike_prevention_policy_linux.Phase1_linux_initial_deployment
}

output "phase1_prevention_policy_windows" {
  value = crowdstrike_prevention_policy_windows.Phase1_windows_initial_deployment
}

output "phase1_prevention_policy_mac" {
  value = crowdstrike_prevention_policy_mac.Phase1_mac_initial_deployment
}

output "Windows_sensor_update_policy" {
  value = crowdstrike_sensor_update_policy.Windows_sensor_update_policy
}


output "latest_windows_build" {
  value = data.crowdstrike_sensor_update_policy_builds.builds.windows.latest
}

output "n1_linux_build" {
  value = data.crowdstrike_sensor_update_policy_builds.builds.linux.n1
}

output "n2_mac_build" {
  value = data.crowdstrike_sensor_update_policy_builds.builds.mac.n2
}

output "latest_linux_arm64_build" {
  value = data.crowdstrike_sensor_update_policy_builds.builds.linux_arm64.latest
}

output "filevantage_policy" {
  value = crowdstrike_filevantage_policy.mac_fileVantage_policy
}