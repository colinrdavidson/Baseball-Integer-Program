#Default Modules
import argparse
import os.path
import subprocess
import sys

#Custom Modules
from generate_data_file import generate_data_file as gdf

#Set up arg parser
parser = argparse.ArgumentParser(description="Generate an optimal draft team.")
parser.add_argument("--input", "-i", dest="input_file", nargs=1, required=True, help="the csv where the data is stored") 
parser.add_argument("--output", "-o", dest="output_file", nargs=1, required=False, default=["output.txt"], help="the file to write the logs and team to") 
args = parser.parse_args()

#Assign args to variables
input_file = args.input_file[0]
output_file = args.output_file[0]

#Message
print("\nInput File: \"" + input_file + "\"")
print("Output File: \"" + output_file + "\"\n")

#See if input file exists
try:
  f = open(input_file, "r")
  f.close()
except IOError:
  sys.exit("Cannot open \"" + input_file + "\", aborting...")

#Message
print("Creating data file for glpk...")

#Generate glpk Data File
try:
  gdf(input_file, "baseball.dat")
except:
  print("There was a problem generating \"baseball.dat\" from \"" + input_file + ", aborting...")
  print("Here is the python exception:\n")
  raise

print("  ...success!\n")

#Run the model

#See if "baseball.dat" file exists
try:
  f = open("baseball.dat", "r")
  f.close()
except IOError:
  sys.exit("Cannot open \"baseball.dat\", aborting...")

#See if "baseball.mod" file exists
try:
  f = open("baseball.mod", "r")
  f.close()
except IOError:
  sys.exit("Cannot open \"baseball.mod\", aborting...")

#Message
print("Running command:")
print("  glpsol --math --data baseball.dat --model baseball.mod\n")

#Run external command "glpsol"
with open(output_file, "w") as f:
  argarray = ["glpsol", "--math", "--data", "baseball.dat", "--model", "baseball.mod"] 
  subprocess.call(argarray, stdout=f)

#Message
print("Output written to \"" + output_file + "\"")
