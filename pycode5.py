#!/usr/bin/python3

from os import cpu_count
from os import curdir
from os import getenv
from os import getpid
from os import getppid

print(f'cpu_count   :  {cpu_count()}')
print(f'curdir      :  {curdir}')
print(f'getenv      :  {getenv("MAIL")}')
print(f'getpid      :  {getpid()}')
print(f'getppid     :  {getppid()}')

