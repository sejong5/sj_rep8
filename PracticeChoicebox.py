import easygui
flavor = easygui.choicebox('What is your favorite flavor.', choices = ['Chocolate', 'Vanilla', 'Strawberry'])
easygui.msgbox('You picked ' + flavor)
