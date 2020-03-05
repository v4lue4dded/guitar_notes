import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import os


os.chdir('guitar_images')

whole_notes = ['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']*2


scales = { 
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2 , 3, 5, 7, 10, 11],
    "dorian" : [0,  2,  3,  5,  7,  9, 10, 12],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10, 12],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 10, 12],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10, 12],
    "lydian" :[0, 2, 4, 6, 7, 9, 11, 12],
}

def get_notes(key, intervals):
    # a sufficiently long sequence of notes to slice from
    whole_notes = ['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']*3
    # finding start of slice
    root = whole_notes.index(key)
    # taking 12 consecutive elements
    octave = whole_notes[root:root+12]
    # accesing indexes specified by `intervals` to retrieve notes
    return [octave[i] for i in intervals]

# # initializing a dict with the name of the strings as keys
# strings = {i:0 for i in 'EADGB'}
# for i in strings.keys():
#     # finding the index of first note in the string
#     start = whole_notes.index(i)
#     # taking a slice of 20 elements
#     strings[i] = whole_notes[start:start+20]

whole_notes_basic = ["C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"]
whole_notes = whole_notes_basic + ["'" + x for x in whole_notes_basic] + ["''" + x for x in whole_notes_basic]

strings = ["E", "A", "'D", "'G", "'B", "''E"]

string_notes = dict()

for s in strings:
    s_index = whole_notes.index(s)
    print(s,s_index )
    string_notes[s] = whole_notes[s_index:(s_index+7)]


# def plot(key, intervals, night=True):


night=False


for q_a in ["question", "answer"]:
    for j in range(0,30):
        n_j = whole_notes[4+j]
        print(j,n_j)
        # Plot Strings 
        fig, ax = plt.subplots(figsize=(7,6))
        background = ['white', 'black']
        for i in range(1,7):
            ax.plot([i for a in range(22)])
            

        # setting color of the background using argument night
        ax.set_facecolor(background[night])
        # finding note positions of the scale in the guitar
        # to_plot = find_notes(scale)

        # for every note of the scale in every string make a circle
        # with the note's name as label in the corresponding fret

        for y_val, key in zip([1,2,3,4,5,6], ["E", "A", "'D", "'G", "'B", "''E"]):
            # print(y_val, key)
            for i in range(0,6):
                # print(i)
                font = 12
                x = i+0.5  # shift the circles to the right
                note = string_notes[key][i]
                if n_j == note:
                    p = mpatches.Circle((x, y_val), 0.3, zorder=9, linewidth= 3, facecolor = "white", edgecolor="red"  )
                else:
                    p = mpatches.Circle((x, y_val), 0.3, zorder=9, linewidth= 3, facecolor = "white", edgecolor="grey")

                ax.add_patch(p)
                # if note is the root make it a bit bigger
                # add label to middle of the circle
                if q_a == "answer":
                    ax.annotate(note, (i+0.5, y_val), color='black', weight='bold', 
                                    fontsize=8, ha='center', va='center', zorder=999999)

        ax.add_patch(mpatches.Circle((3.5, 3.5), 0.07, zorder=9, linewidth= 3, color="black"))
        ax.add_patch(mpatches.Circle((5.5, 3.5), 0.07, zorder=9, linewidth= 3, color="black"))

        ax.axhline(y=6.4, color="black", linewidth=3, zorder=999)
        ax.axhline(y=0.6, color="black", linewidth=3, zorder=999)

        # Plotting Frets
        for i in range(1,7):
            # decorates the twelve fret with a gray and thick fret
            # trace a vertical line (a fret)
            if i == 1:
                ax.axvline(x=i, color=background[night-1], linewidth=2.5, zorder=999)
            else:
                ax.axvline(x=i, color=background[night-1], linewidth=0.5, zorder=999)
            





        ax.set_axisbelow(True)
        # setting height and width of displayed guitar
        ax.set_xlim([0.5, 5.1])
        ax.set_ylim([0.4, 6.5])
        plt.axis('off')
        plt.yticks(np.arange(1,7), ["E", "A", "'D", "'G", "'B", "''E"])
        plt.xticks(np.arange(7)+0.5, np.arange(0,22))
        plt.savefig('guitar_picture_'+q_a+"_"+str(j)+'.png')