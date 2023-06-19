# This code uses the rpc.py module obtained from the Discord RPC repository
# Original rpc.py code by Nivesh Birangal: https://github.com/niveshbirangal/discord-rpc

import rpc
import time

client_id = '0000000000000000000'  # Your application's client ID
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC connection successful.")

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    elapsed_minutes = elapsed_time // 60
    elapsed_hours = elapsed_minutes // 60
    elapsed_days = elapsed_hours // 24

    if elapsed_days > 0:
        elapsed_days = int(elapsed_days)
        state = f"for {elapsed_days} day{'s' if elapsed_days != 1 else ''}"
    elif elapsed_hours > 0:
        elapsed_hours = int(elapsed_hours)
        state = f"for {elapsed_hours} hour{'s' if elapsed_hours != 1 else ''}"
    elif elapsed_minutes > 0:
        elapsed_minutes = int(elapsed_minutes)
        state = f"for {elapsed_minutes} minute{'s' if elapsed_minutes != 1 else ''}"
    else:
        state = "Just started playing"

    # Visual details of the Rich Presence

    activity = {
        "state": state,
        "details": "(Finding Majima in the karaoke bar.)",  # Custom detail, comment if you don't want it to be included
        "assets": {
            "large_image": "imagename"  # Name of the image used for the icon
        }
    }
    rpc_obj.set_activity(activity)
    time.sleep(15)
