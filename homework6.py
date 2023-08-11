some_string = "київ,оДеса Львів.житоМИР,уЖгОрОд.....ХарКІВ , слАвУтИч".replace(',', ' ').replace('.', ' ')
city_names = some_string.split()
formatted_city_names = [name.title() for name in city_names]

for city in formatted_city_names:
    message = f"Я \U00002764 {city}"
    print(message)
