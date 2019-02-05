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

# Function
#------------
def train_dialog(dialog_training_data_file, domain_file, path_to_model = '/home/tcs/chatbot_project_phase_1/models/dialogue'):
    logging.basicConfig(level='INFO')
	# first we will give the domain file, and policy to the agent.
    agent = Agent(domain_file,
              policies=[MemoizationPolicy(max_history=1)])
	# then we will give dialog training data file to it. 
    training_data = agent.load_data(dialog_training_data_file)
	# here we will train the dialogue into the agent using the loaded the training data , define out values to the variables to 		# tweak the training
    agent.train(
        training_data,
        augmentation_factor=50,
        epochs=200,
        batch_size=10,
        validation_split=0.2)
	# then we save the dialogue model
    agent.persist(path_to_model)

# Train
#--------
train_dialog('/home/tcs/chatbot_project_phase_1/stories.md', '/home/tcs/chatbot_project_phase_1/domain.yml')

print("completed")
