11#Blackjack
from p1_random import P1Random
def main():

	rng = P1Random()
	x = 0
	y = 0
	# Starting games at -1 and adding one when the game starts means that the number of games will show as 1 when the first game is completed
	num_games = -1
	wins = 0
	ties = 0
	losses = 0

	while x != 4:

		if y == 0: #Will use y = 0 and y = 1 to switch on and off the sequence to start a new game

			num_games += 1
			hand = 0 #Reset hand after game
			print(f'START GAME #{num_games + 1}')
			print('')
			card_value = rng.next_int(13) + 1
			y = 1 #Turn off start game sequence until a player wins or loses

			#Change non number cards to their real name and adjust their value
			if card_value == 1:
				card_name = 'ACE'
				card_value_adjusted = 1
			elif card_value > 1 and card_value < 11:
				card_name = card_value
				card_value_adjusted = card_value
			elif card_value == 11:
				card_name = 'JACK'
				card_value_adjusted = 10
			elif card_value == 12:
				card_name = 'QUEEN'
				card_value_adjusted = 10
			elif card_value == 13:
				card_name = 'KING'
				card_value_adjusted = 10

			hand = card_value_adjusted #Adjust hand to new card value
			print(f'Your card is a {card_name}!')
			print(f'Your hand is: {hand}')
			print('')
			print('1. Get another card')
			print('2. Hold hand')
			print('3. Print statistics')
			print('4. Exit')
			print('')
			x = int(input('Choose an option: '))
		#When user inputs 1 as their choice it starts this part of the loop
		if x == 1:
			print('')
			card_value = rng.next_int(13) + 1
			if card_value == 1:
				card_name = 'ACE'
				card_value_adjusted = 1
			elif card_value > 1 and card_value < 11:
				card_name = card_value
				card_value_adjusted = card_value
			elif card_value == 11:
				card_name = 'JACK'
				card_value_adjusted = 10
			elif card_value == 12:
				card_name = 'QUEEN'
				card_value_adjusted = 10
			elif card_value == 13:
				card_name = 'KING'
				card_value_adjusted = 10
			#Hand gets newly drawn card added to it
			hand += card_value_adjusted
			print(f'Your card is a {card_name}!')
			print(f'Your hand is: {hand}')
			print('')
			#Win sequence if hand is 21, y becomes 0 to start new game, x becomes 0 so the rest of the elif isnt ran
			if hand == 21:
				print('BLACKJACK! You win!')
				print('')
				wins += 1
				x, y = 0, 0
			#If hand is over 21 lose game, y and x = 0 to start new game
			elif hand > 21:
				print('You exceeded 21! You lose.')
				print('')
				losses += 1
				x, y = 0, 0
			#If hand is less than 21 let player choose option
			elif hand < 21:
				print('1. Get another card')
				print('2. Hold hand')
				print('3. Print statistics')
				print('4. Exit')
				print('')
				x = int(input('Choose an option: '))
		#If player chooses 2 to hold hand, dealer card is drawn
		elif x == 2:
			dealers_hand = rng.next_int(11) + 16
			#If dealer hand is > 21 dealer loses
			if dealers_hand > 21:
				print('')
				print(f"Dealer's hand: {dealers_hand}")
				print(f'Your hand is: {hand}')
				print('')
				print('You win!')
				print('')
				wins += 1
			#If dealer and player are equal, tie, start new game
			elif dealers_hand == hand:
				print('')
				print(f"Dealer's hand: {dealers_hand}")
				print(f'Your hand is: {hand}')
				print('')
				print("It's a tie! No one wins!")
				print('')
				ties += 1
			#If dealer hand is bigger than player hand but less than 22 you lose
			elif dealers_hand > hand and dealers_hand < 22:
				print('')
				print(f"Dealer's hand: {dealers_hand}")
				print(f'Your hand is: {hand}')
				print('')
				print('Dealer wins!')
				print('')
				losses += 1
			x, y = 0, 0
		#If player chooses 3 show stats for game
		elif x == 3:
			if num_games == 0:
				print('No games played!')
				print('')
				x = int(input('Choose an option: '))
			else:
				print('')
				print(f'Number of Player wins: {wins}')
				print(f'Number of Dealer wins: {losses}')
				print(f'Number of tie games: {ties}')
				print(f'Total # of games played is: {wins + losses + ties}')
				#Calculate win percent from wins over total games *100
				win_percent = (wins / (wins + losses + ties)) * 100
				print(f'Percentage of Player wins: {win_percent:.1f}%')
				print('')
				print('1. Get another card')
				print('2. Hold hand')
				print('3. Print statistics')
				print('4. Exit')
				print('')
				x = int(input('Choose an option: '))
		#If user inputs number other than 0-4 the game asks you to input proper number
		else:
			print('')
			print('Invalid input!')
			print('Please enter an integer value between 1 and 4.')
			print('')
			print('1. Get another card')
			print('2. Hold hand')
			print('3. Print statistics')
			print('4. Exit')
			print('')
			x = int(input('Choose an option: '))








if __name__ == "__main__":
	main()

