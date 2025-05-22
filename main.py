import random
from art import logo

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
  return random.choice(cards);

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(u_score, c_score):
  if u_score == c_score:
    return "Draw 😐"
  elif c_score == 0:
    return "You lost. Dealer has Blackjack 😱"
  elif u_score == 0:
    return "You won with a Blackjack 😎"
  elif u_score > 21:
    return "You went over. You lose 😭"
  elif c_score > 21:
    return "Dealer went over. You win 🥳"
  elif u_score > c_score:
    return "You win 😃"
  else:
    return "You lose 🙁"
  

def play_blackjack():

  print(logo)
  user_cards = [];
  computer_cards = [];
  is_game_over = False;
  computer_score = -1;
  user_score = -1;

  # for loop range operator
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())




  while not is_game_over:

    user_score = calculate_score(user_cards);
    computer_score = calculate_score(computer_cards);

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"dealer first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21 or user_score == 21:
      is_game_over = True;
    else:
      draw_another_card = input("Type 'y' for Hit or 'n' for Stand: ")
      if draw_another_card == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score));


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  print("\n" * 20)
  play_blackjack()




""".------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/   
"""
  
