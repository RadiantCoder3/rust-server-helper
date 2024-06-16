import os
import subprocess
import requests

def install_steamcmd(username):
    print("Checking for SteamCMD installation...")
    steamcmd_path = f'/home/{username}/steamcmd/steamcmd.sh'
    if not os.path.exists(steamcmd_path):
        print("SteamCMD not found, installing...")
        steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz'
        os.makedirs(f'/home/{username}/steamcmd', exist_ok=True)
        os.chdir(f'/home/{username}/steamcmd')
        response = requests.get(steamcmd_url)
        with open('steamcmd_linux.tar.gz', 'wb') as f:
            f.write(response.content)
        subprocess.run(['tar', '-xvzf', 'steamcmd_linux.tar.gz'], check=True)
    else:
        print("SteamCMD is already installed.")

def install_rust_server(username):
    print("Installing Rust Server...")
    subprocess.run([f'/home/{username}/steamcmd/steamcmd.sh', '+login', 'anonymous', '+force_install_dir', f'/home/{username}/rust_server', '+app_update', '258550', 'validate', '+quit'], check=True)

def main():
    username = input("Enter your Linux username: ")
    install_steamcmd(username)
    install_rust_server(username)
    print(f"Rust server setup is complete! Runing command './RustDedicated' in the '/home/{username}/rust_server' folder to start the server.")

if __name__ == "__main__":
    main()
