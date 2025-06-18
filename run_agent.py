from agent_setup import get_agent_executor

def main():
    city = "Manali"
    days = 4
    agent_executor = get_agent_executor(city, days)
    user_input = f"Plan a {days}-day trip to {city}."
    print("\nGenerating your itinerary for Manali (4 days)...\n")
    response = agent_executor.invoke({
        "city": city,
        "days": days,
        "input": user_input
    })
    print("\n--- Generated Itinerary ---\n")
    print(response)

if __name__ == "__main__":
    main() 