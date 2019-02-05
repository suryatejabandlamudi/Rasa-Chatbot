# Imports
#-----------
# rasa core
import logging
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
#  from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
print("Importing Done")


# first we get the nlu interpreter ,then we load the agent
rasaNLU = RasaNLUInterpreter("/home/tcs/chatbot_project_phase_1/models/nlu/default/chat")
agent = Agent.load("/home/tcs/chatbot_project_phase_1/models/dialogue", interpreter= rasaNLU)

print("start")
# asking question
agent.handle_message('hey')
print("end")

