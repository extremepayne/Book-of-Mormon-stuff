# Random verse generator
# Goal: randomly generate a verse from any part 
# of the Book of Mormon with each verse having 
# an equal probablilty


# imports
import random


# This wil be accomplished by creating a list with 
# each of the verses in the Book of Mormon in it,
# then selecting a random element from that list.


# variable
# This is a dictionary that contains all the information
# needed to kow which verses are in the BoM and which aren't
# (like 1 Nephi 1:21 or Enos 2:1)
# The key is the name of the book
# The vaue (a list) represents both the chapters and their verses.
# Each number in the list is a nuber of verses, the chapter is stated
# implicitly as the index. (Plus one, since chapters start at 1 and indices
# start at 0.)
# I included the number of chapters in each book in a comment at the
# end of every value (list).
BoM_books = {
			"1 Nephi" : [20, 24, 31, 38, 22, 6,  22, 38, 6,  22, 36, 23, 42, 30,
						 36, 39, 55, 25, 24, 22, 26, 31], #22
			"2 Nephi" : [32, 30, 25, 35, 3,  18, 11, 25, 53, 25, 8,  22, 26, 6,  
						 30, 13, 25, 22, 21, 34, 16, 6,  22, 32, 30, 33, 35, 32,
						 14, 18, 21, 9,  15], #33
			"Jacob" :   [19, 35, 14, 18, 77, 13, 27], #7
			"Enos" :    [27], #1
			"Jarom" :   [15], #1
			"Omni" :    [30], #1
			"WoM" :     [18], #1
			"Mosiah" :  [18, 41, 30, 15, 7,  33, 21, 19, 22, 29, 37, 35, 12, 31,
						 15, 20, 35, 29, 26, 16, 39, 25, 24, 39, 37, 20, 47], #29
			#"Alma" :   [33, 38, 27, 20, 62, 8, 27, 32, 34, ], #63
			"Helaman" : [34, 14, 37, 26, 52, 41, 29, 28, 41, 19, 38, 26, 39, 31, 17, 25], #16
			"3 Nephi" : [30, 19, 26, 33, 26, 30, 26, 25, 22, 19, 41, 48, 34, 27,
						 24, 20, 25, 39, 35, 46, 29, 17, 14, 18, 6,  21, 33, 40,
						 9,  2], #30
			"4 Nephi" : [49], #1
			"Mormon" :  [19, 29, 22, 23, 24, 22, 10, 41, 37], #9
			"Ether" :   [43, 25, 28, 19, 6,  30, 27, 26, 35, 34, 23, 41, 31, 31, 34], #15
			"Moroni" :  [4,  3,  4,  3,  2,  9,  48, 30, 26, 34] #10
			}





# define verses list
verses = []


# write verses list

# For each element in BoM_books dictionary 
for book, chapter_list in BoM_books.items():

	chapter = 0
	# Go through each chapter
	for num_verses in chapter_list:
		chapter += 1 # Each time this loop iterates, we go one index 
					 # (and one chapter) farther into the list.
		# Create string referring to chapter
		verse_ref = book + " " + str(chapter) + ":"

		verse = 1
		# Then go through each verse
		while verse <= num_verses:
			# And add that verse's reference to the end of the list
			verses.append(verse_ref + str(verse))
			verse += 1



# At this point we have a list of all the verses in the BoM.

# Pick a random number within bounds of list
number = random.randint(0, len(verses)-1)
# And print...
print(verses[number])

# And we're done!
input("Press enter to exit.") # This line prevents the window from 
							  # closing immediately if ran as it's
							  # own window.
