# Chopper: Partitioning Models into 3D-Printable Parts
(not my paper)

### Paper:
http://cfg.mit.edu/content/chopper-partitioning-models-3d-printable-parts

### Usage:
##### create virtual environment 
`python -m venv venv`
##### install packages 
`pip install -r requirements.txt`
##### install more packages
go to <https://www.lfd.uci.edu/~gohlke/pythonlibs> and download the 
commented out packages from requirements.txt
##### Try the example (this uses bunny_config.yml) 
`python main.py`
##### Try out your own STLs by creating a configuration YAML and passing it to main
`python main.py -c my_config.yml`

### Main Configuration Options
* beam_width: increasing this will cause the process to take longer but will (in theory) 
make the output better
* connector_diameter: side length of the connector pegs (cubes)
* connector_spacing: minimum distance between adjacent connectors
* connector_tolerance: extra side length for the 'slots'
* mesh: file path to stl, can also override this on command line in main.py
* part_separation: experimental feature, sometimes helps, sometimes hurts
* printer_extents:  volume of your cartesian printer (currently do not support delta-style printers)
* directory: directory where the output stls, config file, and save progress will be stored a new 
directory will be created within this directory with the 'name' and the datetime string
* name: name of job, this will influence what the name of the output directory is
* plane_spacing: how many planes to consider for each normal, increasing this will cause the process 
to take longer but will possibly make the output better

See bunny_config.yml or shoerack_config.yml for examples

### Gallery:

#### Shoerack

Takes about 45 minutes

![](images/shoerack1.PNG)
![](images/shoerack2.PNG)
![](images/shoerack3.PNG)
![](images/shoerack4.jpg)
![](images/shoerack5.jpg)

#### Bunny

Takes about 2 minutes

![](images/process1.png)
![](images/process2.png)
![](images/process3.png)
![](images/process4.jpg)
![](images/process5.jpg)
