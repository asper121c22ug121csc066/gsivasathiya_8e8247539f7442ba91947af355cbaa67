'''Implement a class called player that represents a cricket player.The player class should have a
method called play()which prints "The player is playing cicket.Derive two classes,Batman and
Bowler, from the player class.Override the play")method in each derived class to print "The batman
is batting" and "The bowler is bowling", respectively.Write a program to create objects of both the
Batman and Bowler classes and call the play()method for each objects.'''


#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batman
class Batman(player):
  def play(self):
      print("The batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
   def play(self):
       print("The bowler is bowling.")

#Create objects of Batman and Bowler classes
batsman = Batman()
bowler = Bowler()

#Call the play()method for each object
batsman.play()
bowler.play()
