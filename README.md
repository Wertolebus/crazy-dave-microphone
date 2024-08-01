# Transform yourself into Crazy Dave!
Simple script to be a Crazy Dave from Plants vs. Zombies

# How to use
**IMPORTANT: Need to install VB-CABLE Virtual Audio Device.**

**Steps**
1. Install VB-CABLE Virtual Audio Device
2. run
```python
pip install numpy sounddevice soundfile
```
3. run in python
```python
import sounddevice as sd
print(sd.query_devices())
```
4. find your microphone and virtual microphone indexes
5. change in main.py `MIC_DEVICE_INDEX` and `VIRTUAL_MIC_DEVICE_INDEX` with your indexes
6. change threshold (if necessary)
7. run script!

# Important
For better experience with discord, turn off echo- and noise- cancellation.
