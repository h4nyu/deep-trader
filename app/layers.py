#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras import backend as K
from keras.engine.topology import Layer


class Split(Layer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, input_shape):
        super().build(input_shape)

    def call(self, x):
        return x

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.output_dim)
