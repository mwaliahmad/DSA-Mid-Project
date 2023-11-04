import sys
import csv
import pandas as pd
from PyQt5.uic import loadUi
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from model.video import video
from utils.load_data import load_data
import sortingAlgorithms as sa


if __name__ == "__main__":
    exec(open("UI/main_window.py").read())
