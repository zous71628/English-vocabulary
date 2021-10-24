from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


def play_note(note, length, track, base_num=0, deplay=0, velocity=1.0, channel=0, bpm=150):
    meta_time = 60 / bpm * 1000
    major_scale = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(Message('note_on', note=base_note + base_num * 12 + sum(major_scale[0:note]),
                         velocity=round(60 * velocity),
                         time=round(deplay * meta_time), channel=channel))
    track.append(Message('note_off', note=base_note + base_num * 12 + sum(major_scale[0:note]),
                         velocity=round(60 * velocity), time=round(meta_time * length), channel=channel))


def get_chord_arrangement(name):
    chord_dict = {
        "M9": [-12, -5, 0, 8, 12, 15,18],
        "M91":[-24,-17,-12,0,6,12],
        "M92": [-16,-10,0,5,12],
        "M3":[0,4,9,14],

        "MID":[-29, 0 ,12]


    }

    chord = chord_dict[name]

    return chord  # 返回值是一个长度为4的一维数组，每一个值表示这个音符与根音相差的半音数


def add_column_chord(root, name, format, length, track, root_base=0, channel=0):
    root_to_number = {
        'C': 60,
        'D': 62,
        'E': 64,
        'F': 65,
        'G': 67,
        'A': 69,
        'B': 71,
        'C1':72,
        'D1': 74,
        'E1': 76,
        'F1': 77,
        'G1': 79,
        'A1': 81,
        'B1': 83,
        'C2': 84,
        'D2': 86,
        'E2': 88,
        'F2': 89,
        'G2': 91,
        'A2': 93
    }
    root_note = root_to_number[root] + root_base * 12
    chord = get_chord_arrangement(name)
    time = length * 420
    for dis in format:
        note = root_note + chord[dis]
        track.append(Message('note_on', note=note, velocity=56, time=0, channel=channel))
    for dis in format:
        note = root_note + chord[dis]
        if dis == format[0]:
            track.append(Message('note_off', note=note, velocity=56, time=round(time), channel=channel))
        else:
            track.append(Message('note_off', note=note, velocity=56, time=0, channel=channel))


def chord1(track):
    format = [0, 1, 2, 3, 4]
    format0 = [0, 1, 2, 3]
    format1 = [0, 1, 2, 3, 4, 5]
    format3 = [0, 1, 2]

    add_column_chord('D', 'M9', format, 0.75, track)
    add_column_chord('D', 'M9', format, 0.25, track)
    add_column_chord('D', 'M9', format, 0.5, track)
    add_column_chord('C', 'M9', format, 0.5, track)
    add_column_chord('D', 'M9', format, 0.75, track)
    add_column_chord('D', 'M9', format, 0.25, track)
    add_column_chord('D', 'M9', format, 0.5, track)
    add_column_chord('C', 'M9', format, 0.5, track)

    add_column_chord('D', 'M9', format1, 0.75, track)
    add_column_chord('D', 'M9', format, 0.25, track)
    add_column_chord('D', 'M9', format, 0.5, track)
    add_column_chord('C', 'M9', format, 0.5, track)
    add_column_chord('D', 'M91', format1, 1, track)
    add_column_chord('F', 'M3', format0, 1, track)

    add_column_chord('A', 'M92', format, 0.75, track)
    add_column_chord('D', 'M9', format, 0.25, track)
    add_column_chord('D', 'M9', format, 0.5, track)
    add_column_chord('C', 'M9', format, 0.5, track)
    add_column_chord('D', 'M9', format, 0.75, track)
    add_column_chord('D', 'M9', format, 0.25, track)
    add_column_chord('D', 'M9', format, 0.5, track)
    add_column_chord('C', 'M9', format, 0.5, track)

    add_column_chord('D', 'M9', format, 1, track)
    add_column_chord('F', 'M9', format, 1, track)
    add_column_chord('G', 'M9', format, 1, track)
    add_column_chord('A', 'M9', format, 1, track)

    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)

    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('E1', 'MID', format3, 0.25, track)
    add_column_chord('F1', 'MID', format3, 0.25, track)
    add_column_chord('E1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.5, track)
    add_column_chord('C1', 'MID', format3, 0.5, track)

    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)

    add_column_chord('G1', 'MID', format3, 0.5, track)
    add_column_chord('A1', 'MID', format3, 0.5, track)
    add_column_chord('C2', 'MID', format3, 0.5, track)
    add_column_chord('F2', 'MID', format3, 0.5, track)
    add_column_chord('G2', 'MID', format3, 0.5, track)
    add_column_chord('F2', 'MID', format3, 0.5, track)
    add_column_chord('E2', 'MID', format3, 0.5, track)
    add_column_chord('C2', 'MID', format3, 0.5, track)
    add_column_chord('A1', 'MID', format3, 0.25, track)
    add_column_chord('G1', 'MID', format3, 0.25, track)

    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)

    add_column_chord('G', 'MID', format3, 0.5, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.25, track)
    add_column_chord('C1', 'MID', format3, 0.25, track)
    add_column_chord('A', 'MID', format3, 0.5, track)
    add_column_chord('E1', 'MID', format3, 0.25, track)
    add_column_chord('F1', 'MID', format3, 0.25, track)
    add_column_chord('E1', 'MID', format3, 0.25, track)
    add_column_chord('D1', 'MID', format3, 0.5, track)
    add_column_chord('C1', 'MID', format3, 0.5, track)









if __name__ == "__main__":
    chord1(track)
    mid.save("0.mid")
