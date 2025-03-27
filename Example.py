
from HoymilesHmDtu import HoymilesHmDtu

CSn = 0
CE = 24

hm = HoymilesHmDtu("1141xxxxxxxx", CSn, CE)

hm.InitializeCommunication()
success, info = hm.QueryInverterInfo()

print(f"success: {success}")
HoymilesHmDtu.PrintInverterInfo(info)

