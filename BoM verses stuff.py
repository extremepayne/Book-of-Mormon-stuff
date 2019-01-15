#I'm not going to comment this very well, it's just for a infographic.
#If you want to know how this all works, random BoM verse.py has most of this same code, but better commented.
BoM_books = {
			"1 Nephi" : [20, 24, 31, 38, 22, 6,  22, 38, 6,  22, 36, 23, 42, 30,
						 36, 39, 55, 25, 24, 22, 26, 31], #22
			"2 Nephi" : [32, 30, 25, 35, 3,  18, 11, 25, 53, 25, 8,  22, 26, 6,  
						 30, 13, 25, 22, 21, 34, 16, 6,  22, 32, 30, 33, 35, 32,
						 14, 18, 21, 9,  15], #33
			"Jacob" : 	[19, 35, 14, 18, 77, 13, 27], #7
			"Enos" : 	[27], #1
			"Jarom" : 	[15], #1
			"Omni" : 	[30], #1
			"WoM" : 	[18], #1
			"Mosiah" : 	[18, 41, 30, 15, 7,  33, 21, 19, 22, 29, 37, 35, 12, 31,
						 15, 20, 35, 29, 26, 16, 39, 25, 24, 39, 37, 20, 47], #29
			#"Alma" : #63,
			#"Helaman" : #16,
			"3 Nephi" : [30, 19, 26, 33, 26, 30, 26, 25, 22, 19, 41, 48, 34, 27,
						 24, 20, 25, 39, 35, 46, 29, 17, 14, 18, 6,  21, 33, 40,
						 9,  2], #30
			"4 Nephi" : [49], #1
			"Mormon" :  [19, 29, 22, 23, 24, 22, 10, 41, 37], #9
			#"Ether" : #15,
			"Moroni" :  [4,  3,  4,  3,  2,  9,  48, 30, 26, 34] #10
			}


count = 0
my_list = []
for book, chapter_list in BoM_books.items():
	chapter = 0
	for num_verses in chapter_list:
		chapter += 1
		if num_verses == chapter:
			count += 1
			my_list.append(book + str(chapter))



print("Chapters that have the same number of verses as the chapter.")
print(count, my_list)
input("Press enter to exit")