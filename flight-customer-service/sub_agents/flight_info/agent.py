from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

flight_info_agent = Agent(
    model=MODEL,
    name="flight_info_agent",
    instruction=prompt.FLIGHT_INFO_PROMPT,
    output_key="flight_info_output",
    tools=[google_search],
)
