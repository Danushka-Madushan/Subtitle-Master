import re
import os
import sys
import requests
import msvcrt
import time

try:
	url = input("\n (Baiscopelk) TV-Series Link : ")
	x = re.match(r'^(https?://|)*www.baiscopelk.com/tv-series/', url)
	start = time.time()
	if x:

		req = requests.get(url).content.decode('utf-8')
		file = open("webdata.dat", "w", encoding='utf-8', errors="ignore")
		file.write(req)
		file.close()
		a_file = open("webdata.dat", "r", encoding='utf-8', errors="ignore")
		string_without_line_breaks = ("")
		for line in a_file:
		  stripped_line = line.rstrip()
		  string_without_line_breaks += stripped_line
		a_file.close()
		data = re.search(r'<tbody>(.+?)</tbody>' ,string_without_line_breaks).group(1)
		os.system("del webdata.dat")
		e = re.findall(r'href="(https?://www.baiscopelk.com/\S+|[-a-zA-Z0-9 @:%._\/+~#?=]*)"', data)
		episodes = []

		for m in e:
			episodes.append(m)
		print("\n ---------------------------------- ")
		print(f" : {str(len(episodes)).zfill(3)} Links found! ")
		print(" ---------------------------------- ")
		if len(episodes) == 0:
			msvcrt.getch()
			sys.exit()

		links = []
		index = 1
		f_index = 0
		for k in episodes:
			link_data = requests.get(k).content.decode("utf-8")
			s = re.findall(r'href="(https?[:][/][/]www[.]baiscopelk[.]com/Downloads/\S+|[-a-zA-Z0-9 @:%._\+~#=]*[/])">.*<[/]a>', link_data)
			title = re.findall(r'<h1[ ]class="name[ ]post-title[ ]entry-title"><span[ ]itemprop="name">([-a-zA-Z0-9() @%._\+~#=]*)', link_data)
			if len(s) == 0:
				h = open("Dead_links.txt", "w+")
				h.write(k + "\n")
				h.close()
				f_index+=1
			for n in s:
				if len(n) >= 1:
						links.append(n)
			print(f" : Processing... [ Processed : {index} ] [ Dead links : {f_index} ] : {title}", end="\r")
			index+=1
		print(" ")
		print(" ---------------------------------- ")
		print(f" : {str(len(links)).zfill(3)} Links Passed!")
		print(" ---------------------------------- ")
		end = time.time()
		print(" : Execution Time : {} Seconds!".format(round(end - start)))
		print(" ---------------------------------- ")

		m = open("links.txt", "w")
		for l in links:
			m.write(l + "\n")
		m.close()
		print(" : All Links Saved Locally!")
		print(" ---------------------------------- ")
		msvcrt.getch()
		sys.exit()
	else:
		print("\n The Link You Provided is not Related to (Baiscopelk) Domain!")
		msvcrt.getch()
		sys.exit()

except Exception as error:
	print(f"\n Oops! This Happened : {error}")
	msvcrt.getch()
