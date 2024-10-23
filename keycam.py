
key_to_cam = {
        "A"  : "11B",
        "Am" : "8A",
        "A#" : "6B",
        "A#m": "3A",
        "Bb" : "6B",
        "Bbm": "3A",
        "B"  : "1B",
        "Bm" : "10A",
        "C"  : "8B",
        "Cm" : "5A",
        "C#" : "3B",
        "C#m": "12A",
        "Db" : "3B",
        "Dbm": "12A",
        "D"  : "10B",
        "Dm" : "7A",
        "D#" : "5B",
        "D#m": "2A",
        "Eb" : "5B",
        "Ebm": "2A",
        "F"  : "7B",
        "Fm" : "4A",
        "F#" : "2B",
        "F#m": "11A",
        "Gb" : "2B",
        "Gbm": "11A",
        "G"  : "9B",
        "Gm" : "6A",
        "G#" : "4B",
        "G#m": "1A",
        "Ab" : "4B",
        "Abm": "1A",
        }

# cam_to_key returns a list because a single
# Camelot scale can have multiple key synonyms.
# For example, 6B can be A# or Bb
cam_to_key = {}
for k, v in key_to_cam.items():
    cam_to_key.setdefault(v, []).append(k)

