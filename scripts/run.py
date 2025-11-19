from pathlib import Path

from calculator_pkg_abhinav_jmf import Calculator
from calculator_pkg_abhinav_jmf.file_calculator import FileCalculator

print(Calculator().add(1, 2))
FileCalculator().sum_file(Path("~/Desktop/nums.csv").expanduser())
# FileCalculator().sum_file(Path("/home/anon/Desktop/nums.csv").expanduser())
