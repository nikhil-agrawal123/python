def new_population(population, growth_rate, years):
    rate = growth_rate / 100
    a = 0
    while a <years:
        population += population * rate
        rate -= 0.001
        a+=1
    return population

def max_population_year(population, growth_rate):

    current_year = 0
    population_growth = growth_rate
    max_population = 0
    out = 0
    previous_population = 0
    
    while True:
        current_year += 1
        current_population = 0
        
        for i in population:
            current_population += new_population(i, population_growth, current_year)
            population_growth -= 0.4

        if current_population < previous_population:
            break
        elif current_population > max_population:
            out = current_year
            max_population = current_population
        previous_population = current_population
        population_growth = growth_rate
    return out

print(max_population_year([50, 1450, 1400, 1700, 1500, 600, 1200], 2.5))

def test():
    assert max_population_year([50, 1450, 1400, 1700, 1500, 600, 1200], 2.5) == 13
    assert max_population_year([50, 1450, 1400, 1700, 1500, 600, 1200], 2.25) == 11


test()

#bonus

def max_population_year_2(population, growth_rate):

    max_population = 0
    max_population_year = 0
    previous_population = 0
    current_year = 0

    while True:
        current_year += 1
        total_current_population = 0
        
        for i in range(len(population)):
            population_growth = growth_rate[i]
            z = population[i]
            total_current_population += new_population(z, population_growth, current_year)
            population_growth -= 0.4

        if total_current_population < previous_population:
            break
        elif total_current_population > max_population:
            max_population = total_current_population
            max_population_year = current_year
        previous_population = total_current_population
        population_growth = growth_rate
    return max_population_year, max_population

print(max_population_year_2([50, 1450, 1400, 1700, 1500, 600, 1200], [2,2.25,2.5,2.75,3,3.25,3.5]))