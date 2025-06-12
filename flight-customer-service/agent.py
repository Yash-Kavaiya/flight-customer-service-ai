from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.flight_info import flight_info_agent
from .sub_agents.booking_management import booking_management_agent
from .sub_agents.baggage_services import baggage_services_agent
from .sub_agents.policy_support import policy_support_agent

MODEL = "gemini-2.5-pro-preview-05-06"

customer_service_coordinator = LlmAgent(
    name="customer_service_coordinator",
    model=MODEL,
    description=(
        "Provide comprehensive flight customer service assistance by "
        "coordinating specialized agents to handle flight information, "
        "booking management, baggage services, and policy support."
    ),
    instruction=prompt.CUSTOMER_SERVICE_COORDINATOR_PROMPT,
    output_key="customer_service_output",
    tools=[
        AgentTool(agent=flight_info_agent),
        AgentTool(agent=booking_management_agent),
        AgentTool(agent=baggage_services_agent),
        AgentTool(agent=policy_support_agent),
    ],
)

root_agent = customer_service_coordinator
