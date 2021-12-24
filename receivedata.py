
from pylsl import StreamInlet, resolve_stream
import matplotlib.pyplot as plt

def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('name', 'openvibeSignal')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        print(timestamp, *sample,sep=',')





if __name__ == '__main__':
    main()