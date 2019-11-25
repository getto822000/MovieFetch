import os, os.path, random, shutil

print "Enter source directory for your videos (don't forget the /) : "
source_directory = raw_input()
       
videoCounter = 0
for root, dirs, files in os.walk(source_directory):
    for file in files:    
        if file.endswith('.mp4'):
            videoCounter += 1
            
print "You have",(videoCounter),"videos."

print "How many random videos do you want to select?"
number_select_videos = int(raw_input())

print "Enter destination directory for your random videos (make sure it is empty) : "
destination_directory = raw_input()

full_path_movies_list = []

for root, dirs, files in os.walk(source_directory):
    for f in files:
        full_path_movies = os.path.join(root, f)
        if os.path.splitext(full_path_movies)[1] == '.mp4':		
    		full_path_movies_list.append(full_path_movies)

destination_files = 0
while destination_files <= number_select_videos:
	random_video = random.choice(full_path_movies_list)
	shutil.copy2(random_video, destination_directory)
	destination_files = sum(len(files) for  r,d, files in os.walk(destination_directory))
   			
print("\n\n"+"$"*23+"[" + str(destination_files - 1) + " Videos Moved Successfully ]"+"$"*23)
