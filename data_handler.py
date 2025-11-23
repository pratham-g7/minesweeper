from random import choice
from pickle import load, dump, UnpicklingError
from string import ascii_uppercase, digits


def save_data(data: list, save_path, code=None):
    if code != None:
        del_save(code, save_path)
    else:
        code = "".join([choice(ascii_uppercase)] + [choice(digits) for _ in range(5)])
    with open(save_path, mode="rb+") as saves:
        dump({code: data}, saves)
    return code


def load_data(cd: str, save_path):
    global saved
    global code
    data = []
    with open(save_path, mode="rb+") as saves:
        saves.seek(0)
        while True:
            try:
                data.append(load(saves))
            except EOFError:
                break
            except UnpicklingError:
                break
    for save in data:
        if cd in list(save.keys()):
            saved = True
            code = cd
            return True, save[cd]
    else:
        return False, None


def del_save(r_code, save_path):
    b_data = []
    with open(save_path, mode="rb+") as saves:
        while True:
            try:
                b_data.append(load(saves))
            except EOFError:
                break
        b_data = [b for b in b_data if r_code not in list(b.keys())]
        saves.truncate(0) 
        for i in b_data:
            dump(i, saves)
