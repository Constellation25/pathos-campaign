from .oracle import Oracle

class LicenseError(Exception):
    pass

class CygnusOrchestrator:
    def __init__(self):
        self.mantra = "Cygnus: Us. Geek the Greek."

    def verify_key(self, key):
        if not key or key != "TEST-KEY-123":
            raise LicenseError("CYGNUS DENIED: Invalid Constellation Key.")
        return True

    def invoke(self, agent_name, function_name, payload, key):
        self.verify_key(key)
        from .pantheon import run_agent_function
        result_data = run_agent_function(function_name, **payload)
        final_result = {"status": "success", "agent": agent_name, "data": result_data}
        final_result["oracle_wisdom"] = Oracle.speak(agent_name)
        return final_result

cygnus = CygnusOrchestrator()
