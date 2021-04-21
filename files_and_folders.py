# Prompt
# Make a folder heirarchy like so:
#         current_folder
#                |
#       -------Grandfather----------
#       /     /      \    \     \
#   father1 father2  uncle1 uncle2 uncle3
#              |
#             son
#
#
# within the "son" folder, create 5 .txt files with a name consisting of 
# an animal name and a random 4 digit number  (e.g. "cat_1235.txt")
# randomly choose an animal name from a collection of 5 animal names
#
# print out all the file names
#
# Then create another batch of 5 files, but now they are in the "uncle2" folder
# and the names are same, except that the number portion is now flipped.
# (e.g. "cat_5321.txt")
#
# print out all the file names in "uncle2" folder
#
# out of those 10 files, relocate the ones that end in an even number
# to the "trash"
#
# finally, walk through the entire files and folder tree and print them out.
#
# then delete everything you have created and print out that it was indeed deleted.
#
#
# Few Ending Questions
#   1. What type is the variable "subfolders" when you use os.walk()?
#   2. Where is the "Recycle Bin" on Linux??