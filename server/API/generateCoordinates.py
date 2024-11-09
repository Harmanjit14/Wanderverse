# myapp/API/generateCoordinates.py

import graphene
import random

# Predefined list of coordinates (latitude, longitude)
PREDEFINED_COORDINATES = [
    (52.9715, -9.4309),  # Cliffs of Moher, Ireland
    (37.9715, 23.7257),  # Acropolis, Athens, Greece
    (48.8584, 2.2945),   # Eiffel Tower, Paris, France
    (41.8902, 12.4922),  # Colosseum, Rome, Italy
    (37.9715, 23.7267),  # Parthenon, Athens, Greece
    (41.4036, 2.1744),   # Sagrada Familia, Barcelona, Spain
    (51.1789, -1.8262),  # Stonehenge, Wiltshire, England
    (43.7229, 10.3966),  # Leaning Tower of Pisa, Italy
    (37.7412, -25.6756)  # Azores, Portugal
]

class GenerateCoordinates(graphene.ObjectType):
    latitude = graphene.Float()
    longitude = graphene.Float()

class Query(graphene.ObjectType):
    generate_coordinates = graphene.Field(GenerateCoordinates)

    def resolve_generate_coordinates(self, info):
        # Select a random coordinate from the predefined list
        latitude, longitude = random.choice(PREDEFINED_COORDINATES)
        return GenerateCoordinates(latitude=latitude, longitude=longitude)
