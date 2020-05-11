SEARISE=1.6
for num in range(1,26): 
    SEARISE = SEARISE * num 

print(format(num, '2.0f'), '\t', format(num* SEARISE, '5.2f'), 'milimeter')


