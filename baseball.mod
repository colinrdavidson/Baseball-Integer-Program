# Sets
set PLAYERS;
set POSITIONS := 
  {"C",
  "1B",
  "2B",
  "3B",
  "SS",
  "RF",
  "CF",
  "LF",
  "SP",
  "RP",
  "DH"};


# Player data parameters: name, position, salary, points
param name {PLAYERS} symbolic;
param position {PLAYERS} symbolic in POSITIONS;
param salary {PLAYERS};
param points {PLAYERS};

# Assignment
var x{PLAYERS}, binary;

#Objective Value
maximize team_points :
  sum{i in PLAYERS} x[i]*points[i];

#Constraints
subject to budget : 
  sum{i in PLAYERS} x[i]*salary[i] <= 100000;
subject to catchers :
  sum{i in PLAYERS : position[i] == "C"} x[i] >= 1;
subject to first_basemen :
  sum{i in PLAYERS : position[i] == "1B"} x[i] >= 1;
subject to second_basemen :
  sum{i in PLAYERS : position[i] == "2B"}  x[i]>= 1;
subject to third_basemen :
  sum{i in PLAYERS : position[i] == "3B"}  x[i]>= 1;
subject to shortstops :
  sum{i in PLAYERS : position[i] == "SS"}  x[i]>= 1;
subject to outfielders :
  sum{i in PLAYERS : position[i] == "RF" || position[i] == "CF" || position[i] == "LF"}  x[i]>= 3;
subject to starting_pitchers :
  2 <= sum{i in PLAYERS : position[i] == "SP"}  x[i] <= 3;
subject to other_pitcher :
  sum{i in PLAYERS : position[i] == "SP" || position[i] == "RP"} x[i] == 3;
subject to utility :
  sum{i in PLAYERS} x[i] == 12;

solve;

#Print out the team, unused salary, and how many points the model predicts
printf "\n\nGENERATED TEAM:\n\n";
printf "%-20s %-10s %-10s\n", "Name", "Position", "Salary";
printf {i in PLAYERS : x[i] == 1} "%-20s %-10s %-10.0f\n", name[i], position[i], salary[i];
printf "\n";

printf "UNUSED SALARY: %0.2f\n\n", 100000 - sum{i in PLAYERS : x[i] == 1} salary[i];
printf "PREDICTED POINTS: %0.2f\n\n", sum{i in PLAYERS : x[i] == 1} points[i];


end;
