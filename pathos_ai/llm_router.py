from rich.console import Console
from .vault import vault

console = Console()

class LLMRouter:
    def __init__(self):
        self.providers = {
            "qwen": self._call_qwen,
            "openai": self._call_openai,
            "anthropic": self._call_anthropic,
            "google": self._call_google,
            "local": self._call_local
        }
    
    def _call_qwen(self, prompt, model="Qwen/Qwen2.5-72B-Instruct"):
        return {"provider": "qwen", "model": model, "response": f"[Qwen] {prompt[:50]}..."}
    
    def _call_openai(self, prompt, model="gpt-4"):
        api_key = vault.get_token("openai")
        if not api_key:
            raise ValueError("OpenAI key not found. Run 'pathos vault add --provider openai'")
        return {"provider": "openai", "model": model, "response": f"[OpenAI] {prompt[:50]}..."}
    
    def _call_anthropic(self, prompt, model="claude-3-opus"):
        api_key = vault.get_token("anthropic")
        if not api_key:
            raise ValueError("Anthropic key not found.")
        return {"provider": "anthropic", "model": model, "response": f"[Anthropic] {prompt[:50]}..."}
    
    def _call_google(self, prompt, model="gemini-pro"):
        api_key = vault.get_token("google")
        if not api_key:
            raise ValueError("Google key not found.")
        return {"provider": "google", "model": model, "response": f"[Google] {prompt[:50]}..."}
    
    def _call_local(self, prompt, model="local"):
        return {"provider": "local", "model": model, "response": f"[Local] {prompt[:50]}..."}
    
    def route(self, provider, prompt, **kwargs):
        if provider not in self.providers:
            raise ValueError(f"Unknown provider: {provider}")
        return self.providers[provider](prompt, **kwargs)

llm_router = LLMRouter()
