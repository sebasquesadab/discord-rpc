
from pypresence import Presence
import time

#config
state = "yesyesyes"
details = "Uploading Images!"
large_image = "yes"
client_id = "791833473765736508"
large_text = "Free And Open Source"

#button1 config
Buton1Label = "The Github!"
Buton1Url = "https://github.com/3v1"

#button2 config
Buton2Label = "The Github! Again"
Buton2Url = "https://github.com/3v1"

RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(state=state, details=details, large_image=large_image, large_text=large_text, buttons=[{"label": Buton1Label, "url": Buton1Url}, {"label": Buton2Label, "url": Buton2Url}]) # Can specify up to 2 buttons

while 1:
    time.sleep(15) #Can only update presence every 15 seconds
