class GirlsConnectHeroes:
  def draw(self): pass

class UltimateRare(GirlsConnectHeroes):
  def draw(self):
    print('my favorite UR class heroes is Kuzunoha Jr.')

class SuperRare(GirlsConnectHeroes):
  def draw(self):
    print('my favorite SR class heroes is Tenjin')

class Rare(GirlsConnectHeroes):
  def draw(self):
    print('my favorite R class hero is Galford')

class GirlsConnectHeroesClass:
  @staticmethod
  def getHeroesClass(type):
    if type == 'ultimate rare':
      return UltimateRare()
    elif type == 'super rare':
      return SuperRare()
    elif type == 'rare':
      return Rare()
    assert 0, type + 'ini tidak valid'