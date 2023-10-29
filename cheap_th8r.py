import pyaudio
import sounddevice as sd
import soundfile as sf
from argparse import *
from threading import Thread
import random

program_help = '''
This Python program utilizes the pyaudio, sounddevice, and soundfile libraries to provide audio and video playback with the flexibility to choose from a random selection of audio output devices.
You can control the device you want to use for audio output by specifying device indices.'''
global dev_str
parser = ArgumentParser(description=program_help,formatter_class=RawTextHelpFormatter)
dev_dict = {}


def custom_list(arg):
    return [int(x) for x in arg.split(',')]

def list_devices():
    global dev_str
    dev_str = ''
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    for i in range(0, device_count):
        info = p.get_device_info_by_index(i)
        dev_dict[info["index"]] = info["name"]
        # print("Device {} = {}".format(, ))
        dev_str += f'{info["index"]} : {info["name"]} channels supported : {info["maxOutputChannels"]} with  \n'
    return dev_dict

def audiofunc(song,device_play):
    print(f"Playing {song} on device {dev_dict[device_play]}")
    data1,fs1 = sf.read(song,dtype='float32',channels=2)
    sd.play(data1,fs1,device=device_play)
def audiofunc1(song,device_play):
    data1,fs1 = sf.read(song,dtype='float32')
    sd.play(data1,fs1,device=device_play)
def audiofunc2(song,device_play):
    data1,fs1 = sf.read(song,dtype='float32')
    sd.play(data1,fs1,device=device_play)


def get_random_devices():
    list_devices()
    random_list=[]
    values =''
    for i in range(1,4):
        temp = random.randint(0,len(dev_dict))
        random_list.append(temp)
        values+=f'{temp} : {dev_dict[temp]}\n\t'
    return random_list,values
def main():
    
    type_help='''
        There are two types which is currently supported by this program.... 
        -t song :   for any audio to be played using the set of speakers you selected...
        -t vid  :   for any video to be played using the set of speakers you selected...
    '''
    nums,values= get_random_devices()
    
    device_help =f'''
        All the devices that can act as the output will be shown over here.
        -d {nums} to select the respective devices from the above list of devices '''
    file_help=f'''
        The file that has to be played in multiple devices
        -f filename.mp4
    '''
    parser.add_argument('-t','--type',required=True,default='song',help=type_help)
    parser.add_argument('-f','--file',required=True,help=file_help)
    parser.add_argument('-d','--devices',required=True,help=device_help,type=custom_list)
    # parser.add_argument('-h','--help',help=ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    print(args.type)
    print(args.file)
    print(args.devices)
    print(dev_str)

    threads=[]
    for i in args.devices:
        thread = Thread(target=audiofunc,args=(args.file,i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
if __name__=='__main__':
    main()