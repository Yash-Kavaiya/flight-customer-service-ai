# API Reference - Flight Customer Service AI

## Overview

This document provides detailed API reference for the Flight Customer Service AI multi-agent system.

## Main Agent

### `customer_service_coordinator`

The primary entry point for all customer service interactions.

```python
from flight_customer_service import customer_service_coordinator

# Process a customer request
response = customer_service_coordinator.process_request(
    customer_input="I need help with my flight",
    context={"customer_id": "12345", "session_id": "abc-123"}
)
```

**Parameters:**
- `customer_input` (str): The customer's inquiry or request
- `context` (dict, optional): Additional context information

**Returns:**
- `response` (dict): Comprehensive response with routing and resolution information

## Sub-Agents

### Flight Information Agent

#### `flight_info_agent`

Specializes in real-time flight information and status updates.

```python
from flight_customer_service.sub_agents.flight_info import flight_info_agent

result = flight_info_agent.process({
    "flight_number": "AA123",
    "date": "2025-06-15",
    "airport_codes": ["LAX", "JFK"]
})
```

**Input Parameters:**
- `flight_number` (str): Flight identifier (e.g., "AA123")
- `date` (str): Travel date (ISO format or relative like "today")
- `airport_codes` (list): Departure and arrival airport codes
- `passenger_details` (dict, optional): Name or confirmation number

**Output:**
- Flight status and schedule information
- Gate and terminal details
- Delay information and alternatives

### Booking Management Agent

#### `booking_management_agent`

Handles all booking-related operations and modifications.

```python
from flight_customer_service.sub_agents.booking_management import booking_management_agent

result = booking_management_agent.process({
    "action": "modify_booking",
    "confirmation_number": "ABC123",
    "changes": {
        "seat_preference": "aisle",
        "meal_preference": "vegetarian"
    }
})
```

**Input Parameters:**
- `action` (str): Type of operation ("new_booking", "modify_booking", "cancel_booking")
- `confirmation_number` (str): Existing booking reference
- `passenger_details` (dict): Customer information
- `travel_requirements` (dict): Flight preferences and requirements
- `changes` (dict): Specific modifications requested

**Output:**
- Updated booking information
- Available options and alternatives
- Fee calculations and confirmations

### Baggage Services Agent

#### `baggage_services_agent`

Manages baggage tracking, claims, and related services.

```python
from flight_customer_service.sub_agents.baggage_services import baggage_services_agent

result = baggage_services_agent.process({
    "service_type": "track_baggage",
    "baggage_claim_number": "BAG789",
    "flight_details": {
        "flight_number": "UA456",
        "route": "SFO-ORD",
        "date": "2025-06-12"
    }
})
```

**Input Parameters:**
- `service_type` (str): Type of service ("track_baggage", "file_claim", "policy_info")
- `baggage_claim_number` (str): Tracking reference
- `flight_details` (dict): Associated flight information
- `passenger_info` (dict): Customer details
- `incident_details` (dict): For claims and issues

**Output:**
- Baggage status and location
- Claim processing information
- Compensation details

### Policy Support Agent

#### `policy_support_agent`

Provides policy information, emergency assistance, and support.

```python
from flight_customer_service.sub_agents.policy_support import policy_support_agent

result = policy_support_agent.process({
    "inquiry_type": "refund_policy",
    "ticket_type": "economy_basic",
    "booking_reference": "XYZ789",
    "circumstances": "flight_cancellation"
})
```

**Input Parameters:**
- `inquiry_type` (str): Type of policy question
- `booking_reference` (str): Relevant booking
- `customer_status` (dict): Loyalty program and ticket information
- `circumstances` (str): Specific situation or emergency type

**Output:**
- Policy explanations and applications
- Available options and alternatives
- Emergency assistance procedures

## Data Structures

### Customer Context

```python
customer_context = {
    "customer_id": "string",
    "session_id": "string",
    "loyalty_status": "string",
    "preferences": {
        "language": "string",
        "communication_channel": "string",
        "accessibility_needs": ["string"]
    },
    "booking_history": ["booking_reference"]
}
```

### Flight Information

```python
flight_info = {
    "flight_number": "string",
    "airline": "string",
    "aircraft_type": "string",
    "route": {
        "departure": {
            "airport_code": "string",
            "airport_name": "string",
            "terminal": "string",
            "gate": "string",
            "scheduled_time": "datetime",
            "estimated_time": "datetime",
            "actual_time": "datetime"
        },
        "arrival": {
            "airport_code": "string",
            "airport_name": "string",
            "terminal": "string",
            "gate": "string",
            "scheduled_time": "datetime",
            "estimated_time": "datetime",
            "actual_time": "datetime"
        }
    },
    "status": "string",
    "delay_reason": "string",
    "connections": ["flight_info"]
}
```

### Booking Details

```python
booking = {
    "confirmation_number": "string",
    "passengers": [{
        "name": "string",
        "passenger_type": "string",
        "seat_assignment": "string",
        "special_services": ["string"]
    }],
    "flights": ["flight_info"],
    "fare_details": {
        "fare_class": "string",
        "total_cost": "decimal",
        "taxes_fees": "decimal",
        "currency": "string"
    },
    "payment_info": {
        "method": "string",
        "status": "string"
    }
}
```

### Baggage Information

```python
baggage = {
    "claim_number": "string",
    "status": "string",
    "last_location": "string",
    "tracking_history": [{
        "timestamp": "datetime",
        "location": "string",
        "status": "string"
    }],
    "description": {
        "type": "string",
        "color": "string",
        "brand": "string",
        "size": "string"
    },
    "compensation": {
        "eligible": "boolean",
        "amount": "decimal",
        "currency": "string",
        "reason": "string"
    }
}
```

## Error Handling

### Common Error Codes

- `INVALID_INPUT`: Invalid or missing input parameters
- `AGENT_UNAVAILABLE`: Requested specialist agent is unavailable
- `DATA_NOT_FOUND`: Requested information not found
- `SYSTEM_ERROR`: Internal system error
- `RATE_LIMIT_EXCEEDED`: Too many requests in time period

### Error Response Format

```python
error_response = {
    "error": {
        "code": "string",
        "message": "string",
        "details": "string",
        "suggestion": "string"
    },
    "timestamp": "datetime",
    "request_id": "string"
}
```

## Configuration

### Environment Variables

```bash
# Google ADK Configuration
GOOGLE_ADK_API_KEY="your_api_key"
GOOGLE_ADK_PROJECT_ID="your_project_id"

# Model Configuration
MODEL_NAME="gemini-2.5-pro-preview-05-06"
MODEL_TEMPERATURE=0.3
MODEL_MAX_TOKENS=2048

# System Configuration
MAX_CONCURRENT_AGENTS=10
REQUEST_TIMEOUT=30
CACHE_TTL=300
```

### Agent Configuration

```python
agent_config = {
    "flight_info_agent": {
        "tools": ["google_search"],
        "max_search_results": 10,
        "cache_duration": 300
    },
    "booking_management_agent": {
        "tools": [],
        "simulation_mode": True,
        "fee_calculation": True
    },
    "baggage_services_agent": {
        "tools": [],
        "tracking_simulation": True,
        "compensation_calculator": True
    },
    "policy_support_agent": {
        "tools": ["google_search"],
        "emergency_escalation": True,
        "policy_database": True
    }
}
```

## Usage Examples

See `examples/basic_usage.py` for comprehensive usage examples and integration patterns.
