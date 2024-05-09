import os
import subprocess
import requests
import tkinter as tk
from tkinter import messagebox, ttk

def check_rust_executable():
    return os.path.exists('C:\\rust_server\\RustDedicated.exe')

def install_steamcmd(progress):
    progress['value'] = 20
    root.update_idletasks()
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
        messagebox.showinfo("Installation", "SteamCMD has been installed.")
    else:
        messagebox.showinfo("Installation", "SteamCMD is already installed.")
    progress['value'] = 40

def install_rust_server(progress):
    progress['value'] = 60
    root.update_idletasks()
    print("Installing Rust Server...")
    subprocess.run(['C:\\steamcmd\\steamcmd.exe', '+login', 'anonymous', '+force_install_dir', 'C:\\rust_server', '+app_update', '258550', 'validate', '+quit'], check=True)
    messagebox.showinfo("Installation", "Rust Server has been installed.")
    progress['value'] = 80

def run_rust_server(progress):
    progress['value'] = 100
    root.update_idletasks()
    print("Running Rust Server...")
    subprocess.Popen(['C:\\rust_server\\RustDedicated.exe', '-batchmode', '+server.ip 0.0.0.0', '+server.port 28015', '+server.tickrate 30', '+server.hostname "Your Server Name"', '+server.identity "my_server"', '+server.maxplayers 50', '+server.worldsize 3000', '+server.saveinterval 300', '+rcon.ip 0.0.0.0', '+rcon.port 28016', '+rcon.password "YourRconPassword"', '-nographics'])
    messagebox.showinfo("Server Running", "Rust server is now running.")

def setup_server():
    progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
    progress.pack(pady=20)
    if not check_rust_executable():
        install_steamcmd(progress)
        install_rust_server(progress)
    run_rust_server(progress)

def main():
    global root
    root = tk.Tk()
    root.title("Rust Server Setup by @radiantcoder3")
    tk.Button(root, text="Setup and Run Rust Server", command=setup_server).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
