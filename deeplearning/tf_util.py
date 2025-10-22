import numpy as np
import tensorflow as tf
from keras.callbacks import Callback

class EpochTiming(Callback):
    """Callback para medir el tiempo de cada época durante el entrenamiento del modelo.
    Esta clase extiende la clase Callback de Keras para medir el tiempo que toma cada época
    durante el entrenamiento. También calcula y almacena los tiempos promedio, mínimo y máximo de las épocas.
    """

    def on_train_begin(self, logs=None):
        # Llamado al comienzo del entrenamiento.
        self._epochs_time = np.array([])  # Arreglo para almacenar el tiempo de cada época

    def on_train_end(self, logs=None):
        # Llamado al final del entrenamiento.
        # Calcula estadísticas (tiempos total, promedio, mínimo y máximo) basadas en los tiempos de las épocas.

        self.epochs = len(self._epochs_time)
        self.avg_epoch_time = self._epochs_time.mean()
        self.min_epoch_time = self._epochs_time.min()
        self.max_epoch_time = self._epochs_time.max()
        self.total_time = self._epochs_time.sum()

    def on_epoch_begin(self, epoch, logs=None):
        # Llamado al comienzo de cada época.        
        # Registra el tiempo de inicio de la época.

        self._start_time = tf.timestamp()

    def on_epoch_end(self, epoch, logs=None):
        # Llamado al final de cada época. 
        # Calcula el tiempo transcurrido durante la época y lo almacena en el arreglo de tiempos de épocas.

        time = tf.timestamp() - self._start_time
        self._epochs_time = np.append(self._epochs_time, time)
    
    # Estos metodos no se usan porque los eventos asociados no se requieren para el objetivo de la clase
    # def on_batch_begin(self, batch, logs=None):

    # def on_batch_end(self, batch, logs=None):

    # def on_test_begin(self, logs=None):

    # def on_test_end(self, logs=None):
