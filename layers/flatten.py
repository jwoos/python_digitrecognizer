from typing import Callable, Tuple

from layers import base
import utils

import numpy as np


class Flatten(base.BaseLayer):
    def __init__(self):
        super().__init__(units=1)

    def initialize(self, input_shape: Tuple[int, int, int]):
        super().initialize(input_shape)

        self.weights = None
        self.biases = None

    def forward(self, data: np.ndarray) -> np.ndarray:
        data = np.copy(data)
        return data.reshape((1,))

    def backward(self, data: np.ndarray, output: np.ndarray, delta: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        delta = np.copy(delta)
        return delta.reshape(input_shape)

    def infer_output_shape(self, input_shape: Tuple[int, int, int]) -> Tuple[int, int]:
        return (1, np.product(input_shape))
