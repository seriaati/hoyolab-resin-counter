import genshinstats as gs
gs.set_cookie(ltuid=7368957, ltoken="X5VJAbNxdKpMp96s7VGpyIBhSnEJr556d5fFMcT5")

uid = 901211014
notes = gs.get_notes(uid)
time = (notes['max_resin']-notes['resin'])*8/60
hours = int(time)
minutes = (time*60) % 60.
print(f"User UID: {uid}")
print(f"Current resin: {notes['resin']}/{notes['max_resin']}")
print(f"Resin full in %d hours %02d minutes" % (hours, minutes))
print(f"Current realm currency: {notes['realm_currency']}/{notes['max_realm_currency']}")
print(f"Expeditions completed: {len(notes['expeditions'])}/{notes['max_expeditions']}")
