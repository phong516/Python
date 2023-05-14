#coding: utf-8
from os import name
import sys
from cx_Freeze import setup, Executable
base=None
exe=Executable(script="app.py",base=base)
setup(name="cx_Freeze",version="0.1",description="converter",executables=[exe])