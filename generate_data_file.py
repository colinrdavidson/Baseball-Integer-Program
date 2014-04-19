import csv
import sys

#A function to generate a data file for glpk
#The input file is a csv where:
#     column 1 is name
#     column 2 is position
#     column 3 is salary
#     column 4 is points
def generate_data_file(input_file, output_file):
  raw_data = []
  count = 0

  #Open csv/data file for reading/writing
  with open(input_file, "r") as read_file:
    with open(output_file, "w") as write_file:
      #Parse csv
      reader = csv.reader(read_file)
      #Need this line
      write_file.write("param : PLAYERS : name position salary points :=")
      
      #Write each line of csv to data file
      for row in reader:
        #Checks on heading names
        if count == 0:
          if row[0].lower() not in ["name", "player"]:
            while True:
              ans = input("The first column should be the player's name, but the heading is \"" + str(row[0]) + "\". Is it okay to proceed? [y/n]: ")
              if ans.lower() == "y":
                break
              elif ans.lower() == "n":
                print("Okay, aborting...")
                sys.exit("UserInput: Something wrong with headings, bail.")
              else:
                print("INVALID INPUT")

          if row[1].lower() not in ["position", "pos"]:
            while True:
              ans = input("The second column should be the player's position, but the heading is \"" + str(row[1]) + "\". Is it okay to proceed? [y/n]: ")
              if ans.lower() == "y":
                break
              elif ans.lower() == "n":
                print("Okay, aborting...")
                sys.exit("UserInput: Something wrong with headings, bail.")
              else:
                print("INVALID INPUT")

          if row[2].lower() not in ["salary", "sal"]:
            while True:
              ans = input("The third column should be the player's salary, but the heading is \"" + str(row[2]) + "\". Is it okay to proceed? [y/n]: ")
              if ans.lower() == "y":
                break
              elif ans.lower() == "n":
                print("Okay, aborting...")
                sys.exit("UserInput: Something wrong with headings, bail.")
              else:
                print("INVALID INPUT")

          if row[3].lower() not in ["points", "poi", "score"]:
            while True:
              ans = input("The fourth column should be the player's predicted points, but the heading is \"" + str(row[3]) + "\". Is it okay to proceed? [y/n]: ")
              if ans.lower() == "y":
                break
              elif ans.lower() == "n":
                print("Okay, aborting...")
                sys.exit("UserInput: Something wrong with headings, bail.")
              else:
                print("INVALID INPUT")


        if count != 0:
          temp_row = [i for i in row]
          write_file.write("\n" + str(count) + " \"" + str(temp_row[0]) + "\" \"" + str(temp_row[1]) + "\" " + str(temp_row[2]) + " " + str(temp_row[3]))
        count += 1

      #To signal end of data file
      write_file.write(";\n\nend;")

  #make sure files are closed
  assert read_file.closed == True
  assert write_file.closed == True
