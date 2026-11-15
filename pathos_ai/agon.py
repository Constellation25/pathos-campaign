import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from .oracle import Oracle

console = Console()

def play_astragaloi():
    console.print(Panel.fit("[bold cyan]🎲 ASTRAGALOI: Knucklebones of Fate[/bold cyan]", style="cyan"))
    console.print("\n[bold]Rolling the bones...[/bold]")
    time.sleep(1)
    
    sides = [1, 3, 4, 6]
    roll = [random.choice(sides) for _ in range(4)]
    total = sum(roll)
    is_aphrodite = len(set(roll)) == 4
    
    table = Table(title="🦴 The Roll")
    table.add_column("Bone 1", style="yellow")
    table.add_column("Bone 2", style="yellow")
    table.add_column("Bone 3", style="yellow")
    table.add_column("Bone 4", style="yellow")
    table.add_column("Total", style="bold green")
    table.add_row(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(total))
    
    console.print(table)
    
    if is_aphrodite:
        console.print("\n[bold magenta]✨ APHRODITE THROW ACHIEVED! ✨[/bold magenta]")
    else:
        console.print(f"\n[dim]Standard roll. Odds of Aphrodite Throw: 1 in 8.[/dim]")
    
    console.print(f"\n[dim italic]🎛️ Cygnus Note: {Oracle.speak('warmth')}[/dim italic]")

def play_morra():
    console.print(Panel.fit("[bold cyan]✋ MORRA: Test of Reflexes[/bold cyan]", style="cyan"))
    
    try:
        user_fingers = int(Prompt.ask("\n[bold green]Flash fingers (0-5)[/bold green]"))
        if not (0 <= user_fingers <= 5):
            console.print("[bold red]⚡ Invalid number.[/bold red]")
            return
            
        ai_fingers = random.randint(0, 5)
        ai_guess = random.randint(0, 10)
        
        console.print(f"\n[dim]AI flashes [bold]{ai_fingers}[/bold], guesses total: [bold]{ai_guess}[/bold][/dim]")
        time.sleep(1)
        
        actual_total = user_fingers + ai_fingers
        console.print(f"\n[bold]Actual total: {actual_total}[/bold]")
        
        if ai_guess == actual_total:
            console.print("\n[bold red]🏛️ ORACLE WINS.[/bold red]")
        else:
            console.print("\n[bold green]🎉 VICTORY![/bold green]")
            
    except ValueError:
        console.print("[bold red]⚡ Enter a valid number.[/bold red]")

def agon_menu():
    console.print(Panel.fit("[bold cyan]🏛️ THE PAHTOS AGON[/bold cyan]", style="cyan"))
    console.print("1. 🎲 Astragaloi (Probability)")
    console.print("2. ✋ Morra (Reflexes)")
    console.print("3. 🏛️ Petteia (Coming soon)")
    console.print("4. 🏁 Pente Grammai (Coming soon)")
    
    choice = Prompt.ask("\n[bold green]Choose (1-4)[/bold green]", default="1")
    
    if choice == "1":
        play_astragaloi()
    elif choice == "2":
        play_morra()
    else:
        console.print("[bold yellow]⚠️ Coming soon![/bold yellow]")
