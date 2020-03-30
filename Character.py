from characters import quarentine
class Character():

    def __init__(self, name, job, location, color, cards):
        self.name    = name
        self.job       = job
        self.location = location
        self.color     = color
        self.cards     = cards


char_quarentine = Character(
    quarentine.info['name'],
    quarentine.info['job'],
    quarentine.info['location'],
    quarentine.info['color'],
    quarentine.info['cards']
)

