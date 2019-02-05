# -*- coding: utf-8 -*-
# Imports
#-----------
# rasa nlu
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
print("a bit more")
from rasa_nlu.model import Metadata, Interpreter
print("importing done")
# Functions
#------------
def train (data, config_file, model_dir):
	#loading training data
    training_data = load_data(data)
	#loading config file
    trainer = Trainer(config.load(config_file))
	#training
    trainer.train(training_data)
	#saving the model
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

# Training
#------------
train('/home/tcs/chatbot_project_phase_1/nlu_train.md', '/home/tcs/chatbot_project_phase_1/nlu_config.yml', '/home/tcs/chatbot_project_phase_1/models/nlu')


print("end")
