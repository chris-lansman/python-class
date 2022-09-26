# Introduction to Computer Science in Python
## Lessons/files for the course.
### This repository will be updated weekly. Perform a 'git-pull' on a regular basis to verify you have the latest files.

#### The student-hw folder is where homework will be uploaded on a weekly basis.

#### Using Git
***Note: These commands have to be run from inside the python-class repository (folder) on your local machine from the commandline. 
         You will need to open a terminal to the folder. See video here for a how-to: TODO ADD VIDEO
         
- Update your local copy of the class files with any new files from this repository.
    git pull
- If you have modified any files in the classwork folder and you want to reset them back to their original state use the following command
    git checkout -- classwork
- If you want to reset the entire folder you have two options:
    1) Delete the folder completely and re-clone the repository.
        a) git clone https://github.com/chris-lansman/python-class.git
    2) Perform a "hard reset"
        a) git reset --hard
   
#### Uploading HW assignments
Each week you will be expected to upload the homework assignment by Friday morning.
You will "push" your changes to this repository to the corresponding classwork/week# folder.
Your file name should be in the format LastName_FirstName_HW_Week#.py
  ex) Lansman_Chris_HW_Week2.py

##### Steps to upload HW assignments
Tutorial video here: TODO ADD VIDEO

1) Create the file you will save your code in down in the corresponding /python-class/student-hw/week# folder
2) Once you have finished the file and verified it runs save your changes.
3) Prepare the file for push (upload) to the repository here on gitlab
    From the command line:
      a) Add your file to your local copy of the repository
          a.1) git add student-hw/week#/LastName_FirstName_HW_Week#.py
      b) Add a comment as to what this change is.
          b.1) git commit -m "Adding my HW assignment for week 3 to the repository"
      c) Finally "push" (upload your change to the this remote repository)
          c.1) git push
                After the push you should see something like:
                $ git push
                      Enumerating objects: 7, done.
                      Counting objects: 100% (7/7), done.
                      Delta compression using up to 16 threads
                      Compressing objects: 100% (4/4), done.
                      Writing objects: 100% (5/5), 522 bytes | 522.00 KiB/s, done.
                      Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
                      remote: Resolving deltas: 100% (1/1), completed with 1 local object.
                      To https://github.com/chris-lansman/python-class.git
                         6469429..d01aba7  main -> main
                         
At this point you have uploaded your homework assignmnet for the week and are done.
