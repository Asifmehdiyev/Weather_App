import streamlit as st
import requests

API_KEY = "c84a868ca7734d0ba15130117230906"

def fetch_weather_data(country, city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city},{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract relevant weather information from the JSON response
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        weather_description = data['current']['condition']['text']

        # Styling for the weather information boxes
        st.markdown("<h3 style='text-align: center;'>Weather Information</h3>", unsafe_allow_html=True)

        # Box design for the temperature with icon
        st.info(f"Temperature: {temperature}°C")

        # Box design for the humidity with icon
        st.info(f"Humidity: {humidity}%")

        # Box design for the weather description with icon
        st.info(f"Weather description: {weather_description}")

    else:
        st.write("Error fetching weather data.")

def get_city_country_names():
    # Make a request to the Geonames API to get city and country names
    base_url = "http://api.geonames.org/searchJSON"
    username = "asifmehdiyev"
    params = {
        "q": "*",
        "maxRows": 1000,  # Maximum number of rows to retrieve
        "featureClass": "P",  # Restrict results to populated places
        "username": username
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    city_country_list = []
    for result in data["geonames"]:
        city = result.get("name", "")
        country = result.get("countryName", "")
        if city and country:
            city_country_list.append((city, country))

    return city_country_list



def get_weather():
    # Custom CSS to change the main theme color to green and center-align the elements
    st.markdown("""
    <style>
    .stApp {
        background-size:cover;
        width:100%;        
         background-repeat: no-repeat;
        background-image: url("https://images.unsplash.com/photo-1496450681664-3df85efbd29f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80");
        background-color: green;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
        width: 400px;
    }
    
    .select-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        gap: 10px;
        max-width: 250px;
    }
    
    .button-container {
        flex: 0;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 5px;
        max-width: 250px;
    }
    
    </style>
    """,unsafe_allow_html=True)


    # Adding the Font Awesome CSS
    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <style>
        .fas {
            margin-right: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Styling for the 'Weather App' text
    st.markdown("<h1 style='text-align: center; color: white;'>Weather App</h1>", unsafe_allow_html=True)

    # Specify the country and city using selectboxes
    country = st.selectbox("Select Country", ["Argentina", "Australia", "Austria", "Azerbaijan","Bahrain", "Belgium", "Brazil",
                                              "Bulgaria", "Canada", "Croatia", "Czech Republic", "Denmark", "Dominican Republic",
                                              "Egypt", "Finland", "France", "Germany", "Greece", "Hong Kong SAR China", "Hungary",
                                              "India", "Indonesia", "Ireland", "Italy", "Japan", "Jordan", "South Korea", "Malaysia",
                                              "Macao SAR, China", "Mexico", "Morocco", "Netherlands", "Norway", "Poland", "Portugal",
                                              "Romania", "Russian Federation", "Saudi Arabia", "Singapore", "South Africa", "Spain",
                                              "Sweden", "Switzerland", "Thailand", "Tunisia", "Turkey", "Ukraine", "United Kingdom",
                                              "United States", "Vietnam"])
    
    # Dynamically update the list of cities based on the selected country
    if country:
        city_options = []
        if country == "Argentina":
            city_options = ["Buenos Aires", "Mar del Plata", "San Carlos de Bariloche", "Salta", "Mendoza", "Ushuaia", "Cordoba",
                            "Rosario", "La Plata"]
        elif country == "Australia":
            city_options = ["Canberra", "Adelaide", "Brisbane", "Darwin", "Gold Coast", "Hobart", "Cairns", "Perth", "Melbourne",
                            "Sydney"]
        elif country == "Austria":
            city_options = ["Vienna", "Graz", "Feldkirch", "Baden bei Wien", "Salzburg", "Linz", "Eisenstadt", "Innsbruck", "Bregenz", "Krems an der Donau"]
        elif country == "Azerbaijan":
            city_options = ["Baku", "Ganja", "Sumgayit", "Lankaran", "Sheki", "Guba", "Nakhchivan", "Shusha", "Gabala"]
        elif country == "Bahrain":
            city_options = ["Manama", "Isa Town", "Jidhafs", "Riffa", "Hamad Town", "Budaiya", "Muharraq", "Sitra", "Al Hidd"]
        elif country == "Belgium":
            city_options = ["Bruges", "Antwerp", "Liege", "Brussels", "Leuven", "Namur", "Ghent", "Mechelen", "Mons", "Dinant"]
        elif country == "Brazil":
            city_options = ["Rio de Janeiro", "Sao Paolo", "Salvador", "Brasilia", "Recife", "Fortaleza", "Manaus", "Curitiba", "Belo Horizonte", "Florianópolis"]
        elif country == "Bulgaria":
            city_options = ["Sofia", "Plovdiv", "Varna", "Burgas", "Veliko Tarnovo", "Bansko", "Nessebar", "Ruse", "Sozopol", "Koprivshtitsa"]
        elif country == "Canada":
            city_options = ["Toronto", "Montreal", "Calgary", "Ottawa", "Edmonton", "Winnipeg", "Mississauga", "Vancouver", "Brampton", "Hamilton"]
        elif country == "Croatia":
            city_options = ["Dubrovnik", "Split", "Zagreb", "Zadar", "Rovinj", "Sibenik", "Trogir", "Rijeka", "Makarska", "Osijek"]
        elif country == "Czech Republic":
            city_options = ["Prague", "Olomouc", "Brno", "Cesky Krumlov", "Liberec", "Ceske Budejovice", "Karlovy Vary", "Pilsen", "Ostrava", "Kutna Hora"]
        elif country == "Denmark":
            city_options = ["Copenhangen", "Aarhus", "Odense", "Aalborg", "Roskilde", "Skagen", "Esbjerg", "Helsingor", "Ribe", "Vejle"]
        elif country == "Dominican Republic":
            city_options = ["Santo Domingo", "Punta Cana", "Puerto Plata", "La Romana", "Cabarete", "Samana", "Las Terrenas", "Sosua", "Jarabacoa", "Bayahibe"]
        elif country == "Egypt":
            city_options = ["Cairo", "Alexandria", "Luxor", "Aswan", "Hurghada", "Sharm El-Sheikh", "Dahab", "Giza", "Marsa Alam", "Siwa Oasis"]
        elif country == "Finland":
            city_options = ["Helsinki", "Turku", "Tampere", "Rovaniemi", "Porvoo", "Oulu", "Jyväskylä", "Savonlinna", "Espoo", "Kuopio"]
        elif country == "France":
            city_options = ["Nice", "Paris", "Lyon", "Bordeaux", "Strasbourg", "Marseille", "Toulouse", "Lille", "Nantes", "Montpellier"]
        elif country == "Germany":
            city_options = ["Berlin", "Hamburg", "Munich", "Frankfurt", "Cologne", "Stuttgart", "Dusseldof", "Leipzig", "Dresden", "Nuremberg"]
        elif country == "Greece":
            city_options = ["Athens", "Thessaloniki", "Nafplio", "Mykonos", "Santorini", "Meteora", "Rhodes", "Corfu", "Heraklion", "Chania"]
        elif country == "Hong Kong SAR China":
            city_options = ["Mongkok", "Tsim Sha Tsui", "Tai O", "Lan Kwai Fong", "Nathan Road", "Causeway Bay"]
        elif country == "Hungary":
            city_options = ["Budapest", "Lake Balaton", "Eger", "Pecs", "Debrecen", "Szentendre", "Szeged", "Esztergom", "Győr", "Sopron"]
        elif country == "India":
            city_options = ["Mumbai", "Kolkata", "Chennai", "Agra", "Hyderabad", "Varanasi", "Jaipur", "Bangalore", "New Delhi", "Udaipur"]
        elif country == "Indonesia":
            city_options = ["Jakarta", "Yogyakarta", "Bandung", "Surabaya", "Medan", "Ubud", "Lombok", "Makassar", "Semarang", "Kuta"]
        elif country == "Ireland":
            city_options = ["Dublin", "Galway", "Cork", "Killarney", "Kilkenny", "Kerry", "Killarney National Park", "Waterford", "Limerick", "Glendalough"]
        elif country == "Italy":
            city_options = ["Venice", "Rome", "Milan", "Florence", "Bologna", "Verona", "Turin", "Sinea", "Genoa", "Cinque Terre"]
        elif country == "Japan":
            city_options = ["Kyoto", "Osaka", "Tokyo", "Hiroshima", "Sapporo", "Yokohama", "Fukuoka", "Nagoya", "Kobe", "Kanazawa"]
        elif country == "Jordan":
            city_options = ["Petra", "Amman", "Wadi Room Protected Area", "Aqaba", "Jerash", "The Treasury", "Madaba", "Dana Biosphere Reservce", "Wadi Musa", "Irbid"]
        elif country == "South Korea":
            city_options = ["Seoul", "Busan", "Jeju-si", "Gyeongju-si", "Incheon", "Daegu", "Jeonju-si", "Seoraksan National Park", "Gwangju", "Daejeon"]
        elif country == "Malaysia":
            city_options = ["Kuala Lumpur", "Ipoh", "Malacca", "Kuching", "Kota Kinabalu", "George Town", "Johor Bahru", "Putrajaya", "Cameron Highlands", "Kota Bharu"]
        elif country == "Mexico":
            city_options = ["Mexico City", "Merida", "Oaxaca", "Cancun", "San Miguel de Allende", "Guadalajara", "Puerto Vallarta", "Puebla", "Guanajuato", "Playa del Carmen"]
        elif country == "Morocco":
            city_options = ["Fes", "Essaouira", "Chefchaouen", "Marrakesh", "Rabat", "Tangier", "Meknes", "Casablanca", "Agadir", "Asilah"]
        elif country == "Netherlands":
            city_options = ["Amsterdam", "Rotterdam", "The Hague", "Utrecht", "Maastricht", "Delft", "Haarlem", "Best", "Leiden", "Arnhem"]
        elif country == "Norway":
            city_options = ["Oslo", "Ålesund", "Bergen", "Stavanger", "Trondheim", "Bodø", "Lillehammer", "Tromsø Municipality", "Fredrikstad", "Kristiansand"]
        elif country == "Poland":
            city_options = ["Kraków", "Warsaw", "Gdańsk", "Poznań", "Wrocław", "Zakopane", "Lublin", "Łódź", "Toruń", "Katowice"]
        elif country == "Portugal":
            city_options = ["Lisbon", "Porto", "Coimbra", "Evora", "Braga", "Sintra", "Aveiro", "Guimaraes", "Faro District", "Óbidos"]
        elif country == "Romania":
            city_options = ["Bucharest", "Brașov", "Sibiu", "Cluj-Napoca", "Timișoara", "Sighișoara", "Constanța", "Iași", "Suceava", "Oradea"]
        elif country == "Russian Federation":
            city_options = ["Saint Petersburg", "Moscow", "Kazan", "Sochi", "Vladivostok", "Yekaterinburg", "Nizhny Novgorod", "Veliky Novgorod", "Suzdal", "Irkutsk"]
        elif country == "Saudi Arabia":
            city_options = ["Jeddah", "Riyadh", "Hegra", "Al Ula", "Diriyah", "Medina", "Dammam", "Masmak Fortress", "Al Masjid an Nabawi", "King Fahd's Fountain"]
        elif country == "South Africa":
            city_options = ["Capetown", "Johannesburg", "Durban", "Port Elizabeth", "Pretoria", "Bloemfontein", "Knysna", "Western Cape", "Stellenbosch", "Oudtshoorn"]
        elif country == "Spain":
            city_options = ["Barcelona", "Madrid", "Seville", "Granada", "Valencia", "Bilbao", "Donostia-San Sebastian", "Córdoba", "Toledo", "Alicante"]
        elif country == "Sweden":
            city_options = ["Malmö", "Stockholm", "Gothenburg", "Uppsala", "Linköping", "Örebro", "Kiruna", "Visby", "Kalmar", "Västerås"]
        elif country == "Switzerland":
            city_options = ["Zürich", "Lucerne", "Geneva", "Bern", "Interlaken", "Lausanne", "Lugano", "Zermatt", "Basel", "St. Gallen"]
        elif country == "Thailand":
            city_options = ["Bangkok", "Chiang Mai", "Krabi", "Phra Nakhon Si Ayutthaya", "Pattaya City", "Mueang Chiang Rai", "Kanchanaburi", "Phuket", "Nakhon Ratchasima", "Hua Hin"]
        elif country == "Tunisia":
            city_options = ["Tunis", "Sidi Bou Said", "Hammamet", "Sousse", "Djerba", "Kairouan", "Dougga", "Carthage", "Sfax", "Medina of Tunis"]
        elif country == "Turkey":
            city_options = ["Istanbul", "Antalya", "Ankara", "Konya", "Izmir", "Bursa", "Bodrum", "Trabzon", "Ephesus", "Fethiye"]
        elif country == "Ukraine":
            city_options = ["Kyiv", "Lviv", "Odessa", "Kharkiv", "Chernivtsi", "Chernihiv", "Uzhhorod", "Zaporizhzhia", "Dnipro", "Mukachevo"]
        elif country == "United Kingdom":
            city_options = ["London", "Manchester", "Liverpool", "Edinburgh", "Cambridge", "Oxford", "Bristol", "Birmingham", "Brighton", "Bath"]
        elif country == "United States":
            city_options = ["New York City", "San Francisco", "Washington DC", "New Orleans", "Seattle", "Las Vegas", "San Diego", "Miami", "Charleston", "Nashville"]
        elif country == "Vietnam":
            city_options = ["Hội An", "Hanoi", "Hue", "Ho Chi Minh City", "Nha Trang", "Da Nang", "Dalat", "Sa Pa", "Ninh Binh", "Can Tho"]
        # Add more countries and their corresponding cities here
        
        city = st.selectbox("Select City", city_options)  # Will be populated based on the selected country
        
        if st.button('Get Weather'):
            fetch_weather_data(country, city)

if __name__ == '__main__':
    get_weather()
