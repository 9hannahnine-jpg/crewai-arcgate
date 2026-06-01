from typing import Any, Dict, List, Optional, Union

ARC_GATE_BASE_URL = "https://web-production-6e47f.up.railway.app/v1"

class ArcGateLLM:
    """Drop-in LLM wrapper for CrewAI that routes through Arc Gate governance."""

    def __init__(self, model="gpt-4o-mini", api_key="demo", base_url=ARC_GATE_BASE_URL,
                 temperature=0.7, deployment_id=None, session_id=None, policy_mode=None):
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.temperature = temperature
        self.deployment_id = deployment_id
        self.session_id = session_id
        self.policy_mode = policy_mode
        self._llm = self._build()

    def _build(self):
        try:
            from crewai import LLM
        except ImportError:
            raise ImportError("crewai is required: pip install crewai")
        headers = {"Authorization": f"Bearer {self.api_key}"}
        if self.deployment_id:
            headers["X-Sentry-Deployment"] = self.deployment_id
        if self.session_id:
            headers["x-arc-session-id"] = self.session_id
        if self.policy_mode:
            headers["x-arc-policy-mode"] = self.policy_mode
        return LLM(
            model=f"openai/{self.model}",
            base_url=self.base_url,
            api_key=self.api_key,
            temperature=self.temperature,
            extra_headers=headers,
        )

    def call(self, messages, tools=None, callbacks=None, available_functions=None):
        return self._llm.call(
            messages=messages, tools=tools,
            callbacks=callbacks, available_functions=available_functions,
        )

    def __getattr__(self, name):
        return getattr(self._llm, name)
