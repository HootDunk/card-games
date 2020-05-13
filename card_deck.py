
import random

def deck_of_cards():
	deck = []
	suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
	for suit in suits:
		for num in range(2, 15):
			if num < 11:
				deck.append(f"{num} of {suit}")
			elif num == 11:
				deck.append(f"Jack of {suit}")
			elif num == 12:
				deck.append(f"Queen of {suit}")
			elif num == 13:
				deck.append(f"King of {suit}")
			elif num == 14:
				deck.append(f"Ace of {suit}")

	return deck


def get_suit(card):
	if 'Hearts' in card:
		suit = 'Heart'
	elif 'Spades' in card:
		suit = 'Spades'
	elif 'Clubs' in card:
		suit = 'Club'
	elif 'Diamonds' in card:
		suit = "Diamond"

	return suit


def get_value(card):
	for num in range(2, 11):
		if f'{num}' in card:
			value = num
	if 'Jack' in card:
		value = 'Jack'
	elif 'Queen' in card:
		value = 'Queen'
	elif 'King' in card:
		value = 'King'
	elif 'Ace' in card:
		value = 'Ace'

	return value


def same_value(card1, card2):
	card1_value = get_value(card1)
	card2_value = get_value(card2)

	if card1_value == card2_value:
		return True
	elif card1_value != card2_value:
		return False


def same_value_extended(cards):
	card_values = []
	for card in cards:
		value = get_value(card)
		card_values.append(value)
	card_values.append(None)

	results = []
	i = 0
	while card_values[i] != None:
		if card_values[i+1] != None:
			if card_values[i] == card_values[i+1]:
				results.append(0)
			elif card_values[i] != card_values[i+1]:
				results.append(1)
		i += 1

	if 1 in results:
		same_value = False
	else:
		same_value = True

	return same_value


def same_suit(card1, card2):
	card1_suit = get_suit(card1)
	card2_suit = get_suit(card2)

	if card1_suit == card2_suit:
		return True
	elif card1_suit != card2_suit:
		return False

def same_suit_extended(cards):
	card_suits = []
	for card in cards:
		value = get_suit(card)
		card_suits.append(value)
	card_suits.append(None)

	results = []
	i = 0
	while card_suits[i] != None:
		if card_suits[i+1] != None:
			if card_suits[i] == card_suits[i+1]:
				results.append(0)
			elif card_suits[i] != card_suits[i+1]:
				results.append(1)
		i += 1

	if 1 in results:
		same_value = False
	else:
		same_value = True

	return same_value

def deal_top_card(deck):
	top_card = deck.pop(0)

	return top_card

def get_random_card(deck):
	random_card = random.choice(deck)
	deck.remove(random_card)

	return random_card

def shuffle_deck(deck):
	'''the random.shuffle(deck) changes the deck, to keep
	the existing deck you would want to use random.sample()'''
	random.shuffle(deck)  

	return deck

def deal_hand(deck, size):
	hand = []
	for i in range(size):
		card = deal_top_card(deck)
		hand.append(card)

	return hand

def deal_hand(deck, hand_size, num_hands):
	"""consider using a dict"""
	hands = []
	for hand in range(num_hands):
		hands.append([])

	hand_index = 0
	for hand in hands:
		for _ in range(hand_size):
			card = deal_top_card(deck)
			hands[hand_index].append(card)

		hand_index += 1

	return hands

def give_cards(num_of_players, hands):
	if num_of_players == 2:
		player1 = hands[0]
		player2 = hands[1]
		return player1, player2
	elif num_of_players == 3:
		player1 = hands[0]
		player2 = hands[1]
		player3 = hands[2]
		return player1, player2, player3
	elif num_of_players == 4:
		player1 = hands[0]
		player2 = hands[1]
		player3 = hands[2]
		player4 = hands[3]
		return player1, player2, player3, player4

 
