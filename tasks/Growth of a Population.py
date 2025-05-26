def nb_year(p0, percent, aug, p):
    years = 0
    current_population = p0
    
    while current_population < p:
        growth = current_population * (percent / 100)
        current_population += int(growth) + aug
        years += 1
    
    return years