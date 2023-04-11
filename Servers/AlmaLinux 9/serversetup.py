import os
import subprocess
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_word(words):
    return random.choice(words)

words = ["firestorm", "cyclone", "thunder", "avalanche", "blizzard", "tornado", "titan", "neptune", "mars", "astro", "crident"]
random_word = generate_random_word(words)
random_string = generate_random_string(6)

hostname = f"{random_word}-{random_string}"

commands = [
    "sudo dnf update -y",
    "sudo dnf upgrade -y",
    "sudo systemctl enable firewalld --now",
    "sudo firewall-cmd --add-service=ssh --permanent",
    "sudo firewall-cmd --zone=public --add-interface=tailscale0 --permanent",
    "sudo firewall-cmd --add-port=8443/tcp --permanent",
    "sudo firewall-cmd --add-port=2022/tcp --permanent",
    "sudo firewall-cmd --reload",
    "sudo dnf install fail2ban -y",
    "sudo systemctl start fail2ban",
    "sudo systemctl enable fail2ban",
    f"sudo hostnamectl set-hostname {hostname}",
    "sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo",
    "sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin",
    "sudo systemctl start docker",
    "sudo systemctl enable docker",
    "sudo usermod -aG docker $USER",
    "newgrp docker",
    "sudo dnf install epel-release -y",
    "sudo dnf install cmake gcc make curl -y",
    "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y",
    "source ~/.profile",
    "source ~/.cargo/env",
]

def run_command(command):
    try:
        subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(f"Completed: {command}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode('utf-8').strip()}")

if __name__ == "__main__":
    for command in commands:
        print(f"Executing: {command}")
        run_command(command)
