from runner import Runner
from loader import Loader
from console_printer import ConsolePrinter


print("Social network simulator.")
Runner(Loader(), ConsolePrinter()).run_program(input("Enter a file name for network data: "))
