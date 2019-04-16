import curses

def main(stdscr):
    stdscr.addstr('hello world')
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)