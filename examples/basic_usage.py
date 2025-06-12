#!/usr/bin/env python3
"""
Basic usage example for the Flight Customer Service AI system.

This example demonstrates how to use the multi-agent customer service system
to handle various types of customer inquiries.
"""

import sys
sys.path.append('..')

from flight_customer_service import customer_service_coordinator

def main():
    """Demonstrate basic usage of the customer service system."""
    
    print("Flight Customer Service AI - Basic Usage Example")
    print("=" * 50)
    
    # Example 1: Flight Information Inquiry
    print("\n1. Flight Information Inquiry:")
    print("-" * 30)
    
    flight_inquiry = {
        "customer_request": "I need to check the status of flight AA123 departing from LAX to JFK today",
        "flight_number": "AA123",
        "route": "LAX to JFK",
        "date": "today"
    }
    
    print(f"Customer Request: {flight_inquiry['customer_request']}")
    print("System would route to: Flight Information Agent")
    print("Expected Response: Real-time flight status, gate info, delays, etc.")
    
    # Example 2: Booking Management
    print("\n2. Booking Management Request:")
    print("-" * 30)
    
    booking_inquiry = {
        "customer_request": "I need to change my seat assignment and meal preference for my upcoming flight",
        "confirmation_number": "ABC123",
        "service_type": "seat_change_and_meal"
    }
    
    print(f"Customer Request: {booking_inquiry['customer_request']}")
    print("System would route to: Booking Management Agent")
    print("Expected Response: Seat map, available options, meal choices, confirmation")
    
    # Example 3: Baggage Services
    print("\n3. Baggage Services Request:")
    print("-" * 30)
    
    baggage_inquiry = {
        "customer_request": "My baggage didn't arrive with my flight. I need to track it and file a claim",
        "baggage_claim_number": "BAG789",
        "flight_details": "UA456 from SFO to ORD"
    }
    
    print(f"Customer Request: {baggage_inquiry['customer_request']}")
    print("System would route to: Baggage Services Agent")
    print("Expected Response: Tracking status, claim process, compensation info")
    
    # Example 4: Policy Support
    print("\n4. Policy Support Request:")
    print("-" * 30)
    
    policy_inquiry = {
        "customer_request": "What are the cancellation fees for my ticket and can I get a refund?",
        "ticket_type": "economy_basic",
        "booking_reference": "XYZ789"
    }
    
    print(f"Customer Request: {policy_inquiry['customer_request']}")
    print("System would route to: Policy Support Agent")
    print("Expected Response: Cancellation policy, fee structure, refund options")
    
    # Example 5: Multi-Agent Coordination
    print("\n5. Complex Multi-Agent Request:")
    print("-" * 30)
    
    complex_inquiry = {
        "customer_request": "My flight was cancelled due to weather. I need rebooking, want to change my seat, and my baggage is missing",
        "issue_types": ["flight_disruption", "rebooking", "seat_selection", "baggage_tracking"]
    }
    
    print(f"Customer Request: {complex_inquiry['customer_request']}")
    print("System would coordinate: Flight Info + Booking Management + Baggage Services + Policy Support")
    print("Expected Response: Comprehensive solution addressing all aspects")
    
    print("\n" + "=" * 50)
    print("Note: This is a demonstration of the system architecture.")
    print("In actual usage, the agents would provide real responses.")
    print("=" * 50)

def demonstrate_agent_capabilities():
    """Show the capabilities of each specialized agent."""
    
    print("\nAgent Capabilities Overview:")
    print("=" * 50)
    
    agents = {
        "Flight Information Agent": [
            "Real-time flight status monitoring",
            "Gate and terminal information",
            "Delay notifications and reasons",
            "Alternative flight options",
            "Airport services and amenities"
        ],
        "Booking Management Agent": [
            "New flight reservations",
            "Booking modifications and cancellations",
            "Seat selection and upgrades",
            "Special service requests",
            "Payment and refund processing"
        ],
        "Baggage Services Agent": [
            "Baggage tracking and status",
            "Lost baggage claims",
            "Compensation procedures",
            "Special baggage handling",
            "Policy information"
        ],
        "Policy Support Agent": [
            "Fare rules and restrictions",
            "Refund policies",
            "Emergency assistance",
            "Travel insurance information",
            "Loyalty program support"
        ]
    }
    
    for agent_name, capabilities in agents.items():
        print(f"\n{agent_name}:")
        print("-" * len(agent_name))
        for capability in capabilities:
            print(f"  • {capability}")

if __name__ == "__main__":
    main()
    demonstrate_agent_capabilities()
