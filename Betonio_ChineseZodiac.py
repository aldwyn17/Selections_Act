# Declare the variables of each chinese zodiac signs
rat_sign = (1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020)
ox_sign = (1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021)
tiger_sign = (1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022)
rabbit_sign = (1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023)
dragon_sign = (1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024)
snake_sign = (1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025)
horse_sign = (1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026)
goat_sign = (1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027)
monkey_sign = (1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028)
rooster_sign = (1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029)
dog_sign = (1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030)
pig_sign = (1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031)

# Use input function to take input from the user
year = eval(input("What is your birth year?\n"))

# Make an If-else statement
if year in rat_sign:
    print("Your chinese zodiac sign is Rat.")
elif year in tiger_sign:
    print("Your chinese zodiac sign is Tiger.")
elif year in rabbit_sign:
    print("Your chinese zodiac sign is Rabbit.")
elif year in dragon_sign:
    print("Your chinese zodiac sign is Dragon.")
elif year in snake_sign:
    print("Your chinese zodiac sign is Snake.")
elif year in horse_sign:
    print("Your chinese zodiac sign is Horse.")
elif year in goat_sign:
    print("Your chinese zodiac sign is Goat.")
elif year in monkey_sign:
    print("Your chinese zodiac sign is Monkey.")
elif year in rooster_sign:
    print("Your chinese zodiac sign is Rooster.")
elif year in dog_sign:
    print("Your chinese zodiac sign is Dog.")
elif year in pig_sign:
    print("Your chinese zodiac sign is Pig.")
else:
    print("The year", year, "is not counted in the Chinese Calendar.")
