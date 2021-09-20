from enum import Enum

class Commands(Enum):
    GO = 1
    STOP = 2
    
commands = {}
commands[Commands.GO] = "GO"
commands[Commands.STOP] = "STOP"

class Responses(Enum):
    GREETING = 1
    SELECT_TIME = 2
    CONFUSED=3
    WAIT_COUNTING=4
    START_COUNTING=5
    TIME_UP=6

responses={}
responses[Responses.GREETING]="Hello boss. Welcome to the Count Down feature."
responses[Responses.SELECT_TIME]="Please enter the count down time."
responses[Responses.CONFUSED]="Sorry boss. I don't understand. Please say that again."
responses[Responses.WAIT_COUNTING]="Start in..."
responses[Responses.START_COUNTING]="Let's go!!!"
responses[Responses.TIME_UP]="Time's up!!!"

