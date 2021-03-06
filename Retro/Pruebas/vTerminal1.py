'''
Se puede instalar tambien con
apt-get install python-urwid
'''

import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#8cf'),
    ('inside', '', '', '', 'g38', '#8c0'),
    ('outside', '', '', '', 'g27', '#f80'),
    ('bg', '', '', '', 'g7', '#666'),]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(placeholder, 'bg')
loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

div = urwid.Divider()
outside = urwid.AttrMap(div, 'outside')
inside = urwid.AttrMap(div, 'inside')
txt = urwid.Text(('banner', u" Fer Retro programming "), align='center')
streak = urwid.AttrMap(txt, 'streak')
pile = loop.widget.base_widget # .base_widget skips the decorations
for item in [outside, inside, streak, inside, outside]:
    pile.contents.append((item, pile.options()))

loop.run()