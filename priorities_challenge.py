#https://www.archives.gov/electoral-college/allocation
#Found a correct list of electoral votes in 2020

actual = '''Alabama - 9 votes

Kentucky - 8 votes

North Dakota - 3 votes

Alaska - 3 votes

Louisiana - 8 votes

Ohio - 18 votes

Arizona - 11 votes

Maine - 4 votes

Oklahoma - 7 votes

Arkansas - 6 votes

Maryland - 10 votes

Oregon - 7 votes

California - 55 votes

Massachusetts - 11 votes

Pennsylvania - 20 votes

Colorado - 9 votes

Michigan - 16 votes

Rhode Island - 4 votes

Connecticut - 7 votes

Minnesota - 10 votes

South Carolina - 9 votes

Delaware - 3 votes

Mississippi - 6 votes

South Dakota - 3 votes

District of Columbia - 3 votes

Missouri - 10 votes

Tennessee - 11 votes

Florida - 29 votes

Montana - 3 votes

Texas - 38 votes

Georgia - 16 votes

Nebraska - 5 votes

Utah - 6 votes

Hawaii - 4 votes

Nevada - 6 votes

Vermont - 3 votes

Idaho - 4 votes

New Hampshire - 4 votes

Virginia - 13 votes

Illinois - 20 votes

New Jersey - 14 votes

Washington - 12 votes

Indiana - 11 votes

New Mexico - 5 votes

West Virginia - 5 votes

Iowa - 6 votes

New York - 29 votes

Wisconsin - 10 votes

Kansas - 6 votes

North Carolina - 15 votes

Wyoming - 3 votes'''

#Pulled from the question provided
incorrect = 'Alabama - 9 votes, Alaska - 3 votes, Arizona - 11 votes, Arkansas - 6 votes, California - 25 votes, Colorado - 9 votes, Connecticut - 7 votes, Delaware - 3 votes, District of Columbia - 3 votes, Florida - 29 votes, Georgia - 16 votes, Hawaii - 4 votes, Idaho - 4 votes, Illinois - 20 votes, Indiana - 11 votes, Iowa - 6 votes, Kansas - 6 votes, Kentucky - 8 votes, Louisiana - 8 votes, Maine - 4 votes, Maryland - 10 votes, Massachusetts - 11 votes, Michigan - 16 votes, Minnesota - 10 votes, Mississippi - 6 votes, Missouri - 10 votes, Montana - 3 votes, Nevada - 6 votes, New Hampshire - 14 votes, New Jersey - 14 votes, New Mexico - 5 votes, New York - 29 votes, North Carolina - 15 votes, North Dakota - 3 votes, Ohio - 18 votes, Oklahoma - 7 votes, Oregon - 7 votes, Pennsylvania - 20 votes, Providence - 4 votes, South Carolina - 9 votes, South Dakota - 3 votes, Tennessee - 11 votes, Texas - 38 votes, Utah - 6 votes, Vermont - 2 votes, Virginia - 13 votes, Washington - 12 votes, West Virginia - 5 votes, Wisconsin - 10 votes, Wyoming - 3 votes'

#Cleaning up the actual data into netsted lists with ready to go key-value pairs
actual_list = actual.split(' votes\n\n')
for i in range(len(actual_list)):
  actual_list[i] = actual_list[i].split(' - ')

#Cleaning up the incorrect data into netsted lists with ready to go key-value pairs
incorrect_list = incorrect.split(' votes, ')
for i in range(len(incorrect_list)):
  incorrect_list[i] = incorrect_list[i].split(' - ')

#Turning the nested lists into dictinoaries
actual_dict={i[0]:i[1] for i in actual_list}
incorrect_dict={i[0]:i[1] for i in incorrect_list}

#Creating a dictionary of akin pairs between lists to test against later
pairs = {k: incorrect_dict[k] for k in incorrect_dict if k in actual_dict and incorrect_dict[k] == actual_dict[k]}

#Deleting akin pairs from the actual list and printing remainder
for key in pairs.keys():
    del actual_dict[key]
print(actual_dict)

#Deleting akin pairs from the incorrect list and printing remainder
for key in pairs.keys():
    del incorrect_dict[key]
print(incorrect_dict)
