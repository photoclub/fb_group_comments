import csv,sys,os
cur_path = sys.path[0]



print(cur_path)
def initializeFile():
    if(os.path.exists(cur_path+"\\combined_file.csv")):
        print("Continuing because file already exists")
    else:
        print("creating file...")
        with open(cur_path+'\\combined_file.csv', 'w', newline='') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames = ["Group Name", "Group URL", "Comments","Commentor Name","Commentor Profile URL"])
            writer.writeheader()

initializeFile()