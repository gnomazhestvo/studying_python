def city_contry(city, country, population=''):
    if population:
        message = f"{city.title()}, {country.title()} - population {population}"
    else:
        message = f"{city.title()}, {country.title()}"
    return message