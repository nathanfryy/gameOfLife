"""
Adrianna Rodencal
Programming 2
First Started: 2/6/2020
Last Updated: 2/21/2020
"""

from cell import Cell
from world import World
from time import sleep
import toolbox

class Life(object):

    feedbackSets = {'new-worlds': {'command': 'New Worlds Menu'},
                    'new-world': {'command': 'Random World Created'},
                    'long-l': {'command': 'Long-l World Created'},
                    'acorn': {'command': 'Acorn World Created'},
                    'home': {'command': 'Main Menu'},
                    'world-editor': {'command': 'World Editor Menu'},
                    'world-size': {'command': 'Edit Dimensions'},
                    'fill-size': {'command': 'Change Fill Percent'},
                    'delay': {'command': 'Generation Delay'},
                    'change-display': {'command': 'Cell Characters Changed'},
                    'next-generation': {'command': 'Simulation Runthrough'},
                    'skip-generation': {'command': 'End of Simulation'},
                    'generations': {'command': 'Generation Menu'},
                    'help': {'command': 'Instructions'},
                    'quit': {'command': 'End of Game'},
                    'save': {'command': 'Current World Saved'} }

    feedbackSet = 'home'

    command = feedbackSets[feedbackSet]['command']

    @classmethod
    def set_command(cls, feedbackSet):
        """
        Print info at the end of the menus telling
        the user what just happened
        :param feedbackSet: What command was just run
        :return: none
        """
        legalValues = cls.feedbackSets.keys()
        if feedbackSet in legalValues:
            cls.feedbackSet = feedbackSet
            cls.command = cls.feedbackSets[feedbackSet]['command']
        else:
            raise ValueError(f'DisplaySet must be in {legalValues}.')

    def __init__(self):
        # self.__rows = row
        # self.__columns = column
        self.__currentWorld = World(20, 20)
        self.__currentPercent = 50
        self.__delay = .5
        self.__menu = 'main'

    def main(self):
        command = 'help'
        parameter = None
        while command != 'quit':
            if command == 'help':
                self.help()
            elif command == 'next-generation':
                self.advance(parameter)
            elif command == 'skip-generation':
                self.skip_advance(parameter)
            elif command == 'new-world':
                self.new_world()
            elif command == 'fill-size':
                self.fill_size(parameter)
            elif command == 'delay':
                self.generation_delay(parameter)
            elif command == 'world-size':
                self.world_size(parameter)
            elif command == 'change-display':
                self.change_display(parameter)
            elif command == 'long-l':
                self.long_l()
            elif command == 'acorn':
                self.acorn()
            elif command == 'save':
                self.save_world(myPath = './worlds/')
            self.show_menu()
            self.set_command('home')
            command, parameter = self.get_command()

    def help(self):
        """
        Print information when requested then print a new world.
        :param: none
        :return: none
        """
        print('''
        ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪WELCOME₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪
        Do you want to play a game of life?
        Sit back and watch the world you created interact with each other,
        living and dying over and over again. In this simulation you will
        be allowed to select the size of the world as well as the percent
        of cells that are living.
        ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪
        Commands:
        New World - this will create a new randomized world. If World Size
            and Fill Size are not selected it will print a default world of 10x10
            and 50% fill size.
        World Size - this will ask you how big you would like your world to 
            be. And then print a new world with that size.
        Fill Size - this will ask you what percent of the world you would
            like living.
        Next Generation or <ENTER> - this will ask you how many "generations" 
            would you like to go through then will print them out for you.
        Help or ? - this will reprint these instructions in case you forget
        Quit - this will stop the entire program.
        ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪''')
        input(' Press <ENTER> when ready to see a world example...')
        self.new_world()

    def show_menu(self):
        """
        Show main menu for the user to chose from
        :param: none
        :return: none
        """
        if self.__menu == 'main':
            print(f'''
[N]ew Worlds    World [E]ditor    [G]enerations    [H]elp   [Q]uit    Sa[V]e    [{Life.command}]''')
        if self.__menu == 'worlds':
            print(f'''
New [W]orld    [L]ong l    [A]corn    H[O]me    [{Life.command}]''')
        if self.__menu == 'editor':
                print(f'''
World [S]ize    [F]ill Size    [D]elay]    [C]hange Display    H[O]me    [{Life.command}]''')
        if self.__menu == 'generations':
                print(f'''
Ne[X]t Generation   S[K]ip Generations    H[O]me    [{Life.command}]''')

    def get_command(self):
        """
        Takes userInput and returns it with any parameters
        :param: none
        :return: command that was chosen and the parameters of that commmand
        """
        commands = {'n': 'new-worlds',
                    'e': 'world-editor',
                    'g': 'generations',
                    'o': 'home',
                    'w': 'new-world',
                    's': 'world-size',
                    'f': 'fill-size',
                    't': 'next-generation',
                    'v': 'save',
                    'l': 'long-l',
                    'a': 'acorn',
                    'k': 'skip-generation',
                    'c': 'change-display',
                    'd': 'delay',
                    'h': 'help',
                    '?': 'help',
                    'q': 'quit',
                    '': 'next-generation'}

        validCommands = commands.keys()

        userInput = 'xxx'
        parameter = None
        while userInput[0].lower() not in validCommands:
            self.__menu = 'main'
            userInput = input('Command: ')
            if userInput == '':
                userInput = 'w'
                parameter = 1
        command = commands[userInput[0].lower()]
        self.set_command(command)
        if userInput[0].lower() in ('n'):
            self.__menu = 'worlds'
        if userInput[0].lower() in ('e'):
            self.__menu = 'editor'
        if userInput[0].lower() in ('g'):
            self.__menu = 'generations'
        if len(userInput) > 1:
            parameter = userInput[1:].strip()
        return command, parameter

    def world_size(self, parameter):
        """
        Allow user to change the current world size
        :param parameter: what dimensions did the user give
        :return: none
        """
        row = int(input('How many rows(vertical) would you like? '))
        column = int(input('How many columns(horizontal) would you like? '))
        self.__currentWorld = World(row, column)
        self.__currentWorld.randomize(self.__currentPercent)
        print(self.__currentWorld)

    def new_world(self):
        """
        Print a new world using the current dimensions
        :param: none
        :return: none
        """
        print(f'››››››››››››››››››››››››››››››››››››››››')
        self.random()
        print(f'‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹')

    def fill_size(self, parameter):
        """
        Allow user to change the current fill percent of the world
        :param parameter:
        :return: none
        """
        prompt = 'What percent of cells should be alive? '
        percent = toolbox.get_integer_between(1, 100, prompt)
        self.__currentPercent = percent

    def long_l(self):
        """
        Print out a new blank world with only a l alive
        :param: none
        :return: none
        """
        rows = self.__currentWorld.get_rows()
        columns = self.__currentWorld.get_columns()
        self.__currentWorld = World(rows, columns)

        middleRow = int(rows / 2)
        middleColumn = int(columns / 2)

        self.__currentWorld.set_cell(middleRow - 2, middleColumn, True)
        self.__currentWorld.set_cell(middleRow - 1, middleColumn, True)
        self.__currentWorld.set_cell(middleRow - 0, middleColumn, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 1, True)
        print(self.__currentWorld, end='')

    def acorn(self):
        """
        Print out a new blank world for the "acorn"
        :param: none
        :return: none
        """
        rows = self.__currentWorld.get_rows()
        columns = self.__currentWorld.get_columns()
        self.__currentWorld = World(rows, columns)

        middleRow = int(rows / 2)
        middleColumn = int(columns / 2)

        self.__currentWorld.set_cell(middleRow - 1, middleColumn - 2, True)
        self.__currentWorld.set_cell(middleRow - 0, middleColumn - 0, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn - 3, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn - 2, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 1, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 2, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 3, True)
        print(self.__currentWorld, end='')

    def random(self):
        """
        Print out a random world with current dimensions
        and current fill percents
        :param: none
        :return: none
        """
        self.__currentWorld.randomize(self.__currentPercent)
        print(self.__currentWorld)

    def advance(self, parameter):
        """
        Ask user how many times they would like to run though generations
       :param parameter:
        :return: none
        """
        lifeTime = toolbox.get_integer('How many generations would you like to go through? ')
        life = 1
        while life <= lifeTime:
            self.__currentWorld.next_generation()
            string = f'››››››››››››››››››››››››››››››››››››››››\n'
            string += f'{self.__currentWorld}\n'
            string += f'{self.status_bar(life)}\n'
            string += f'‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\n'
            print(string)
            sleep(self.__delay)
            life += 1

    def generation_delay(self, parameter):
        """
        Set the amount of "delay" between each  shown generation
        :param parameter:
        :return: none
        """
        delay = int(input('How many seconds of delay would you like between generations? '))
        self.set_delay(delay)

    def skip_advance(self, parameter):
        """
        Run generations but only show the last one
        :param parameter:
        :return: none
        """
        lifeTime = toolbox.get_integer('How many generations would you like to go through? ')
        life = 1
        while life <= lifeTime:
            if life == lifeTime:
                self.__currentWorld.next_generation()
                string = f'››››››››››››››››››››››››››››››››››››››››\n'
                string += f'{self.__currentWorld}\n'
                string += f'{self.status_bar(life)}\n'
                string += f'‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\n'
                print(string)
                life += 1
            else:
                self.__currentWorld.next_generation()
                life += 1

    def change_display(self, parameter):
        """
        Print possible display changes for the user.
        :param parameter:
        :return: none
        """
        if toolbox.is_integer(parameter) and \
                1 <= int(parameter) <= len(Cell.displaySets.keys()):
            setNumber = int(parameter)
        else:
            print('**************************************')
            for number, set in enumerate(Cell.displaySets):
                liveChar = Cell.displaySets[set]['liveChar']
                deadChar = Cell.displaySets[set]['deadChar']
                print(f'{number+1}: living cells: {liveChar} dead cells: {deadChar}')
            print(f'{number+1}: Choose your own characters! ')
            print('**************************************')
            prompt = 'What character set would you like to use?'
            setNumber = toolbox.get_integer_between(1, number + 1, prompt)
        setString = list(Cell.displaySets.keys+())[setNumber - 1]
        Cell.set_display(setString)
        print(self.__currentWorld, end='')

    def status_bar(self, life):
        """
        Set the amount of "delay" between each  shown generation
        :param life: what generation the simulation is on
        :return: string
        """
        rows = self.__currentWorld.get_rows()
        columns = self.__currentWorld.get_columns()
        percentAlive = (self.__currentWorld.percent_alive())
        string = 'Status:   '
        string += f'Generation ~ {life}   '
        string += f'Dimensions ~ [{rows}x{columns}]   '
        string += f'Alive ~  {percentAlive}   '
        string += f'Speed/Delay ~ {self.__delay}'
        return string

    def save_world(self, myPath):
        """
        Allow user to save current world
        :param myPath: directory to folder all saved worlds
        are in
        :return: none
        """
        toolbox.get_boolean('Would you like to save current world? ')
        if True:
            filename = input('What would you like to name your file? ')
            if filename[-5:] != '.life':
                filename = filename + '.life'
                print(filename)
            currentDisplaySet = Cell.displaySet
            Cell.set_display('basic')
            self.__currentWorld.write_file(filename)

    def open_file(self):
        """
        Ask user what file they would like open and
        print it as new world
        :param: none
        :return: none
        """
        filename = input('Which file would you like to open? ')

    def set_delay(self, delay):
        self.__delay = delay

    def get_delay(self):
        return self.__delay

if __name__ == '__main__':
    gameOfLife = Life()
    gameOfLife.main()