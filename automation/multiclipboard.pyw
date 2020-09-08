# multiclipboard.pyw - Saves and loads pieces of text to the clipboard.

import shelve, sys
import pyperclip

mcbshelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save' :
    mcbshelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])

mcbshelf.close()