class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']  ## Class attribute
    def __init__(self, name, species):
        if species not in self.allowed:
            raise ValueError(f'You can have a {species} as a pet!')
        self.name = name
        self.species = species
    
    def set_species(self, species):
        if species not in self.allowed:
            raise ValueError(f'You can have a {species} as a pet!')
        self.species = species
    
cat = Pet('Blue', 'cat')
dog = Pet('Wyatt', 'dog')


