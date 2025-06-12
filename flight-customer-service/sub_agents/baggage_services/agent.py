from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

baggage_services_agent = Agent(
    model=MODEL,
    name="baggage_services_agent",
    instruction=prompt.BAGGAGE_SERVICES_PROMPT,
    output_key="baggage_services_output",
)
