import PySimpleGUIQt as sg

logo = r"C:\Users\filph\Desktop\Sara Project\Lightbulb.ico"
menu_def = ['File', ['Hide', '&Open', '&Save',['1', '2', ['a','b']], '&Properties', 'E&xit']]

tray = sg.SystemTray('My Tray', menu=menu_def, filename=logo)

while True:
    menu_item = tray.Read(timeout=0)
    if menu_item is not None:
        print(menu_item)