#first we need to import the packages we will need from the standard Libraries
import json
import csv

# this section deals with exporting to json. first we will create ab=nd define a function called to_json_files. it will take the user date from the f#fetch_users function

def to_json_file(export_file, users):
    # and then it will dump it out ( it will look nice with the indent=4 we wre specifying)
    json.dump(users, export_file, indent=4)
    # the we will close the export file
    export_file.close()

# This section deals with exporting to csv.
def to_csv_file(export_file, users):
    # With csv, we need a header (like column names)
    # We're specifying here what those names are.
    # Note the \n (newline) at the end of shell.
    # Once the line is done writing, we need to go
    # to the next line and start the actual exporting
    # of the data
    export_file.write('name,id,home,shell\n')

# Now is where we're actually starting to use
    # the csv package. We'll create a writer that
    # will do the actual writing out of the data.
    writer = csv.writer(export_file)

    # We already wrote the header line to the file, and
    # since it ended with a newline character our rows
    # will all go below the header.
    rows = [[user['name'], user['id'], user['home'], user['shell']] for user in users]

    # This is going to actually write the data, rows
    writer.writerows(rows)

    #And this closes the file
    export_file.close()


