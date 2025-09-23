import random
class Personnage:
  def __init__(self, nbreDeVie, nbreDePotions):
    self.vie=nbreDeVie
    self.potions=nbreDePotions
  def donneEtat (self):
    return self.vie
  def perdVie (self):
    if random.random()>0.5:
      nbPoint = 1
    else :
      nbPoint = 2
    self.vie=self.vie-nbPoint
  def boirePotion (self):
    if self.potions>0:
        self.vie=self.vie+1
        self.potions-=1

def game():
  bilbo = Personnage(20,5)
  gollum = Personnage(20,5)
  while bilbo.donneEtat()>0 and gollum.donneEtat()>0 :
    if bilbo.donneEtat()<5:
      bilbo.boirePotion()
      print("Bilbo a bu une potion")
    bilbo.perdVie()
    if gollum.donneEtat()<5:
      gollum.boirePotion()
      print("Gollum a bu une potion")
    gollum.perdVie()
  if bilbo.donneEtat()<=0 and gollum.donneEtat()>0:
    msg = f"Gollum est vainqueur, il lui reste encore {gollum.donneEtat()} points alors que Bilbo est mort"
  elif gollum.donneEtat()<=0 and bilbo.donneEtat()>0:
    msg = f"Bilbo est vainqueur, il lui reste encore {bilbo.donneEtat()} points alors que Gollum est mort"
  else :
    msg = "Les deux combattants sont morts en même temps"
  return msg
