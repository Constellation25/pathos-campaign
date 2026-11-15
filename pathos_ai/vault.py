import os
import json
from pathlib import Path
from cryptography.fernet import Fernet
from rich.console import Console
from rich.table import Table

console = Console()

VAULT_FILE = Path.home() / ".pathos_vault.json"
KEY_FILE = Path.home() / ".pathos_master_key"

class TokenVault:
    def __init__(self):
        self._ensure_master_key()
        self.fernet = self._load_fernet()
        
    def _ensure_master_key(self):
        if not KEY_FILE.exists():
            key = Fernet.generate_key()
            KEY_FILE.write_bytes(key)
            KEY_FILE.chmod(0o600)
    
    def _load_fernet(self):
        key = KEY_FILE.read_bytes()
        return Fernet(key)
    
    def _load_vault(self):
        if not VAULT_FILE.exists():
            return {}
        try:
            encrypted_data = VAULT_FILE.read_bytes()
            decrypted_data = self.fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data)
        except Exception as e:
            return {}
    
    def _save_vault(self, data):
        json_data = json.dumps(data).encode()
        encrypted_data = self.fernet.encrypt(json_data)
        VAULT_FILE.write_bytes(encrypted_data)
        VAULT_FILE.chmod(0o600)
    
    def add_token(self, provider, token):
        vault = self._load_vault()
        vault[provider] = token
        self._save_vault(vault)
        console.print(f"[bold green]✅ Token for '{provider}' stored.[/bold green]")
    
    def get_token(self, provider):
        vault = self._load_vault()
        return vault.get(provider)
    
    def remove_token(self, provider):
        vault = self._load_vault()
        if provider in vault:
            del vault[provider]
            self._save_vault(vault)
            console.print(f"[bold green]✅ Token for '{provider}' removed.[/bold green]")
    
    def list_tokens(self):
        vault = self._load_vault()
        if not vault:
            console.print("[bold yellow]⚠️ Vault is empty.[/bold yellow]")
            return
        
        table = Table(title="🔐 PaTHos Token Vault")
        table.add_column("Provider", style="cyan")
        table.add_column("Status", style="green")
        
        for provider in vault.keys():
            table.add_row(provider, "✅ Stored")
        
        console.print(table)

vault = TokenVault()
