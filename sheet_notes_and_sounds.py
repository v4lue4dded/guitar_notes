

import abjad
import os
from midi2audio import FluidSynth
import copy

os.chdir('sheet_note_images')
os.getcwd()

note_range = range(-8,22) 
note_index = range(0,len(note_range))

notes = [abjad.Note(pitch, 1) for pitch in note_range]
notes_lists = [list(str(x)) for x in notes]

for i in note_index:
    n = notes[i]
    n_list = notes_lists[i]
    if n_list[1].isalpha():
        n_s_list = copy.deepcopy(notes_lists[i-1])
        n_s_list.insert(1,'s')
        n_s = abjad.Note(''.join(n_s_list))
        n_f_list = copy.deepcopy(notes_lists[i+1])
        n_f_list.insert(1,'f')
        n_f = abjad.Note(''.join(n_f_list))
        print(n_s, n_f)
        staff = abjad.Staff([n_s, n_f])
    else:
        print(n)
        staff = abjad.Staff([n])

    lilypond_file = abjad.LilyPondFile.new(
    staff
    , global_staff_size=14
    , default_paper_size=('a10', 'landscape')
    )

    f = open("note_sheet_"+str(i)+".ly", "w")
    f.write(format(lilypond_file))
    # f.close()
    sound_file = "note_sound_"+str(i)
    abjad.persist(n).as_midi(sound_file+".mid") 


    i += 1#


from pdf2image import convert_from_path

i = 0

for i in note_index:
    image = convert_from_path("note_sheet_"+str(i)+".pdf", 1000)
    image[0].save("note_sheet_"+str(i)+".png","PNG")

    # fs = FluidSynth()
    # x = 'C:\\Users\\SFede\\Dropbox (Privat)\\repos\\Music\\sheet_note_images\\'+sound_file+".mid"
    # x = 'C:/Users/SFede/'+sound_file+".mid"
     
    # fs.midi_to_audio(x , sound_file+".wav")



# staff = abjad.Staff(notes)
# abjad.show(staff)

# abjad.Note("c1 cs1 df1 d1")
# abjad.show(abjad.Staff([abjad.Note("c1")]))


# abjad.show(abjad.Staff([abjad.Note("c1")]))
# abjad.show(abjad.Staff([abjad.Note("c1")]))
# abjad.show(abjad.Staff([abjad.Note("c1")]))


# note = abjad.Note("c'1")
# # abjad.show(note)

# notes = [abjad.Note(pitch, 1) for pitch in ["c'","cs'","df'","d'"]]
# staff = abjad.Staff(notes)
# abjad.show(staff)


# abjad.show(Staff())

# abjad.show()

# note = abjad.Note("c'4")



# import abjad





# staff = abjad.Staff("c'4 d'4 e'4 f'4")
# lilypond_file = abjad.LilyPondFile.new(
#   staff
# , global_staff_size=14
# , default_paper_size=('a10', 'portrait')
# )

# # lilypond_file.header_block.composer = abjad.Markup('Josquin')
# # lilypond_file.header_block.title = abjad.Markup('Missa sexti tonus')
# # lilypond_file.layout_block.indent = 0
# # lilypond_file.layout_block.left_margin = 15

# # lilypond_file.paper_block.set_paper_size = ("a10","landscape")






# print(format(lilypond_file))

# import glob
# import os

# list_of_files = glob.glob('C:\\Users\\SFede\\.abjad\\output\\*') # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
# print(latest_file)


# from pdf2image import convert_from_path
# image = convert_from_path(latest_file, 1000)

# image[0].show()


# # vowel list
# vowel = ['a', 'e', 'i', 'u']

# # inserting element to list at 4th position
# vowel.insert(3, 'o')

# print('Updated List: ', vowel)