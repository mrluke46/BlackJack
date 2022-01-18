
1. Create a Card class in Python. It should have an __init__, __str__, __repr__

__init__ should take in either a suite and value or a JSON object that gets converted into the class. We want some sort of standard too, so it should convert numbers to words and all upper case so the suite is either "HEARTS", "DIAMONDS", "SPADES", "CLUBS" and the values are "ACE", "TWO", "THREE", ... "JACK", "QUEEN", "KING".

__str__ should return a string that you could print out

__repr__ should return the JSON object

__eq__ should return True if the cards are equal

__ne__ should return True if the cards are not equal

(Bonus id you look at how to do greater than, less than, etc.)

In addition to these built in functions, you should have the following:
isFaceCard(): returns True or False if it's a face card.
isSameSuite(): returns True or False if the suite is the same.
isSameValue(): returns True or False if the value is the same

2. Create a Deck class in Python that is a collection of exactly 52 cards. It should have the __init__, __str__ and __repr__ functions but also a shuffle, dealt, undealt, dealCard

3. Test classes

Look at unittest and pytest.

Eventually we’ll have a Hand class and then eventually we’ll have a game

Like a Game class. The Game class will have have Cards, Hands, and a Deck
