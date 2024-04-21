

def screen_display_logic(window=None, event=None):
    import main
    from screen.mainTitle import mainTitle
    from screen.loadingScreen import loading_screen
    
    if main.game_first_loading is True: 
        main.current_screen = loading_screen
        #debug code
        #print("loading screen")
    else :
        main.current_screen = mainTitle
        #debug code
        #print("main title")S
        
    main.current_screen.display(window,event)
    main.game.display.update()
    
