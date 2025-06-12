from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

booking_management_agent = Agent(
    model=MODEL,
    name="booking_management_agent",
    instruction=prompt.BOOKING_MANAGEMENT_PROMPT,
    output_key="booking_management_output",
)
