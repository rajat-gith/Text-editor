from curses import window
import keyboard

def restrict_key():

    keyboard.block_key('alt')
    keyboard.block_key('option')
    keyboard.block_key('ctrl')
    keyboard.block_key('Windows')
    keyboard.block_key('command')
    keyboard.block_key('Delete')
    keyboard.block_key('Home')
    keyboard.block_key('insert')
    keyboard.block_key('tab')
    keyboard.block_key('Escape')
