import time, sys

dots = [".", "..", "..."]
high_dots = ["*", "**", "***"]
cross = ["+", "x"]
slashes = ["/", "\\"]
extended_slashes = ["/", "|", "\\"]
progress_bar = ["|   |", "|=  |", "|== |", "|===|"]
shruggie = ["" ,"¯", "¯\\", "¯\_", "¯\_(", "¯\_(ツ", "¯\_(ツ)", "¯\_(ツ)_", "¯\_(ツ)_/", "¯\_(ツ)_/¯"]
table_flip = ["(╯°□°）╯┳━┳", "(╯°□°）╯┳━┳", "(╯°□°）╯︵┻━┻", "(╯°□°）╯︵  ┳━┳"]
loading_letters = ["","l","lo","loa","load","loadi","loadin","loading"]

mega_fast = [0.04]
quick = [0.2]
medium = [0.5]
slow = [1]

limping = [0.2, 0.2, 0.6]

def clear_line():
    sys.stdout.write("\033[F")

def loading(string, logo, timing, repeat):
    for _ in range(repeat):
        for i in range(len(logo)):
            current_wait = timing[i % len(timing)]
            current_logo = logo[i]

            if "$" + logo[0] + "$" in string:
                current_string = string.replace("$" + logo[0] + "$", current_logo)

            if string == "":
                current_string = current_logo

            else:
                current_string = string.replace("$$", current_logo)

            print(current_string)
            time.sleep(current_wait)
            clear_line()
            print(" "*len(current_string)*2)
            clear_line()


loading("$$", shruggie, mega_fast, 100)
