#!/usr/bin/env bash

# Сначала выполнить следующие команды в cmd:
# gcc -Wall task_2.c -o task -lm                                                    --> компиляция C-файла (на выходе task)
# pip3 install nuitka                                                               --> скачивание nuitka
# python3 -m nuitka task_1.py                                                       --> компиляция Py-файла при помощи nuitka (на выходе task_1.bin)
# gcc task_4_lib_c.c -fPIC -shared -o c_shared_lib.so -lm -Ofast -march=native      --> компиляция C-файла в SO (на выходе c_shared_lib.so, нужен для работы task_4.py)


time python3 task_1.py
time ./task
time ./task_1.bin
time python3 task_4.py

# Если не выйдет дать права на выполнение этого файла, то просто выполните следующую команду в cmd:
# time python3 task_1.py && time ./task && time ./task_1.bin && time python3 task_4.py