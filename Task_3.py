class MyCustomError(Exception):
    """Клас виключення помилки вводу неправильного коду для відкривання дверей"""

class OpenDoor:
    def open_door(self, code):
        self.enter_code(code)
        print(f'The door is open. Entered code {code} is right')

    def enter_code(self, code):
        if code != 1234:
            raise MyCustomError('Wrong code. The door is closed')
        else:
            print('Come in')

open = OpenDoor()

try:
    open.open_door(12345)
except NameError:
    print('Enter correct 4 numbers')










