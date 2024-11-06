import tensorflow as tf
from tensorflow.keras import layers, losses
from tensorflow.keras.models import Model
from sklearn.preprocessing import StandardScaler
import numpy as np
import etc.helper as helper
import scipy.signal as sig
from matplotlib import pyplot as plt
from IPython import display
import soundfile as sf

SPEC = 100

#Autoencoder model definition
class Autoencoder(Model):
    def __init__(self, latent_dim, train_size=0.7, test_size=0.3, epochs=100, random_state=5):
        super(Autoencoder, self).__init__()
        self.model_name = "custom_spectral_model_test"

        self.latent_dim = latent_dim
        self.in_shape = ((0,0,0))
        self.out_shape = ((0,0,0))

        self.train_size = train_size
        self.test_size = test_size
        self.epochs = epochs
        self.random_state = random_state
        

    def call(self, x):
        print(f"Input shape: {x.shape}")
    
        # Encoding the real part
        encoded_real = self.encoder_real(x)
        print(f"Encoded real shape: {encoded_real.shape}")
        
        # Encoding the imaginary part
        encoded_imag = self.encoder_imag(x)
        print(f"Encoded imaginary shape: {encoded_imag.shape}")
        
        # Decoding the real part
        decoded_real = self.decoder_real(encoded_real)
        print(f"Decoded real shape: {decoded_real.shape}")
        
        # Decoding the imaginary part
        decoded_imag = self.decoder_imag(encoded_imag)
        print(f"Decoded imaginary shape: {decoded_imag.shape}")
        
        return [decoded_real, decoded_imag]
    
    def predict(self, data, labels):
        reconstructions = self(data)
        loss = losses.mse(reconstructions, labels)
        return reconstructions, loss
    
    def plot_losses(self):
        test_ind = 0
        plt.figure()
        plt.title(f"Model Loss for Epochs = {self.epochs} and Latent Space = {self.latent_dim}")
        plt.plot(self.history.history["loss"], label="Training Loss")
        plt.plot(self.history.history["val_loss"], label="Validation Loss")
        plt.legend()
        plt.savefig(f"figs/{self.model_name}/Model_{self.model_name}_{self.latent_dim}_Loss.png", dpi=300)

        X_test = np.array(self.X_test)
        Y_test = np.array(self.Y_test)
        model_Y1 = np.array(self(self.X_test[test_ind].reshape(1, self.X_test[0].shape[0], self.X_test[0].shape[1]))).reshape(2, self.Y_test.shape[1], self.Y_test.shape[2])
        model_Y = np.abs(model_Y1[0] + (1.j * model_Y1[1]))
        #print("model_y", (model_Y1[0] + (1.j * model_Y1[1])).shape)
        modelYwave = self.spectro.istft(model_Y1[0] + (1.j * model_Y1[1]))
        true_Y = np.abs(Y_test[test_ind])
        true_wave = self.spectro.istft(Y_test[test_ind])

        display_scale = StandardScaler().fit(true_Y)
        display_Y = display_scale.transform(model_Y)
        #true_Y = display_scale.transform(true_Y)
        display_Y = np.abs(model_Y)
        _, loss = self.predict(self.X_test, [np.real(self.Y_test), np.imag(self.Y_test)])

        plt.plot(true_wave)
        plt.savefig(f"figs/{self.model_name}/Model_{self.model_name}_{self.latent_dim}_realwave.png")
        
        sf.write(f"figs/{self.model_name}/Model_{self.model_name}_{self.latent_dim}_og_audio.flac", true_wave, 1600)

        plt.plot(modelYwave)
        plt.savefig(f"figs/{self.model_name}/Model_{self.model_name}_{self.latent_dim}_wave.png")

        sf.write(f"figs/{self.model_name}/Model_{self.model_name}_output.flac", modelYwave, 1600)

        
        fig, axs = plt.subplots(2,1)
        axs[0].imshow(display_Y, origin='lower', aspect='auto',
            extent=self.spectro.extent(self.out_shape[0]), cmap='inferno')
        axs[0].set_title(f"Reconstructed Audio Spectrogram (Latent Space = {self.latent_dim})")
        
        axs[1].imshow(true_Y, origin='lower', aspect='auto',
            extent=self.spectro.extent(self.out_shape[0]), cmap='inferno')		
        axs[1].set_title("True Audio Spectrogram")
       
        fig.legend()
        
        plt.savefig(f"figs/{self.model_name}/Model_{self.model_name}_{self.latent_dim}_Recon.png", dpi=300)

        #print("display_Y: \n", display_Y)


        """ # Convert the waveform to a spectrogram via a STFT.
        spectrogram = tf.signal.stft(
            true_Y, frame_length=255, frame_step=128)
        # Obtain the magnitude of the STFT.
        spectrogram = tf.abs(spectrogram)
        # Add a `channels` dimension, so that the spectrogram can be used
        # as image-like input data with convolution layers (which expect
        # shape (`batch_size`, `height`, `width`, `channels`).
        spectrogram = spectrogram[..., tf.newaxis]
        #print('Spectrogram shape:', spectrogram.shape)"""
        
        self.test_loss =  np.average(loss)
        print(loss)
        print(self.test_loss)


    def process_data(self, eeg, audio, sample_rate, events, event_dict=None):
        '''process the data before running the model. Requires eeg, audio, and the
        sample_rate to downsample the audio to.'''
        
        #calculate spectrogram of average of the two audio channels
        audio = np.atleast_2d(np.average(audio.T, axis=0))
        
        #downsample audio
        
        audio = sig.resample(audio, eeg.shape[1], axis=1)
        
        events = [18194, 21455, 24784, 27956, 31145, 33639, 37277, 40288, 44117, 46688, 49050, 51076, 53301, 56163, 59405, 63455, 66834, 79477, 83823, 87931,
            91525, 95086, 99359, 102772, 106184, 109425, 111685, 114611, 118441, 122981, 126463, 132195, 144537, 148171, 152369, 156285, 160349,
            162746, 165174, 167852, 169994, 173607, 176532, 180735, 182988, 185354, 188076, 191113, 202124, 205760, 207668, 211343, 214218, 217331, 219557,
            223642, 226545, 229466, 233711, 237012, 240139, 251742, 254136, 257780, 260465, 263313, 266339, 269752, 273907, 276216, 279055, 281751, 284651,
            289103, 300750, 303385, 305890, 308957, 311250, 313988, 316042, 319696, 323227, 326030, 328762, 331563, 335040, 337760, 343389, 355806, 358673,
            362703, 365792, 368546, 371806, 375306, 378165, 382086, 383906, 386516, 390838, 394648, 398692, 401453, 407008, 417847, 
            421406, 424928, 428115, 430842, 433495, 436684, 439429, 442036, 445459, 447736, 450474, 453479, 457217, 459527, 461458]

        # events = events[1:, 0]
        #split audio and eeg into event segments
        split_eeg = helper.split_events(eeg, events[1:-1], sample_rate)
        split_audio = helper.split_events(audio, events[1:-1], sample_rate)

        #split data into train, test, validation
        self.X_train, self.Y_train, self.X_test, self.Y_test, self.X_val, self.Y_val = \
        helper.train_test_val_split(split_eeg, split_audio, self.train_size, \
                            self.test_size, self.random_state)

        self.Y_train = self.Y_train[:,0,:]
        self.Y_test = self.Y_test[:,0,:]
        self.Y_val = self.Y_val[:,0,:]
        
        #SPECTROGRAM ACTUALLY GETS CALC'D HERE
        
        window = sig.windows.gaussian(30, std=5, sym=True)
        spectro = sig.ShortTimeFFT(win=window, hop=19, fs=sample_rate, scale_to='magnitude')
        self.Y_train = spectro.stft(self.Y_train)
        
        self.Y_test = spectro.stft(self.Y_test)
        
        self.Y_val = spectro.stft(self.Y_val)

        #Need this for applying inverse FFT later
        self.spectro = spectro


    def train(self):
        self.X_train = self.X_train.reshape(self.X_train.shape[0], self.X_train.shape[1], self.X_train.shape[2], 1)
        self.in_shape = self.X_train.shape[1:]
        self.out_shape = self.Y_train.shape[1:]

        self.Y_train_real = np.real(self.Y_train)
        self.Y_train_imag = np.imag(self.Y_train)

        self.Y_val_real = np.real(self.Y_val)
        self.Y_val_imag = np.imag(self.Y_val)

        self.encoder_real = tf.keras.Sequential([
            layers.Input(shape=(31, 87, 1)),
            layers.Conv2D(16, (3, 3), strides=2, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.25),
            layers.Conv2D(8, (3, 3), strides=2, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.25),
            layers.Conv2D(4, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Dropout(0.25),
            layers.Conv2D(2, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Dropout(0.25),
            layers.Flatten(),
            layers.Dense(self.latent_dim),
        ])

        self.encoder_imag = tf.keras.Sequential([
            layers.Input(shape=(31, 87, 1)),
            layers.Conv2D(16, (3, 3), strides=2, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.25),
            layers.Conv2D(8, (3, 3), strides=2, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.25),
            layers.Conv2D(4, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Dropout(0.25),
            layers.Conv2D(2, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Dropout(0.25),
            layers.Flatten(),
            layers.Dense(self.latent_dim),
        ])

        self.decoder_real = tf.keras.Sequential([
            # Start with a Dense layer to expand the latent vector
            layers.Dense(16 * 6, activation='relu'),  # Ensure this is large enough to reshape to (16, 6)
            layers.Reshape((16, 6, 1)),  # Reshape to a format that can be processed by Conv2DTranspose
            
            # Apply Conv2DTranspose layers to upsample to the desired dimensions
            layers.Conv2DTranspose(16, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Conv2DTranspose(8, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Conv2DTranspose(4, (3, 3), strides=2, padding='same', activation='relu'),
            
            # Final Conv2DTranspose to match the desired output size
            layers.Conv2DTranspose(1, (3, 3), strides=2, padding='same', activation='sigmoid'),
            
            # Reshape to the final output shape
            layers.Reshape((16, 6))  # This ensures the output matches the target shape

        ])

        self.decoder_imag = tf.keras.Sequential([
            layers.Dense(16 * 6, activation='relu'),
            layers.Reshape((16, 6, 1)),
            layers.Conv2DTranspose(16, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Conv2DTranspose(8, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Conv2DTranspose(4, (3, 3), strides=2, padding='same', activation='relu'),
            layers.Conv2DTranspose(1, (3, 3), strides=2, padding='same', activation='sigmoid'),
            layers.Reshape((16, 6)) 
        ])

        self.compile(optimizer="Adam", loss=losses.MeanSquaredError())


        self.history = self.fit(self.X_train, [self.Y_train_real, self.Y_train_imag],
                epochs=self.epochs,
                validation_data=(self.X_val, [self.Y_val_real, self.Y_val_imag]),
                )

#python testing_script.py my_model_spec_test 100