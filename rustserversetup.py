import os
import subprocess
import requests

def install_steamcmd():
    print("Checking for SteamCMD installation...")
    if not os.path.exists('C:\\steamcmd\\steamcmd.exe'):
        print("SteamCMD not found, installing...")
        steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
        os.makedirs('C:\\steamcmd', exist_ok=True)
        os.chdir('C:\\steamcmd')
        response = requests.get(steamcmd_url)
        with open('steamcmd.zip', 'wb') as f:
            f.write(response.content)
        subprocess.run(['powershell', '-command', "Expand-Archive", '-Path', 'steamcmd.zip', '-DestinationPath', '.'], check=True)
        os.chdir('..')
    else:
        print("SteamCMD is already installed.")

def install_rust_server():
    print("Installing Rust Server...")
    subprocess.run(['C:\\steamcmd\\steamcmd.exe', '+login', 'anonymous', '+force_install_dir', 'C:\\rust_server', '+app_update', '258550', 'validate', '+quit'], check=True)

def create_start_script():
    print("Creating server start script...")
    with open('start_rust_server.bat', 'w') as f:
        f.write('''@echo off
cd C:\\rust_server
RustDedicated -batchmode +server.ip 0.0.0.0 +server.port 28015 +server.tickrate 30 +server.hostname "Your Server Name" +server.identity "my_server" +server.maxplayers 50 +server.worldsize 3000 +server.saveinterval 300 +rcon.ip 0.0.0.0 +rcon.port 28016 +rcon.password "YourRconPassword" -nographics''')

def main():
    install_steamcmd()
    install_rust_server()
    create_start_script()
    print("Rust server setup is complete. Start your server by running 'start_rust_server.bat'.")

if __name__ == "__main__":
    main()
