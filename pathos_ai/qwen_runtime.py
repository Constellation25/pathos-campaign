import os
import sys
from pathlib import Path

class QwenRuntime:
    """Pre-configured Qwen runtime for instant terminal access."""
    
    def __init__(self):
        # Pre-set model configuration
        self.model_name = os.getenv("QWEN_MODEL", "Qwen/Qwen2.5-72B-Instruct")
        self.model_path = os.getenv("QWEN_MODEL_PATH", str(Path.home() / ".cache" / "qwen"))
        self.device = os.getenv("QWEN_DEVICE", "cpu")  # or "cuda" if GPU available
        self.dtype = os.getenv("QWEN_DTYPE", "float16")
        
        # Ensure model directory exists
        Path(self.model_path).mkdir(parents=True, exist_ok=True)
        
    def is_model_cached(self):
        """Check if the model is already downloaded."""
        model_dir = Path(self.model_path) / self.model_name.replace("/", "--")
        return model_dir.exists() and any(model_dir.glob("*.bin"))
    
    def get_quick_load_command(self):
        """Returns the command to quickly load Qwen."""
        if self.is_model_cached():
            return f"python3 -c \"from transformers import AutoModelForCausalLM, AutoTokenizer; model = AutoModelForCausalLM.from_pretrained('{self.model_name}', cache_dir='{self.model_path}'); print('✅ Qwen loaded and ready.')\""
        else:
            return f"python3 -c \"from transformers import AutoModelForCausalLM; model = AutoModelForCausalLM.from_pretrained('{self.model_name}', cache_dir='{self.model_path}'); print('⬇️ Downloading Qwen to {self.model_path}...')\""

# Global instance
qwen_runtime = QwenRuntime()
