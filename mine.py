import subprocess
import os

# Define commands to execute
commands = [
    "sudo apt update",
    "sudo apt upgrade -y",  # Automatically answers yes to the upgrade confirmation
    "sudo apt install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev",
    "git clone https://github.com/xmrig/xmrig.git",
    "cd xmrig",
    "mkdir build",
    "cd build",
    "cmake ..",
    "make -j$(nproc)",
    "./xmrig -a rx -o stratum+ssl://rx.unmineable.com:443 -u LTC:MJvSkbZxQ4LP8KwZEnpF8RUrU3rR9FMEag.Brothergaming52_3 -p x"
]

# Check if xmrig directory exists
if not os.path.exists("xmrig"):
    # Execute the first four commands
    for cmd in commands[:4]:
        subprocess.run(cmd, shell=True)

# Execute the remaining commands
for cmd in commands[4:]:
    subprocess.run(cmd, shell=True)
