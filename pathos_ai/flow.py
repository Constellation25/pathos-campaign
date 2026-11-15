import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .oracle import Oracle

console = Console()

FREQUENCIES = {
    "deep": {"hz": 432, "name": "432 Hz (Natural Harmonic)", "god": "Pythagoras", "effect": "Clears mental fog"},
    "focus": {"hz": 40, "name": "40 Hz (Gamma Waves)", "god": "Athena", "effect": "Neural synchrony"},
    "renewal": {"hz": 528, "name": "528 Hz (Love Frequency)", "god": "Apollo", "effect": "Gentle warmth"}
}

PID_FILE = "/data/data/com.termux/files/usr/tmp/pathos_flow.pid"

def is_playing():
    if os.path.exists(PID_FILE):
        with open(PID_FILE, 'r') as f:
            pid = f.read().strip()
        try:
            os.kill(int(pid), 0)
            return True, pid
        except OSError:
            os.remove(PID_FILE)
    return False, None

def start_flow(mode):
    if mode not in FREQUENCIES:
        console.print(f"[bold red]⚡ Unknown mode '{mode}'. Choose: deep, focus, renewal.[/bold red]")
        return

    is_active, pid = is_playing()
    if is_active:
        console.print("[bold yellow]⚠️ Flow State already active. Stop it first.[/bold yellow]")
        return

    freq_data = FREQUENCIES[mode]
    hz = freq_data["hz"]
    
    console.print(Panel.fit(f"[bold cyan]🦢 INITIATING FLOW STATE: {freq_data['name']}[/bold cyan]", style="cyan"))
    
    cmd = f"play -n synth sine {hz} vol 0.15 > /dev/null 2>&1 & echo $! > {PID_FILE}"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        time.sleep(1)
        is_active, new_pid = is_playing()
        if is_active:
            console.print(f"\n[bold green]✅ Flow State Active (PID: {new_pid})[/bold green]")
        else:
            console.print("[bold red]⚡ Failed to start audio. Ensure 'sox' is installed.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]⚡ SYSTEM ERROR: {str(e)}[/bold red]")

def stop_flow():
    is_active, pid = is_playing()
    if is_active:
        try:
            os.kill(int(pid), 9)
            os.remove(PID_FILE)
            console.print(Panel.fit("[bold green]✅ Flow State Terminated.[/bold green]", style="green"))
        except Exception as e:
            console.print(f"[bold red]⚡ Error: {str(e)}[/bold red]")
    else:
        console.print("[bold yellow]⚠️ No Flow State active.[/bold yellow]")

def flow_status():
    is_active, pid = is_playing()
    table = Table(title="🎛️ PaTHos Flow State Status")
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")
    
    if is_active:
        table.add_row("Status", "✅ ACTIVE")
        table.add_row("Process ID", pid)
    else:
        table.add_row("Status", "⭕ INACTIVE")
        table.add_row("Available Modes", "deep, focus, renewal")
        
    console.print(table)
