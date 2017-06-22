from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

STATUS_MESSAGES = ['FCB <3', 'Visca Barca', 'Mes Que Un Club', 'Barca for life']

print colored("Welcome! Let\'s start being a spy!", 'blue', 'on_green')

question = "Would like to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


def add_status():

    updated_status_message = None

    if spy.current_status_message is not None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You have no status message currently \n'

    default = raw_input("Would like to select from your older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("Set status message of your choice ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'Invalid option! Press y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You have no status update currently. You can add the status update from the menu.'

    return updated_status_message


def add_friend():

    new_friend = Spy('', '', 0, 0.0, '')

    new_friend.name = raw_input("Let\'s add your friend. Enter your friends name:")
    new_friend.salutation = raw_input('What would you like us to call him/her? Mr. or Ms.?:')

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Enter Age")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Enter spy rating")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print colored('Congratulation! Your friend has been added!', 'blue', 'on_grey')
    else:
        print colored('OOPS! Unable to add spy with the details you provided', 'red', 'on_white')

    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1,
                                                                friend.salutation,
                                                                friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose a friend of your choice")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()
    original_image = raw_input("Enter image name with it's extension")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready and sent to your spy friend :D"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("Enter the file name")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "Secret message has been saved! :D"


def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print colored("[%s]:", "blue") % (chat.time.strftime("%d,%B,%Y")), colored("You said", "red")
            print chat.message
        else:
            print colored("[%s]:", "blue") % (chat.time.strftime("%d,%B,%Y")),\
                  colored(friends[read_for].name + "said", "red")
            print chat.message


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    if int(12) < spy.age < int(60):
        print "Authentication complete. Welcome to spychat " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Glad to have you with us."

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n " \
                           "1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n " \
                           "4. Read a secret message \n " \
                           "5. Read Chats from a user \n " \
                           "6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy on spychat. ' \
              'Come to us in a few years to be a part of spychat. '

if existing.upper() == "Y":
    start_chat(spy)
else:
    spy = Spy('', '', 0, 0.0, '')

    spy.name = raw_input("Welcome to spy chat, enter your spy name: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("What should I call you? Mr. or Ms.?:")

        spy.age = raw_input("Please tell us your age")
        spy.age = int(spy.age)

        spy.rating = raw_input("Tell us your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Enter a valid spy name to continue using our app'
