from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating, nickname):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.nickname = nickname
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Fcb', 'Mr.', 24, 4.7, 'Best')

friend_1 = Spy('Messi', 'Mr.', 25, 4.8, 'God')
friend_2 = Spy('Suarez', 'Mr.', 23, 4.6, 'Finesse')
friend_3 = Spy('Neymar', 'Mr.', 25, 4.9, 'Dribble-god')
friend_4 = Spy('Iniesta', 'Mr.', 35, 4.7, 'Don')
friend_5 = Spy('Pique', 'Mr.', 32, 4.5, 'Piquenbauer')

friends = [friend_1, friend_2, friend_3, friend_4, friend_5]
