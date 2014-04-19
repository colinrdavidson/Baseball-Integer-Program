import csv

def generate_data_file(input_file, output_file):
  raw_data = []
  count = 0

  with open(input_file, "r") as read_file:
    with open(output_file, "w") as write_file:
      reader = csv.reader(read_file)
      write_file.write("param : PLAYERS : name position salary points :=")
      for row in reader:
        if count != 0:
          temp_row = [i for i in row]
          write_file.write("\n" + str(count) + " \"" + str(temp_row[0]) + "\" \"" + str(temp_row[1]) + "\" " + str(temp_row[2]) + " " + str(temp_row[3]))
        count += 1

      write_file.write(";\n\nend;")

  assert read_file.closed == True
  assert write_file.closed == True
