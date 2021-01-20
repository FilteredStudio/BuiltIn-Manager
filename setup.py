from distutils.core import setup # Need this to handle modules
import py2exe
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
#from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter.ttk import Button
import os

setup(windows=["builtinmanager.py"], data_files=[("settings", ["settings.txt"])])
