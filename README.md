# crewai-arcgate

**Arc Gate runtime governance for CrewAI agents. One line of code.**

## Install

```bash
pip install crewai-arcgate
```

## Usage

```python
from crewai_arcgate import ArcGateLLM
from crewai import Agent, Task, Crew

# Get your free key at web-production-6e47f.up.railway.app/signup
llm = ArcGateLLM(model="gpt-4o-mini", api_key="your-arc-gate-key")

agent = Agent(role="Researcher", goal="Research safely", llm=llm)
task = Task(description="Research AI safety", agent=agent)
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

## Get your free API key

https://web-production-6e47f.up.railway.app/signup — 500 free requests, no credit card.

Unlimited: $29/month at bendexgeometry.com

## About

Built by Bendex Geometry. Part of the Bendex Arc platform.
