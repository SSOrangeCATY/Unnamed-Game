init = False

def screen_display_logic(window=None, event=None):
    global init
    import main
    from screen.Screen import registryScreen
    if init is False:
        main.screens = registryScreen()
        init = True
    if main.game_first_loading is True: 
        main.current_screen = main.screens.get_screen("LoadingScreen")
        #debug code
        #print("loading screen")
    else :
        main.current_screen = main.screens.get_screen("MainTitle")
        #debug code
        #print("main title")
        
    main.current_screen.display(window,event)
    main.display_update()
    