# -*- coding: utf-8 -*-
"""Convolucional Gato Cachorro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AhvcXCvgpleWjX73STdbOfQV29oCDerN

Olá,

Na aula anterior utilizamos as imagens do Homer e Bart para classificação de imagens. O objetivo desta tarefa é utilizar o mesmo código fonte, porém, para classificar imagens de gatos e cachorros. Você pode fazer o download das imagens nos materiais deste curso e testar outros parâmetros para a rede neural

Bom trabalho!

# Rede neural convolucional - gatos e cachorros

## Importação das bibliotecas
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import zipfile
tf.__version__

"""## Carregamento das imagens"""

from google.colab import drive
drive.mount('/content/drive')

path = "/content/drive/My Drive/Cursos - recursos/dataset_gato_cachorro.zip"
zip_object = zipfile.ZipFile(file=path, mode="r")
zip_object.extractall("./")
zip_object.close()

tf.keras.preprocessing.image.load_img(r'/content/dataset/training_set/gato/cat.1.jpg')

tf.keras.preprocessing.image.load_img(r'/content/dataset/training_set/cachorro/dog.1.jpg')

"""## Construção das bases de treinamento e teste"""

gerador_treinamento = ImageDataGenerator(rescale = 1./255,
                                         rotation_range = 7,
                                         horizontal_flip = True,
                                         shear_range = 0.2,
                                         height_shift_range = 0.07,
                                         zoom_range = 0.2)

base_treinamento = gerador_treinamento.flow_from_directory('/content/dataset/training_set',
                                                           target_size = (64, 64),
                                                           batch_size = 32,
                                                           class_mode = 'binary')

gerador_teste = ImageDataGenerator(rescale = 1./255)

base_teste = gerador_teste.flow_from_directory('/content/dataset/test_set',
                                               target_size = (64, 64),
                                               batch_size = 32,
                                               class_mode = 'binary',
                                               shuffle=False)

"""## Construção e treinamento da rede neural"""

classificador = Sequential()
classificador.add(Conv2D(32, (3,3), input_shape = (64, 64, 3), activation = 'relu'))
classificador.add(MaxPooling2D(pool_size = (2,2)))

classificador.add(Conv2D(32, (3,3), activation = 'relu'))
classificador.add(MaxPooling2D(pool_size = (2,2)))

classificador.add(Flatten())

classificador.add(Dense(units = 128, activation = 'relu'))
classificador.add(Dense(units = 128, activation = 'relu'))
classificador.add(Dense(units = 1, activation = 'sigmoid'))

classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                      metrics = ['accuracy'])

classificador.fit_generator(base_treinamento, epochs = 10, validation_data=base_teste)

"""## Avaliação da rede neural"""

previsoes = classificador.predict(base_teste)

previsoes

previsoes = (previsoes > 0.5)
previsoes

base_teste.class_indices

base_teste.classes

from sklearn.metrics import accuracy_score
accuracy_score(previsoes, base_teste.classes)

from sklearn.metrics import accuracy_score
accuracy_score(previsoes, base_teste.classes)