class Art:

    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner
    
    def __repr__(self):

        return (f'The artist name is {self.artist}. The tile of the art work is {self.title}. '
                    f'Year of work is {self.year}. The medium for art is {self.medium}. '
                    f'The owner of the artwork is {self.owner.name}, {self.owner.location}. ')




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
        self.is_museum = is_museum
        if self.is_museum:
            self.location = location
        else:
            self.location = 'Private Collection'

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            listing = (Listing(artwork, price, self))
            veneer.add_listing(listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self and artwork in veneer.listings:
            artwork.owner = self.name
            veneer.remove_listing(artwork)


edytta = Client('Edytta Halpirt', None, False)
moma = Client('The MOMA', 'New York', True)

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Maddolin', 1910, 'Oil on canvas', edytta)


class Listing:

    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f'Name of the art work is {self.art.title},' \
            f'the price of the art work is {self.price} '

edytta.sell_artwork(girl_with_mandolin, '$6 Million')

veneer.show_listing()
