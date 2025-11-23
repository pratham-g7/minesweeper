from time import sleep


def animate(func):
    def print_animation(txt, del1=0.04, del2=0.2):  # Changes the print speed
        for i in txt:
            func(i, end="")
            if i not in [".", ",", "?", ":", ";"]:
                sleep(del1)
            else:
                sleep(del2)
        func()
        return func

    return print_animation


@animate
def prints(*args, **kwargs):
    print(*args, **kwargs)
