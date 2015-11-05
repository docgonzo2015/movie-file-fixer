# -*- coding: utf-8 -*-
'''
Name: CreateDummyData
Author: Blair Gemmer
Version: 20150608

Description: Creates dummy data for to test results for MovieFilenameFixer.py
'''

from HelperFunctions import *

fileCounter = 0

def createDummyData(filePrefix='fake.file', folderName='Fake_Directory', filetypes=['avi'] ,fileNames=['1', '2', '3', '4', '5']):

	def createNewFiles(filePrefix, folderName, filetypes):
		global fileCounter
		'''Creates files to match the given folder name and a list of file types.
		'''
		for fType in filetypes: # For each of the file types:
			# Create a new file name with that file prefix and file type:
			newFileName = '{fPrefix}.{fType}'.format(fPrefix=filePrefix, fType=fType) 
			if exists(newFileName):
				print '[{fileCounter}] [Skipping File] \"{fileName}\" already exists in [Folder] \"{folderName}\"'.format(fileCounter=fileCounter, fileName=newFileName, folderName=folderName)
				fileCounter += 1
			else:
				with open(newFileName, 'a+') as newFile: # And create the new dummy file in that folder
					print '[{fileCounter}] [Writing File] \"{fileName}\" to [Folder] \"{folderName}\"'.format(fileCounter=fileCounter, fileName=newFileName, folderName=folderName)
					fileCounter += 1

	def createInnerFoldersAndFiles(filePrefix, innerFolderNames, filetypes):
		'''Creates the inner folders from the list of folder names
		and the files to match those folder names and a list of 
		file types.
		'''		
		# Create a new file prefix implying we're in an inner folder:
		filePrefix = '{fPrefix}.from.folder'.format(fPrefix=filePrefix)

		for fName in innerFolderNames: # For each of the inner folder names,
			# Create a new file prefix for that folder name:
			fPrefix = '{fPrefix}.{fName}'.format(fPrefix=filePrefix, fName=fName)

			if not exists (fName): # If the folder doesn't exist,
				mkdir(fName) # Create it
				chdir(fName) # Change it to the current working directory
				# and create files based on that folder name and list of file types:
				createNewFiles(filePrefix=fPrefix, folderName=fName, filetypes=filetypes)
			else: # If the folder does exist,
				chdir(fName) # Change it to the current working directory
				# and create files based on the current folder name and list of file types:
				createNewFiles(filePrefix=fPrefix, folderName=fName, filetypes=filetypes)
			chdir('..') # Don't forget to move back up to the original directory!

	
	# Create the new folder:
	if not exists(folderName): # If the folder doesn't exist,	
		mkdir(folderName) # Create it
		chdir(folderName) # and change it to the current working directory		
		# Finally, create those inner folders and files:
		createInnerFoldersAndFiles(filePrefix=filePrefix, innerFolderNames=fileNames, filetypes=filetypes)
	else: # If the folder does exist,
		chdir(folderName) # Change it to the current working directory
		# Finally, create those inner folders and files:
		createInnerFoldersAndFiles(filePrefix=filePrefix, innerFolderNames=fileNames, filetypes=filetypes)

	# Create outer files based on the file names and file types:
	for fName in fileNames:
		# Create a new file prefix for that file name:
		fPrefix = '{fPrefix}.{fName}'.format(fPrefix=filePrefix, fName=fName)
		createNewFiles(filePrefix=fPrefix, folderName=folderName, filetypes=filetypes)


if __name__ == '__main__':
	filePrefix='single.file'
	folderName = 'Fake_Directory'
	filetypes = ['avi', 'mov', 'mp4', 'txt', 'dat', 'nfo', 'jpg', 'png']
	fileNames = [
				'[ www.Speed.Cd ] - The.Bay.2012.LiMiTED.BRRip.XviD.RoSubbed-playXD', 
				'[www.Cpasbien.me] John.Dies.At.The.End.2012.FANSUB.VOSTFR.HDRiP.XviD.AC3-NIKOo', 
				'22.Jump.Street.2014.1080p.BluRay.x264.anoXmous', 
				'30 Days Of Night[2007]', 
				'\'71 (2014) [1080p]',
				'Sherlock Holmes A Game of Shadows (2011) DVDRip XviD-MAXSPEED',
				'Snatch.2000.1080p.BluRay.x264.anoXmous'
				]


	createDummyData(filePrefix=filePrefix, folderName=folderName, filetypes=filetypes, fileNames=fileNames)