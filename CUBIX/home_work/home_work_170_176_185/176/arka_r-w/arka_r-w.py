
path_r = 'CUBIX/home_work/home_work_170_176_185/176/arka_r-w/arka_input.txt'
with open(path_r, mode='r') as file:
    arka = file.read()
    print("input reading finished...")
counter = 0
counter = arka.count("arka")


result = f"There are {counter} occurrences in the arka tale."
path_w = 'CUBIX/home_work/home_work_170_176_185/176/arka_r-w/arka_output.txt'
with open(path_w, mode="w") as file:
    file.write(result)
    print("output is ready as 'arka_output.txt'")