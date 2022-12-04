import serial
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID = "5820bb90-c130-4b64-9624-2f8a7893fe82_amzn_1"
CLIENT_ID = "270c19aa1ebf4de3b7447cbce0b0bd55"
CLIENT_SECRET = "e8db9a0a5b1a4190a21b670993e1370d"

ser = serial.Serial()
ser.baudrate = 9600


while True:


        ser.port = '/dev/cu.usbmodem142301'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))

        ser.open()
        while True:
            print("Waiting for record scan...")
            id = ser.readline()
            id = str(id)
            id = id.replace(" ", "")
            print("Card Value is:", id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

            if "10221123203" in id:

                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:13T8SvWHczyBPzOemKtEe7'])
                sleep(2)

            elif '8017604012' in id:

                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:6jdOi5U5LBzQrc4c1VT983'])
                sleep(2)
