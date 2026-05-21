from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.pycaw import AudioUtilities



print("Starting audio monitor...")

# Loads in the default (active) microphone
print("Loading active microphone...")
devices = AudioUtilities.GetMicrophone()

# Activating the interface for the microphone
print("Activating interface...")
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Casting the volume
print("Casting volume...")
volume = cast(interface, POINTER(IAudioEndpointVolume))

def get_mute_state():
    # Get boolean value if microphone is muted
    print("Get mute state...")
    is_mute = volume.GetMute()
    print(f"Mute: {is_mute}")
    return is_mute