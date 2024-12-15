import json
from falconpy import Discover

falcon = Discover(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# List of OS platforms available
platforms = ["Windows", "Mac", "Linux"]

# A dictionary to store host IDs based on platform_name
platform_host_map = {platform: [] for platform in platforms}

# Fetch and categorizing hosts for each platform
for platform_name in platforms:
    print(f"Fetching hosts for platform: {platform_name}")
    
    try:
        response = falcon.combined_hosts(
            limit=1000,
            sort="platform_name|asc",
            filter=f"host.platform_name:'{platform_name}'"
        )
        
        # Check if the response contains valid data
        if response.get("status_code") == 200 and response.get("body", {}).get("resources"):
            # Extract host IDs for the given platform
            host_ids = [host.get("id") for host in response["body"]["resources"] if host.get("id")]
            
            # Print for verification
            print(f"Found {len(host_ids)} hosts for platform {platform_name}: {host_ids}")
            
            # Store the host IDs in the map
            platform_host_map[platform_name] = host_ids
        else:
            print(f"Warning: No valid hosts found for platform '{platform_name}' or API returned an error.")
    
    except Exception as e:
        print(f"Error while fetching hosts for platform '{platform_name}': {e}")

# Validate the final result
try:
    if not any(platform_host_map.values()):
        raise ValueError("Error: No hosts were fetched. The platform_host_map is empty.")
    
    # Print the map of platform to host IDs for verification
    print("Platform Host Map:", json.dumps(platform_host_map, indent=4))
    
    # Save the result to a file
    with open("platform_host_map.json", "w") as file:
        json.dump(platform_host_map, file, indent=4)
    print("platform_host_map.json file generated successfully.")
    
except ValueError as ve:
    print(ve)
    with open("platform_host_map.json", "w") as file:
        json.dump({}, file, indent=4)
    print("An empty platform_host_map.json file was created due to errors.")

except Exception as e:
    print(f"Unexpected error: {e}")
    with open("platform_host_map.json", "w") as file:
        json.dump({}, file, indent=4)
    print("An empty platform_host_map.json file was created due to unexpected errors.")
