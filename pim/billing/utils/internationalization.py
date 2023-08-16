import pycountry

countries = sorted([(country.alpha_2, country.name) for country in pycountry.countries])
currencies = sorted(
    [
        (currency.alpha_3, f'{currency.alpha_3} ({currency.name})')
        for currency in pycountry.currencies
    ]
)
