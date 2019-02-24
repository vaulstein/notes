#!/usr/bin/env python

import urwid
import urwid.raw_display
import urwid.web_display


def main():
    text_header = (u"NOTES  "
        u"UP / DOWN / PAGE UP / PAGE DOWN scroll.  F8 exits.")

    text_intro = [('important', u"Text"),
                  u" widgets are the most common in "
                  u"any urwid program.  This Text widget was created "
                  u"without setting the wrap or align mode, so it "
                  u"defaults to left alignment with wrapping on space "
                  u"characters.  ",
                  ('important', u"Change the window width"),
                  u" to see how the widgets on this page react.  "
                  u"This Text widget is wrapped with a ",
                  ('important', u"Padding"),
                  u" widget to keep it indented on the left and right."]

    blank = urwid.Divider()
    listbox_content = [
        blank,
        urwid.Padding(urwid.Text(text_intro), left=2, right=2, min_width=20)
    ]

    def button_press(button):
        frame.footer = urwid.AttrWrap(urwid.Text(
            [u"Pressed: ", button.get_label()]), 'header')

    header = urwid.AttrWrap(urwid.Text(text_header), 'header')

    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)

    palette = [
        ('body', 'black', 'dark gray', 'standout', '#669', '#9ff'),
        ('reverse', 'light gray', 'black'),
        ('header', 'white', 'dark red', 'bold'),
        ('important', 'dark blue', 'light gray', ('standout', 'underline')),
        ('editfc', 'white', 'dark blue', 'bold'),
        ('editbx', 'light gray', 'dark blue'),
        ('editcp', 'black', 'light gray', 'standout'),
        ('bright', 'dark gray', 'light gray', ('bold', 'standout')),
        ('buttn', 'black', 'dark cyan'),
        ('buttnf', 'white', 'dark blue', 'bold'),
    ]

    screen = urwid.raw_display.Screen()

    def unhandled(key):
        if key == 'f8':
            raise urwid.ExitMainLoop()

    urwid.MainLoop(frame, palette, screen,
        unhandled_input=unhandled).run()

def setup():
    main()


if '__main__'==__name__:
    setup()