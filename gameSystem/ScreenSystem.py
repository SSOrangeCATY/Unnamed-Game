def screen_display_logic(window=None, event=None):
    import main
    import screen.mainTitle
    import screen.loadingScreen
    if main.game_first_loading is True and window is not None: 
        screen.loadingScreen.loading_screen(window)
        #debug code
        #print("loading screen")
    else:
        if window is not None:
           screen.mainTitle.main_title(window)
        if event is not None:
           screen.mainTitle.button_event(event)
        #debug code
        #print("main title")
    main.game.display.update()
    
