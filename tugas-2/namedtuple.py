import collections

Uno = collections.namedtuple('Uno', ['rank', 'color'])

class UnoCard:
    ranks = [str(n) for n in range(1, 10)] + ['reverse', 'block', 'plus_two']
    colors = 'red yellow green blue'.split()

    def __init__(self):
        self._unos = [Uno(rank, color) for rank in self.ranks for color in self.colors]
        for i in range(0,4):
            self._unos.append(Uno('plus_four', 'black'))
            self._unos.append(Uno('switch_color', 'black'))

    def __len__(self):
        return len(self._unos)

    def __getitem__(self, position):
        return self._unos[position]
    
    def returnAll(self):
        return self._unos

run = UnoCard
for i in run().returnAll():
    print(i)