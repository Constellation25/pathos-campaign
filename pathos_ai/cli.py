import click
import json
import random
from rich.console import Console
from rich.panel import Panel
from rich.json import JSON
from rich.prompt import Prompt
from .cygnus import cygnus, LicenseError
from .oracle import Oracle
from .sync import run_sync_status
from .flow import start_flow, stop_flow, flow_status
from .vault import vault
from .llm_router import llm_router
from .agon import agon_menu

console = Console()

@click.group(invoke_without_command=True)
@click.pass_context
def pathos(ctx):
    """🦢 PaTHos: The AI Pathway. Cygnus: Us. Geek the Greek."""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit(
            "[bold cyan]🦢 CYGNUS COMMAND CENTER[/bold cyan]\n"
            "[dim]Type 'invoke', 'sync', 'flow', 'vault', 'agon', or 'exit'[/dim]",
            style="cyan",
            border_style="bold cyan"
        ))
        while True:
            try:
                user_input = Prompt.ask("\n[bold green]🏛️ Architect, what is your command?[/bold green]", default="exit")
                if user_input.lower() in ['exit', 'quit', 'q']:
                    console.print("[bold green]Devs, I'm your AI Agent, and I approve of this session. Opa![/bold green]\n")
                    break
                elif user_input.lower() == 'sync':
                    run_sync_status()
                elif user_input.lower() == 'flow':
                    flow_status()
                elif user_input.lower() == 'vault':
                    vault.list_tokens()
                elif user_input.lower() == 'agon':
                    agon_menu()
                else:
                    console.print(f"[yellow]Unknown command: {user_input}.[/yellow]")
            except KeyboardInterrupt:
                console.print("\n[bold red]Session aborted.[/bold red]")
                break

@pathos.command()
@click.option('--agent', required=True)
@click.option('--function', required=True)
@click.option('--input', 'payload_input', required=True)
@click.option('--key', required=True)
@click.option('--provider', default="qwen", help="LLM provider")
def invoke(agent, function, payload_input, key, provider):
    try:
        console.print(Panel.fit("CYGNUS: Us. Geek the Greek. Opa!", style="bold cyan"))
        console.print(f"Loading Specialized Layer: [bold]{provider.upper()}[/bold]...")
        try:
            payload = json.loads(payload_input)
        except:
            payload = {"text": payload_input}
        result = llm_router.route(provider, payload_input)
        console.print("\n[bold green]📜 THE ORACLE HAS SPOKEN:[/bold green]")
        console.print(JSON.from_data(result))
        vibe = random.choice(["intro", "warmth", "workflow", "tweaks", "encouragement"])
        console.print(f"\n[dim italic]🎛️ Cygnus Note: {Oracle.speak(vibe)}[/dim italic]")
        console.print("[bold green]Devs, I'm your AI Agent, and I approve of this execution. Opa![/bold green]\n")
    except Exception as e:
        console.print(f"\n[bold red]⚡ SYSTEM ERROR[/bold red]\n{str(e)}")

@pathos.group()
def vault():
    """Manage the sovereign Token Vault."""
    pass

@vault.command()
@click.option('--provider', required=True)
@click.option('--token', required=True)
def add(provider, token):
    vault.add_token(provider, token)

@vault.command()
def list():
    vault.list_tokens()

@vault.command()
@click.option('--provider', required=True)
def remove(provider):
    vault.remove_token(provider)

@pathos.command()
def sync():
    """Check and configure sovereign P2P sync."""
    run_sync_status()

@pathos.group()
def flow():
    """Manage biometric Flow State frequencies."""
    pass

@flow.command()
@click.option('--mode', required=True, type=click.Choice(['deep', 'focus', 'renewal']))
def start(mode):
    start_flow(mode)

@flow.command()
def stop():
    stop_flow()

@flow.command()
def status():
    flow_status()

@pathos.command()
def agon():
    """Enter The Agon: Challenge the models with ancient Greek games."""
    agon_menu()

if __name__ == '__main__':
    pathos()
