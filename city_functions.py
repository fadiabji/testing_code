
def city_country(city_name, country_name, population=''):
    """ function to retrun the city and country names neatly"""
    if population:
        return f"{city_name.title()}, {country_name.title()} - population: {population}."
    else:
        return f"{city_name.title()}, {country_name.title()},"


