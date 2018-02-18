"""
    Exercise 40 Modules, Classes, and Objects

    In which our intrepit instructor explains how to get things done in Python 
    and along the way exposes his anti-OO biases.
"""
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hb_lyrics = ["Happy birthday to you"
, "I don't want to get sued"
, "So I will stop right there"]
happy_bday = Song(hb_lyrics)

bop_lyrics = ["They rally around the family"
, "With pockets full of shells"]

bulls_on_parade = Song(bop_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()