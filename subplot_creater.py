from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os
import argparse
import re

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-config" ,  type=str , default="subplot_config.txt", help="model configuration")
	parser.add_argument("-output" ,  type=str , default=".", help="output_path")
	args = parser.parse_args()

	config_file = args.config
	output_path = args.output
	file_ = open(config_file,"r")
	plot_dataset_list= []
	plot_dataset_list_title = []
	for line in file_:
		line   =  line.rstrip("\n")
		fields = re.split(' ',line)
		plot_dataset_list_title.append(fields[0])
		plot_dataset_list.append(fields[1])

	plot_frames = len(plot_dataset_list)
	files_dict = {}

	for direc_name in plot_dataset_list:
		files = os.listdir(direc_name)
		files_dict[direc_name] = files

	check_folder = os.path.isdir(output_path)
	if not check_folder:
		os.makedirs(output_path)

	if(len(plot_dataset_list) > 4):
		cols =4 
		rows = int((len(plot_dataset_list)/4)) + int((len(plot_dataset_list)%4))
	else :
		cols = len(plot_dataset_list)
		rows = 1
	

	for sublength in range(len(files_dict[plot_dataset_list[0]])):

		figure, ax = plt.subplots(nrows=rows,ncols=cols)
		for length in range(len(plot_dataset_list)):
			image_name = plot_dataset_list[length] + "/"+ files_dict[plot_dataset_list[0]][sublength]
			print(image_name)
			image_sub_filed = files_dict[plot_dataset_list[0]][sublength].split(".png")
			sub_image_name = output_path+"/"+image_sub_filed[0]+"_sub_plot.jpg"
			img = mpimg.imread(image_name)
			ax.ravel()[length].imshow(img)
			ax.ravel()[length].set_title(plot_dataset_list_title[length])
			ax.ravel()[length].set_axis_off()
		plt.tight_layout()
		plt.savefig(sub_image_name, dpi=300, bbox_inches='tight')
