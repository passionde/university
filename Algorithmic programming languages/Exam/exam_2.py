def life_path_number(dob: str):
    dob = dob.replace("-", "")
    if len(dob) == 1:
        return int(dob[0])

    return life_path_number(str(int(dob[0]) + life_path_number(dob[1:])))


print(life_path_number("1879-03-14"))
print(life_path_number("2001-11-07"))
