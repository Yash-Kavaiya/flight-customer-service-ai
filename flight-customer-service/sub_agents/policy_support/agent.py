from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

policy_support_agent = Agent(
    model=MODEL,
    name="policy_support_agent",
    instruction=prompt.POLICY_SUPPORT_PROMPT,
    output_key="policy_support_output",
    tools=[google_search],
)
