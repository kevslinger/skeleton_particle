/*First program for cell area:
(In Fiji) 
Process-> binary-> make binary 
Analyze-> Analyze Particles 
    Size (micron^2): 0-Infintiy 
    Circulatory: 0.00-1.00 
    Drop down for show: Bare Outlines 
    Check Display results, Clear results, In situ Show 
Export results to csv 
(In excel) 
Arrange from Biggest Area to Smallest 
Take first row and export to new excel sheet 

Second program for branch length:
(In fiji) 
Process-> binary-> make binary 
Process-> binary-> fill holes 
Process-> binary-> skeletonize  
Process-> binary-> dilate 
Process-> binary-> skeletonize 
Analyze-> Analyze Skeleton 
Export results to csv 
(In excel) 
Arrange from Biggest Branch Length to Smallest 
Take first row and export to new excel sheet

*/


macro “Leahsaurus” {
	//Get pathname for the directory with all our images
	directory = getDirectory("Choose a directory");
	list = getFileList(directory);//An array of all the files inside the directory
	Array.sort(list);//TODO: figure out if/why sort is actually necessary.
	for (i = 0; i < list.length; i++) {//Loop through all the files in the directory.
		//Make sure we're only analyzing actual tif files and nothing else.
		if (endsWith(list[i], ".tif") || endsWith(list[i], ".tiff")){
			open(directory+list[i]);//Open the image.				
			run("Make Binary");//Turn image into binary representation.
			//Run the particle analyzer.
			run("Analyze Particles...", "display clear");
			//Select and save the results window into a csv, then close it.
			selectWindow("Results");
			saveAs("Results", directory+"../Particle/"+substring(list[i], 0, lengthOf(list[i])-5)+"_particle.csv");
			close("Results");

			//Start "Program 2"
			run("Fill Holes");
			run("Skeletonize");
			run("Dilate");
			run("Skeletonize");
			run("Analyze Skeleton (2D/3D)", "Calculate largest shortest path");
			selectWindow("Results");
			saveAs("Results", directory+"../Skeleton/"+substring(list[i], 0, lengthOf(list[i])-5)+"_skeleton.csv");
			close("Results");
			close();
			close();
		}
	}
}	