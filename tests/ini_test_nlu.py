# Imports
#-----------
# rasa nlu
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


# loading the interpreter 
interpreter = Interpreter.load('/home/tcs/chatbot_project_phase_1/models/nlu/default/chat')
print("Done Loading Interpreter")
# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))

# asking question
ask_question("Hi")

ask_question("i am unable to apply leave")

ask_question("How mad days in January")


ask_question("bye")


print("end")
