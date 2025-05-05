import random




# print(len(user_cards))

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

user_cards = [];
computer_cards = [];

# for loop range operator
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

print(f"user cards: {user_cards}")
print(f"dealer first card: {computer_cards[0]}")



draw_card = True;

while draw_card:

  if calculate_score(user_cards) == 0:
    print("You won!");
    draw_card = False;
  if calculate_score(computer_cards) == 0:
    print("dealer won.");
    draw_card = False;
  if draw_card:
    draw_again = input("Would you like to draw again?");
    if calculate_score(computer_cards) <= 16:
      computer_cards.append(deal_card());
    if draw_again == "yes":
      user_cards.append(deal_card());
      print(f"user cards: {user_cards}")
      print(f"dealer cards: {computer_cards[0]}")

    user_score = calculate_score(user_cards);
    computer_score = calculate_score(computer_cards);
    if user_score > 21:
      print("You lost.")
      draw_card = False;
    if computer_score > 21:
      print("You Won!")
      draw_card = False;
    if draw_again != "yes":
      if(user_score > computer_score):
        print("You Won!!")
      else:
        print("You lost :(")
      draw_card = False;
    

print(f"Your score was: {calculate_score(user_cards)}")
print(f"Dealer score was: {calculate_score(computer_cards)}")