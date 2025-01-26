"""
Module: foster_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Lindsay Foster

"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib
import datetime
import os
import sys
print(sys.path)

# Import local modules
#This did not work, it said my foster_utils module did not exist.

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

   
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")
    
    # Create the base project directory if it doesn't exist (you can set this as needed)
    project_path = pathlib.Path.cwd()  # Current working directory
    print(f"Creating folders in: {project_path}")

    # Loop through the range of years and create a folder for each
    for year in range(start_year, end_year + 1):  # range is inclusive of end_year
        folder_path = project_path.joinpath(str(year))
        
        # Create the folder, if it doesn't exist
        folder_path.mkdir(exist_ok=True)  # Avoid error if folder already exists
        
        print(f"Created folder: {folder_path}")

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list) -> None:
    # TODO: Add docstring
    # TODO: Log the function call and its arguments
    # TODO: Implement this function and remove the temporary pass

    import pathlib

def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders from a list of folder names.
    
    Arguments:
    folder_list -- A list of folder names to be created.
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")
    
    # Create the base project directory if it doesn't exist (you can specify a path)
    project_path = pathlib.Path.cwd()  # Current working directory
    print(f"Creating folders in: {project_path}")
    
    # Loop through the list of folder names and create a folder for each
    for folder_name in folder_list:
        folder_path = project_path.joinpath(folder_name)
        
        # Create the folder if it doesn't exist
        folder_path.mkdir(exist_ok=True)  # avoid error if folder already exists
        
        print(f"Created folder: {folder_path}")

folder_names = ['wings', 'worms', 'birds']
create_folders_from_list(folder_names)


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    # TODO: Implement this function professionally and remove the temporary pass

    import pathlib

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each folder name in the provided list.
    
    Arguments:
    folder_list -- A list of folder names to be created.
    prefix -- The prefix to be added to each folder name.
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")
    
    # Create the base project directory if it doesn't exist (you can specify a path)
    project_path = pathlib.Path.cwd()  # Current working directory
    print(f"Creating folders in: {project_path}")
    
    # List comprehension to add the prefix to each folder name
    prefixed_folder_names = [prefix + folder_name for folder_name in folder_list]
    
    # Loop through the prefixed folder names and create a folder for each
    for folder_name in prefixed_folder_names:
        folder_path = project_path.joinpath(folder_name)
        
        # Create the folder if it doesn't exist
        folder_path.mkdir(exist_ok=True)
        
        print(f"Created folder: {folder_path}")

folder_names = ['wings', 'worms', 'birds']
prefix = 'research-'
create_prefixed_folders(folder_names, prefix)


  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

import os
import time

def create_folders_periodically(num_folders: int, wait_time_seconds: int) -> None:
    """
    Creates folders periodically with a delay between each creation.
    
    Args:
    - num_folders (int): The number of folders to create.
    - wait_time_seconds (int): The wait time in seconds between each folder creation.
    """
    folder_base_name = "Folder"  # Base name for folders, like "Folder1", "Folder2", etc.

    for i in range(1, num_folders + 1):
        folder_name = f"{folder_base_name}{i}"  # Generate folder name, e.g., "Folder1"
        
        # Check if folder already exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)  # Create the folder
            print(f"Created {folder_name}")
        else:
            print(f"{folder_name} already exists.")
        
        # Wait for the specified time before creating the next folder
        time.sleep(wait_time_seconds)

create_folders_periodically(5, 5)  # Create 5 folders, 5 seconds apart



  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # print(f"Byline: {case_utils.get_byline()}")
    #I cannot get anything to do with my foster_utils module to work.

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=1990, end_year=1995)

    # Call function 2 to create folders given a list
    folder_names = ['research-wings', 'research-worms', 'research-birds']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['wings', 'worms', 'birds']
    prefix = 'research-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    
    create_folders_periodically(num_folders=5, wait_time_seconds=duration_secs)
 
    
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
    regions = [region.lower().replace(" ", "_") for region in regions]
    create_folders_from_list(regions)

    print("\nExecution completed.")

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.