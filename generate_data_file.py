import csv

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
        if count != 0:
          temp_row = [i for i in row]
          write_file.write("\n" + str(count) + " \"" + str(temp_row[0]) + "\" \"" + str(temp_row[1]) + "\" " + str(temp_row[2]) + " " + str(temp_row[3]))
        count += 1

      #To signal end of data file
      write_file.write(";\n\nend;")

  #make sure files are closed
  assert read_file.closed == True
  assert write_file.closed == True
