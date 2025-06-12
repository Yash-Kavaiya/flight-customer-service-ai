# Flight Customer Service AI

A comprehensive multi-agent AI system for flight customer service using specialized agents to handle different aspects of airline customer support.

## System Overview

This system provides exceptional customer service by orchestrating specialized agents to handle various aspects of airline customer support including flight information, booking management, baggage services, and policy-related inquiries.

## Architecture

### Main Coordinator Agent
Routes customers to appropriate specialists and manages the overall service experience.

### Four Specialized Sub-Agents

1. **Flight Information Agent** - Real-time flight status, schedules, delays, gate changes
2. **Booking Management Agent** - New reservations, modifications, cancellations, seat selection
3. **Baggage Services Agent** - Baggage tracking, lost luggage claims, policies, compensation  
4. **Policy & Support Agent** - Fare rules, refunds, fees, emergency assistance, loyalty programs

## Project Structure

```
flight-customer-service/
├── __init__.py
├── agent.py
├── prompt.py
└── sub_agents/
    ├── flight_info/
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    ├── booking_management/
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    ├── baggage_services/
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    └── policy_support/
        ├── __init__.py
        ├── agent.py
        └── prompt.py
```

## Key Features

- **Specialized Expertise**: Each agent focuses on specific customer service domains
- **Coordinated Assistance**: Seamless handoffs between specialists with shared context
- **Real-time Information**: Flight and policy agents use search tools for current data
- **Emergency Response**: Built-in crisis management and emergency rebooking capabilities
- **Comprehensive Coverage**: Handles all major airline customer service scenarios

## Customer Journey Flow

1. Customer contacts the coordinator with their inquiry
2. Coordinator analyzes the request and routes to appropriate specialist(s)
3. Specialist(s) provide expert assistance using their specialized knowledge and tools
4. Coordinator ensures resolution and offers additional support
5. Follow-up and documentation as needed

## Agent Capabilities

### Flight Information Agent
- Flight status monitoring (on-time, delayed, cancelled)
- Gate assignments and terminal information
- Schedule information and connection details
- Weather and external factor impacts
- Airport services and amenities

### Booking Management Agent
- New flight reservations and fare comparison
- Booking modifications (dates, routes, passengers)
- Cancellations and refund processing
- Seat selection and upgrades
- Special services (meals, accessibility, pets)

### Baggage Services Agent
- Real-time baggage tracking
- Lost baggage claims and search coordination
- Baggage policy information
- Compensation procedures and reimbursement
- Special baggage handling (sports equipment, instruments)

### Policy & Support Agent
- Fare rules and ticket restrictions
- Refund policies and fee structures
- Travel insurance information
- Emergency response and crisis management
- Loyalty program support

## Technology Stack

- **Framework**: Google ADK (Agent Development Kit)
- **Model**: Gemini 2.5 Pro Preview
- **Tools**: Google Search integration for real-time information
- **Architecture**: Multi-agent coordination pattern

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Yash-Kavaiya/flight-customer-service-ai.git
   cd flight-customer-service-ai
   ```

2. Install dependencies:
   ```bash
   pip install google-adk
   ```

3. Configure your environment with appropriate API credentials

4. Import and use the root agent:
   ```python
   from flight_customer_service import root_agent
   ```

## Usage Example

```python
from flight_customer_service import customer_service_coordinator

# The coordinator will route customers to appropriate specialists
# and handle the complete customer service interaction
response = customer_service_coordinator.process_request(
    "I need help with my flight status and want to change my seat"
)
```

## Service Standards

- **Response Time**: Immediate acknowledgment with specialist routing
- **Accuracy**: Real-time information from authoritative sources
- **Empathy**: Understanding and addressing customer concerns
- **Resolution**: Complete problem-solving with follow-up
- **Proactivity**: Anticipating needs and offering solutions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue in this repository.
