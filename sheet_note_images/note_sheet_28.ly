\version "2.18.2"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

#(set-default-paper-size "a10" 'landscape) %! abjad.LilyPondFile._get_formatted_scheme_settings()
#(set-global-staff-size 14)                %! abjad.LilyPondFile._get_formatted_scheme_settings()

\header { %! abjad.LilyPondFile._get_formatted_blocks()
    tagline = ##f
} %! abjad.LilyPondFile._get_formatted_blocks()

\layout {}

\paper {}

\score { %! abjad.LilyPondFile._get_formatted_blocks()
    \new Staff
    {
        gs''1
        af''1
    }
} %! abjad.LilyPondFile._get_formatted_blocks()