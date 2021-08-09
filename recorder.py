from kivy.app import App
from kivy.uix.button import Button

# Requires pyaudio
def record(*arg):
    import pyaudio
    import wave

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


class recordApp(App):
    def build(self):
         btn = Button(text ="Push Me !",
         font_size ="20sp",
         background_color =(1, 1, 1, 1),
         color =(1, 1, 1, 1),
         size =(32, 32),
         size_hint =(.2, .2),
         pos =(300, 250))
      # bind() use to bind the button to function callback
        btn.bind(on_press = self.callback)
        return Button(text="record", on_press=record)

recordApp().run()