import pokebase as pb
chesto = pb.APIResource('berry', 'chesto')
print(chesto.natural_gift_type.name)
s1 = pb.SpriteResource('pokemon', 17)
print(s1)