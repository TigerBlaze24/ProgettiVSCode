
class Zoo:
    def __init__(self, fences, zoo_keepers):
        self.fences = fences
        self.zoo_keepers = zoo_keepers
        self.animal_counter = 0  #aggiunge un contatore per gli animali

    def add_animal(self, animal, fence):
        if animal.preferred_habitat == fence.habitat and animal.height * animal.width <= fence.area:
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width
            self.animal_counter += 1  # Incrementa il contatore quando aggiungi un animale
            print("L'animale è stato correttamente aggiunto al recinto.")
        else:
            print("Non è possibile aggiungere l'animale al recinto date le dimensioni o l'habitat errato.")

    def remove_animal(self, animal, fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
        else:
            print("L'animale non è nel recinto.")

    def add_zoo_keeper(self):
        nome = input("Inserisci il nome del guardiano: ")
        cognome = input("Inserisci il cognome del guardiano: ")
        id = len(self.zoo_keepers)  # Assegna l'ID del guardiano
        keeper = ZooKeeper(nome, cognome, id)
        self.zoo_keepers.append(keeper)
        print(f"Guardiano {nome} {cognome} aggiunto.")

    def remove_zoo_keeper(self):
        nome = input("Inserisci il nome del guardiano da rimuovere: ")
        cognome = input("Inserisci il cognome del guardiano da rimuovere: ")
        for keeper in self.zoo_keepers:
            if keeper.nome.lower() == nome.lower() and keeper.cognome.lower() == cognome.lower():
                self.zoo_keepers.remove(keeper)
                print(f"Guardiano {nome} {cognome} rimosso.")
                break
        else:
            print("Nessun guardiano trovato con questo nome e cognome.")

    def add_fence(self, area, temperature, habitat):
        id = len(self.fences)  # Assegna l'ID del recinto
        fence = Fence(id, area, temperature, habitat)
        self.fences.append(fence)
        print(f"Recinto con habitat {habitat} aggiunto.")

   

    def describe_zoo(self):
        print("\nGuardiani:")
        for keeper in self.zoo_keepers:
            print(f"Nome: {keeper.nome}, Cognome: {keeper.cognome}, ID: {keeper.id}")

        print("\nRecinti:")
        for fence in self.fences:
            print(
                f"\n{'#' * 30}\nID Recinto: {fence.id}, Habitat: {fence.habitat}, Area: {fence.area}, Temperatura: {fence.temperature}")
            if fence.animals:
                print("Animali:")
                for animal in fence.animals:
                    print(
                        f"ID Animale: {animal.id}, Nome: {animal.name}, Specie: {animal.species}, Età: {animal.age}, Altezza: {animal.height}, Larghezza: {animal.width}, Habitat preferito: {animal.preferred_habitat}, Salute: {animal.health}")
                    
class Animal:
    def __init__(self, id, name, species, age, height, width, preferred_habitat):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

class Fence:
    def __init__(self, id, area, temperature, habitat):
        self.id = id
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

class ZooKeepers:
    def __init__(self, nome, cognome, id):
        self.nome = nome
        self.cognome = cognome
        self.id = id

    def feed(self, animal, fence):
        if animal.height * animal.width * 1.02 <= fence.area:
            animal.health *= 1.01
            animal.height *= 2.02
            animal.width *= 3.02
        else:
            print("Non c'è abbastanza spazio nel recinto per nutrire l'animale.")

    def clean(self, fence):
        occupied_area = sum([animal.height * animal.width for animal in fence.animals])
        remaining_area = fence.area - occupied_area
        if remaining_area != 0:
            return occupied_area / remaining_area
        else:
            return occupied_area
def get_object_by_attribute(objects, attribute, value):
    matched_objects = []
    for obj in objects:
        if getattr(obj, attribute).lower() == value.lower():
            matched_objects.append(obj)

    if len(matched_objects) > 1:
        print(f"Ci sono più oggetti con lo stesso {attribute}. Ecco i dettagli:")
        for i, obj in enumerate(matched_objects, start=1):
            print(f"{i}. ID: {obj.id}, {attribute.capitalize()}: {getattr(obj, attribute)}")
        id = int(input(f"Inserisci l'ID dell'{attribute} da selezionare: "))
        for obj in matched_objects:
            if obj.id == id:
                return obj
        else:
            print(f"Nessun {attribute} trovato con questo ID.")
    elif matched_objects:
        return matched_objects[0]
    else:
        print(f"Nessun {attribute} trovato con valore {value}.")         
     
ZooKeeper = [ZooKeepers("Teo", "Maggi", 123)]
animal = Animal("Alex", "leone", 20, 2.00, 4.00, 42, "Savana")
fence = Fence(323, 800, 35, "Savana")
zoo = Zoo([], ZooKeeper)  # Crea un'istanza della classe Zoo
zoo.add_animal(animal, fence)  # Aggiungi l'animale al recinto
zoo.fences.append(fence)  # Aggiungi il recinto allo zoo
zoo.describe_zoo()  # Ora puoi chiamare describe_zoo() 
