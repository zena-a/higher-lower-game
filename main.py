#The Higher Lower Game based on which Instagram user has the most followers. 
import random
from ascii_art import logo, vs
from game_data import data
from clearscreen import clear

#Choose a random person
def set_person():
  """Returns a random Instagram user from the game data list"""
  person = random.choice(data)
  return person

#Compares two persons to find out who has the most followers
def compare(person1, person2):
  """Takes the user's follower count and returns the choice (A or B) that represents the user with the most followers"""
  if person1 > person2:
    return "A"
  else:
    return "B"

#Runs the game until player chooses wrong answer
def higher_lower():
  """Generates Instagram users to be compared until the player guesses the wrong answer."""
  end_game = False
  score = 0
  person_a = set_person()
  person_b = set_person()

  while not end_game:
    followers_a = person_a['follower_count']
    followers_b = person_b['follower_count']

    print(f"Compare A: {person_a['name']} a {person_a['description']} from {person_a['country']}")

    print(vs)

    print(f"Compare B: {person_b['name']} a {person_b['description']} from {person_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    answer = compare(followers_a, followers_b) 

    if choice == answer:
      score += 1
      person_a = person_b
      person_b = set_person()
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
    else: 
      end_game = True
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")

print(logo)
higher_lower()
