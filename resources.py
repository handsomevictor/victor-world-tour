# If a place that I stayed:
# for 1 day, the score is 1
# for more than 2 days, score is 2
# for more than 5 days, score is 3
# for more than 1 month, score is 4
# for more than 6 months, score is 5
# for more than 1 year, score is 6
# for more than 4 years, score is 7

all_places = {
    "France":
        {
            "Paris": 7,
            "Strasbourg": 2,
            "Marseille": 2,
            "Nice": 3,
            "Toulon": 2,
            "Normandie": 2
        },
    "Spain":
        {
            "Barcelona": 5,
            "Madrid": 1,
            "Valencia": 1,
            "Murcia": 1,
            "Seville": 1,
            "Cadiz": 1,
            "Zaragoza": 2,
            "Malaga": 1,
            "Bilbao": 3,
            "Tarifa": 2,
        },
    "United Kingdom":
        {
            "London": 3,
            "Cambridge": 2,
        },
    "Netherlands":
        {
            "Amsterdam": 2,
            "Rotterdam": 2,
            "Den Haag": 1,
        },
    "Belgium":
        {
            "Brussels": 2,
            "Brugge": 1,
            "Ghent": 1,
        },
    "Germany":
        {
            "Berlin": 2,
            "Munich": 1,
            "Frankfurt": 1,
            "Hamberg": 1,
        },
    "Poland":
        {
            "Warsaw": 2,
            "Krakow": 2,
            "Gdansk": 1,
            "Katowice": 1,
            "Chochołów": 1,
            "Puck": 1,
            'Gdynia': 1,
            "Zakopane": 2,
        },
    "Czech Republic":
        {
            "Prague": 1,
        },
    "Austria":
        {
            "Vienna": 2,
        },
    "Hungary":
        {
            "Budapest": 3,
        },
    "Slovakia":
        {
            "Bratislava": 1,
        },
    "Italy":
        {
            "Venice": 3,
            "Dolomites": 2,
        },
    "Switzerland":
        {
            "Lucerne": 1,
            "Thun": 2,
            "Zurich": 1,
            "Bern": 1,
            "Interlaken": 1,
            "Basel": 1,
        },
    "Greece":
        {
            "Athens": 2,
            "Thessaloniki": 2,
        },
    "Turkey":
        {
            "Istanbul": 2,
            "Izmir": 2,
            "Mardin": 1,
        },
    "Morocco":
        {
            "Marrakech": 1,
            "Tangier": 1,
            "Fes": 1,
            "Chefchaouen": 2,
            "Rabat": 1,
        },
    "Jordan":
        {
            "Amman": 2,
            "Aqaba": 2,
            "Wadi Rum": 1,
        },
    "Japan":
        {
            "Tokyo": 2,
            "Kyoto": 4,
            "Osaka": 2,
        },
    "South Korea":
        {
            "Seoul": 2,
            "Daejeon": 4,
        },
    "China":
        {
            "Beijing": 7,
            "郑州": 7,
            "Shanghai": 4,
            "Hangzhou": 3,
            "Suzhou": 2,
            "Guilin": 2,
            "Xian": 3,
            "Haerbin": 2,
            "Zhangjiajie": 2,
            "Tangshan": 3,
            "Wuhan": 2,
            "Shenzhen": 3,
            "Urumqi": 2,
            "Kashgar": 2,
            "Hetian": 2,
            "Atushi": 4,
            "Xilingol": 3,
            "Dalian": 2,
            "Tianjin": 3,
            "Hong Kong": 3,
        },
    "Taiwan":
        {
            "Taipei": 3,
            "Taichung": 1,
            "Tainan": 1,
            "Kaohsiung": 2,
        },
    "Thailand":
        {
            "Bangkok": 3,
            "Phuket": 4,
            "Pattaya": 2,
         },
    "Singapore":
        {
            "Singapore": 3,
        },
    "United States":
        {
            "New York": 2,
            "Los Angeles": 1,
            "San Francisco": 2,
            "Miami": 2,
            "Orlando": 2,
            "Washington DC": 2,
            "Boston": 2,
            "Philadelphia": 1,
            "Houston": 2,
            "Atlanta": 3,
            "Denver": 2,
        },
    "Syria":
        {
            "Qamishli": 1,
        },
}


