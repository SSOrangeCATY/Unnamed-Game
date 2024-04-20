
        
def screen_display_logic(window):
    import main
    import screen.loadingScreen
    import screen.mainTitle
    if main.game_first_loading is True: 
        screen.loadingScreen.loading_screen(window)
        #debug code
        print("loading screen")
    else:
        screen.mainTitle.main_title(window)
        #debug code
        print("main title")
    main.game.display.update()
   