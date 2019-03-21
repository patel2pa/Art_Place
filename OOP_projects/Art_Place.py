
class Art:

    def __init__(self, artist, title, year, medium):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    
    def __repr__(self):
        return (f'The artist name is {self.artist}. The tile of the art work is {self.title}. Year of work is {self.year}. The medium for art is {self.medium} ')

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Maddolin', 1910, 'Oil on canvas')


class Marketplace:

    def __init__(self):
        self.listings = []
        
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listing(self):
        for listing in self.listings:
            print(listing)

veneer = Marketplace()
veneer.show_listing()
    

class Client:

    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum
    
