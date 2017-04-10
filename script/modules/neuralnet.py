#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
# from keras.layers import Dropout
# from keras.optimizers import SGD
from keras.optimizers import RMSprop
from keras.models import model_from_json
from keras.regularizers import l2
from keras.regularizers import l1
from keras.objectives import mean_squared_error
from keras.callbacks import EarlyStopping
import numpy as np
import matplotlib.pyplot as plt
from . import errors
from keras import backend as K
from keras import metrics
from keras import initializers


class NeuralNet(object):

    """Docstring for NeuralNet. """

    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.history = None
        self.model = None
        self.input_dim = None
        self.output_dim = None
        self.size = None

    def save(self, model_path):
        self.model.save(model_path)

    def set_dataset(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        self.input_dim = x_train.shape[1]
        self.output_dim = y_train.shape[1]
        self.size = y_train.shape[0]
        print(x_train.shape)
        print(y_train.shape)

    def restore_model(self, model_path, weight_path):
        self.model = model_from_json(model_path)
        self.model.load_weights(weight_path)

    def build_model(self,
                    layer_num=3,
                    init_weight=0,
                    l=0.01,
                    sammary=False,
                    **kwargs
                    ):

        self.model = Sequential()
        self.model.add(Dense(int(self.input_dim),
                             kernel_initializer=initializers.Constant(
                                 value=init_weight),
                             W_regularizer=l1(l),
                             input_shape=(self.input_dim,)))

        self.model.add(Activation("tanh"))

        for i in range(layer_num - 1):
            self.model.add(Dense(self.input_dim))
            self.model.add(Activation("tanh"))

        self.model.add(Dense(int(self.output_dim)))
        self.model.add(Activation("softmax"))

        if sammary is True:
            self.model.summary()

        # sgd = SGD(lr=0.005, decay=1e-6, momentum=0.9, nesterov=True)
        opt = RMSprop(lr=0.0005, rho=0.9, epsilon=1e-08, decay=0.0)

        self.model.compile(loss="categorical_crossentropy", optimizer=opt,
                           metrics=['categorical_accuracy'])

    def fit(self, batch_size):
        self.early_stopping = EarlyStopping(patience=2, verbose=0)
        self.history = self.model.fit(self.x_train,
                                      self.y_train,
                                      nb_epoch=2000,
                                      batch_size=batch_size,
                                      validation_split=0.3,
                                      verbose=0,
                                      callbacks=[self.early_stopping])
        socre = self.history.history['val_categorical_accuracy'][-1]
        print('accuracy is {0}'.format(socre))
        return socre

    def show_graph(self):
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.show()

    def save_graph(self, path):
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.savefig(path)
        plt.gcf().clear()

    def predict(self, x_train):
        return self.model.predict(x_train)

    def validate(self, x_train, y_train):
        preds = self.predict(x_train)
        answers = y_train

        for ans, pred in zip(answers, preds):
            row = "ans: \t{0: 3.3f}, predict: \t{1: 3.3f}, diff:\t{2: 3.3f}"
            print(row.format(ans[0],
                             pred[0],
                             pred[0] - ans[0]))

        ans_t = answers.reshape(answers.shape[1], answers.shape[0])
        pred_t = preds.reshape(preds.shape[1], preds.shape[0])

        mse = K.eval(mean_squared_error(ans_t, pred_t))
        print("mean squared error is {0}".format(mse))

    def validate_category(self, x_train, y_train):
        preds = self.predict(x_train)
        result = [np.equal(np.argmax(pred), np.argmax(ans))
                  for pred, ans in zip(preds, y_train)]
        for ans, pred in zip(y_train, preds):
            print(np.argmax(ans), np.argmax(pred))
        print(np.mean(result))
