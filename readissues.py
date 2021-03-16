import openpyxl
import ghimport

wb_obj = openpyxl.load_workbook('issuesFinaleClean.xlsx') 

# Read the active sheet:
sheet = wb_obj.active
for row in sheet.iter_rows(max_row=6297):
	title = str(row[0].value)
	tags = str(row[3].value)
	# Make sure to match the columns to the fields you want to import
	if row[1].value == "Verified" or row[1].value == "Obsolete" or row[1].value == "Won't Fix" or row[1].value == "Archived" or row[1].value == "Can't Reproduce" or row[1].value == "Done":
		state = "closed"
	else:
		state = "open"

	# Make sure you fill in the milestones IDs
	milestone = None
	if "Version:7" in tags:
		milestone = 19
	if "Version:8.0" in tags:
		milestone = 20
	if "Version:8.1" in tags:
		milestone = 21
	if "Version:8.2" in tags:
		milestone = 15
	if "Version:9" in tags:
		milestone = 16
	if "Version:9.0" in tags:
		milestone = 16
	if "Version:9.1" in tags:
		milestone = 17

	description = str(row[2].value)

	ghimport.make_github_issue(title,description,None,None,None,None,milestone,state,tags)
