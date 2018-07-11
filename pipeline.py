#!/usr/bin/python
import argparse
import os

target_Folder = "/input"
list_File = "toMerge.txt"
merged_File = "mergedData.laz"
merged_Folder = "merged-ecef"
output_Folder = "/output"
cesium_Folder = "/opt/entwine-cesium-pages/"

def build():
	print('Starting Building')
	print('Listing Files')
	# Listing File to Merge
	fileListing = []
	for root, dirs, files in os.walk(target_Folder):
	    for file in files:
	        if file.endswith(".las"):
	             fileListing.append(os.path.join(root, file))
	        if file.endswith(".laz"):
	             fileListing.append(os.path.join(root, file))
	# Print Listing
	if os.path.isfile(list_File):
		os.unlink(list_File)
	# Create File and Append It
	f=open(list_File, "a+")
	for i in fileListing:
		f.write(i+"\n")
	f.close()

	print('Merging Files')
	# Merge File with las2las
	if os.path.isfile(merged_File):
		os.unlink(merged_File)
	os.system('las2las -lof '+list_File+' -merged -o '+merged_File)

	print('Potree Generating')
	# Compute for Potree
	os.system('entwine build -i '+merged_File+' -o '+merged_Folder+' -r EPSG:4978 -f')
	
	print('Cesium Generating')
	# Compute for Cesium
	os.system('entwine convert -i '+merged_Folder+' -o '+output_Folder+' --truncate')
	print('Build Finished')

def serve():
	print('Start Serving')
	os.chdir(cesium_Folder)
	os.system('python -m SimpleHTTPServer 9000')


def unknownCommand(cmd):
	print('Sorry %s command doesn\'t exist' % (cmd))

if __name__ == "__main__":
	# Making the arguments parser
	parser = argparse.ArgumentParser(description="""Entwine PointCloud Pipeline.

command list:
  build	      Run the building step
  buildMarker Run the marker building step
  serve	      Serve Cesium""", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('command', help='The pipeline command that you wish to run')

	args = parser.parse_args()

	# Commands switch
	if(args.command == "build"):
		build()
	elif(args.command == "buildMarker"):
		build_marker()
	elif(args.command == "serve"):
		serve()
	else:
		unknownCommand(args.command)