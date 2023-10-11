from fruits import fruits
from game_card import Game_card
from tabulate import tabulate
import random
import re
import time

class Game_zone:
    def __init__(self, fruits):
        self.fruits = fruits
        self._total_cards = 16
        self._left_cards = 16
        self.two_dimensional_cards = self.generate_card()
        self.current_card = ''


    # initialize the game
    def game_initialize(self):
        self.generate_simulate_game_area()

    # Those methods below are used for initialize the game
    def pick_fruit(self):
        picked_fruits = []
        for _ in range(8):
            picked_fruit = random.choice(self.fruits)
            picked_fruits.append(picked_fruit)
        return picked_fruits

    def combine_fruits(self):
        fruits = self.pick_fruit()
        random_fruits_list = fruits + fruits
        random.shuffle(random_fruits_list)
        return random_fruits_list

    def generate_card(self):
        ramdom_fruits = self.combine_fruits()
        fruit_cards = []
        for i, fruit in enumerate(ramdom_fruits):
            card = Game_card(i, fruit)
            fruit_cards.append(card)
        # change the 16 one_dimensional_card_list into 4x4 two_dimensional_card_list
        two_dimensional_cards = [fruit_cards[i:i+4] for i in range(0, len(fruit_cards), 4)]
        return two_dimensional_cards

    # render cards table
    def render_cards_table(self):
        cards_table = []
        for row in self.two_dimensional_cards:
            row_list = []
            for card in row:
                if card.card_info()['is_matched']:
                    row_list.append('')
                elif card.card_info()['is_click']:
                    row_list.append(card.card_info()['text'])
                else:
                    row_list.append('#')
            cards_table.append(row_list)
        return tabulate(cards_table, tablefmt="double_grid")

    def match_success(self):
        self._left_cards -= 2

    def is_game_completed(self):
        return self._left_cards == 0

    def user_select_card(self, row, col):
        select_card = self.two_dimensional_cards[row][col]
        select_card_info = select_card.card_info()
        select_card.flip_over()
        if select_card_info['is_matched']:
            print(f"DON'T FLIP THE MATCHED CARD PLS~")
            return
        else:
            print(f"You flipped the card [{select_card_info['text']}]")
            if self.current_card and self.current_card != select_card:
                self.validate_two_cards(select_card)
            elif self.current_card and self.current_card == select_card:
                return
            elif not self.current_card:
                self.current_card = select_card


    def validate_two_cards(self, select_card):
        # if flip the cards with the same value, remove those two
        if self.current_card.card_info()['value'] == select_card.card_info()['value']:
            self.current_card.card_matched()
            select_card.card_matched()
            self.match_success()
            self.current_card = ''
            return True
        else:
            self.current_card.flip_down()
            select_card.flip_down()
            self.current_card = ''
            return False

def main():
    new_game = Game_zone(fruits)
    start_time = time.time()
    while not new_game.is_game_completed():
        print(new_game.render_cards_table())
        card_index = input('Flip A Card: ').strip()
        if matches := re.search(r'^[1-4] ?, ?[1-4]$', card_index):
            row, col = matches.group().split(',')
            row_index = int(row.strip()) - 1
            col_index = int(col.strip()) - 1
            new_game.user_select_card(row_index, col_index)
            continue
        else:
            continue
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"You spent {elapsed_time:.2f} seconds to get success! Proud of you!")


if __name__ == "__main__":
    main()