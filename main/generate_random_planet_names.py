"""
Program to generate random names for the planets
"""
from random import randint

names = """Adlai
Aitor
Alaric
Arsen
Art
Aryan
Aurelius
Aurik
Auryn
Azriel
Blaze
Caddell
Caedin
Cael
Calihan
Callen
Calloway
Carrew
Cashel
Seraphina
Sereia
Seren
Serena
Severine
Sheena
Shiloh
Silvia
Sirena
Skylar
Sloane
Snow
Sofie
Sol
Solana
Soleil
Solene
Sonata
Sonnet
Sonora
Caspian
Cassian
Cathal
Cato
Cedro
Cian
Cillian
Lior
Lore
Lucius
Lumina
Lux
Lylah
Lyra
Lyric
Lys
Lysa
Lysander
Lysandra
Lystra
Lunara
Luxora
Marni
Dowo
Mazarine
Meghan
Meryl
Minerva
Crispin
Cyrano
Dagger
Derry
Timorus
Annora
Antheia
Antinea
Aquilina
Aquilo
Arcadia
Arden
Ardith
Arella
Aria
Ariadne
Ariane
Ariel
Arlo
Artemis
Artemisia
Ascella
Ash
Aspen
Astera"""

all_names = names.split('\n')

def generate_random_planet_names(how_many):
    generated_names = []

    for i in range(0, how_many):
        type = randint(0, 3)

        name = all_names[randint(0, len(all_names)-1)]

        if type == 2:
            name = name + '-' + all_names[randint(0, len(all_names)-1)]
        
        if type > 2 or type == 1:
            name = name + '-' + str(randint(3, 17))

        generated_names.append(name)

    return generated_names