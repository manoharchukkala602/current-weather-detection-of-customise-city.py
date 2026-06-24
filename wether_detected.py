import python_weather
import asyncio

city =input("Enter your city:")
async def get_weather():
    async with  python_weather.Client() as clint:
        weather =await clint.get(city)
        print(f"temperature of :{city}:{weather.temperature}")
        print(f"humudity of:{city}:{weather.humidity}")
        print(f"cloud cover of :{city}:{weather.cloud_cover}")
        print(f"country of :{city}:{weather.country}")
        print(f"date time of city:{city}:{weather.datetime}")
        print(f"decsription of city:{city}:{weather.description}")
        print(f"feels like of city:{city}:{weather.feels_like}")
        print(f"kind of city:{city}:{weather.kind}")
        print(f"location population of city:{city}:{weather.local_population}")
        print(f" location of the city:{city}:{weather.location}")
        print(f" preciption of city:{city}:{weather.precipitation}")
        print(f"coordinates of city;{city}:{weather.coordinates}")
        print(f"daily forecating :{city};{weather.daily_forecasts}")
        
asyncio.run(get_weather())