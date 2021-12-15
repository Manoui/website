import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding, LSTM, Dropout
#from keras.utils import to_categorical
from random import randint
import re

# Imports you may need
import seaborn as sns
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import numpy as np
import keras
# importing the module
import ast


import matplotlib.pyplot as plt
from PIL import Image
import random
    
    
def function_test(): 
    
    # reading the data from the file
    with open('dict2.txt') as f:
        data = f.read()

    # reconstructing the data as a dictionary
    word_2_index = ast.literal_eval(data)


    # reading the data from the file
    with open('words2.txt') as f:
        data = f.read()

    # reconstructing the data as a dictionary
    data_text_words = ast.literal_eval(data)

    new_model = keras.models.load_model('text_generation_model_final2')

    input_sequence = []
    output_words = []
    input_seq_length = 4
    n_words = 12600
    vocab_size=2978



    for i in range(0, n_words - input_seq_length , 1):
        in_seq = data_text_words[i:i + input_seq_length]
        out_seq = data_text_words[i + input_seq_length]
        input_sequence.append([word_2_index[word] for word in in_seq])
        output_words.append(word_2_index[out_seq])

    random_seq_index = np.random.randint(0, len(input_sequence)-1)
    random_seq = input_sequence[random_seq_index]

    index_2_word = dict(map(reversed, word_2_index.items()))

    word_sequence = [index_2_word[value] for value in random_seq]

    #print(' '.join(word_sequence))

    for i in range(9):
        int_sample = np.reshape(random_seq, (1, len(random_seq), 1))
        int_sample = int_sample / float(vocab_size)

        predicted_word_index = new_model.predict(int_sample, verbose=0)

        predicted_word_id = np.argmax(predicted_word_index)
        seq_in = [index_2_word[index] for index in random_seq]

        word_sequence.append(index_2_word[ predicted_word_id])

        random_seq.append(predicted_word_id)
        random_seq = random_seq[1:len(random_seq)]

    final_output = ""
    for word in word_sequence:
        final_output = final_output + " " + word


    #print(final_output[1].upper()+final_output[2:]+'.')
    return(final_output)
    