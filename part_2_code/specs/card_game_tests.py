import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace = Card("Spades", 1)
        self.card = Card("Clubs", 3)
        self.card1 = Card("Hearts", 10 )

        self.hand = [self.ace, self.card, self.card1]
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertTrue(self.card_game.check_for_ace(self.ace))
    

    def test_check_highest_card(self):
        self.highest_card = self.card_game.highest_card(self.card1, self.card)
        self.assertEqual(self.highest_card.value, 10)

    def test_total_cards(self):
        self.assertEqual(self.card_game.cards_total(self.hand),"You have a total of 14")
