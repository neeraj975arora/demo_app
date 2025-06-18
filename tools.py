from langchain.tools import Tool
from search_places import search_places
from get_weather import get_weather
from find_hotels import find_hotels
from suggest_itinerary import suggest_itinerary

search_places_tool = Tool(
    name="search_places",
    func=search_places,
    description="Use this tool to find points of interest in a city."
)

get_weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Use this tool to get the current weather for a city."
)

find_hotels_tool = Tool(
    name="find_hotels",
    func=find_hotels,
    description="Use this tool to find hotel options in a city."
)

suggest_itinerary_tool = Tool(
    name="suggest_itinerary",
    func=suggest_itinerary,
    description="Use this tool to generate a trip itinerary prompt for a city and number of days."
)

tools = [search_places_tool, get_weather_tool, find_hotels_tool, suggest_itinerary_tool] 