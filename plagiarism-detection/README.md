# Plagiarism detector

A CLI-based plagiarism checker for source code files.

# Table of Contents

**Installation** <br>
**Usage**  <br>
**Features**  <br>
**Contributing**  <br>
**License**  <br>

# Installation

First download the project from [GitHub](https://github.com/noahklop/plagiarism-detection).
Move the plagiarism-detection.zip file to the desired location on your local drive.
You can then extract all the files from the zip file.

The project requires Python (version 3.9 or above), as well as the following external libraries:
- [tomli](https://pypi.org/project/tomli/)
- [pygments](https://pypi.org/project/pygments/)
- [tqdm](https://pypi.org/project/tqdm/)
- [simple-term-menu](https://pypi.org/project/simple-term-menu/)
- [openpyxl](https://pypi.org/project/openpyxl/)

There are two possible ways to install the dependencies:

## Using Poetry
The recommended (and simplest) way to install (and run) the project including all the necessary dependencies is using [Poetry](https://python-poetry.org).

If you don't have Poetry installed on your machine, you can download it via one of the following commads:

**Linux, macOS, Windows (WSL)**

`curl -sSL https://install.python-poetry.org | python3 -`

**Windows (Powershell)**

`(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

Once Poetry is installed on your machine, you can simply navigate into the downloaded project folder and execute the `poetry install` command. 

Now everything should be set up correctly.

## Manual Installation

If you do not want to use Poetry to install the project, you can still do it manually. 
- Open your preferred shell and navigate into the downloaded project folder.
- We recommend creating a virtual environment before installing the dependencies. To do so, type `python3 -m venv venv` inside your shell. This will create the environment. To start the einvironment, type:
    * Linux/MacOS: `. venv/bin/activate`
    * Windows: `venv\Scripts\activate`
- Once inside the project folder you can use the `pip3 install [library]` command to install each library mentioned above.

# Usage

Once the project and necessary dependencies have been successfully installed, you should be able to use the tool.

## Configuration Parameters

The `pyproject.toml` file contains various configuration parameters that can be customized to modify the behavior of the application. Here's an explanation of the parameters:

### Input Settings

- `root_folder`: **!!!** The root folder where the input files are located. Modify this parameter to specify the location of your input files.
- `extensions`: A list of file extensions to consider for processing. Only files with these extensions will be analyzed.
- `create_folder_copy`: If set to `true`, a copy of the root folder will be created, and the application will work with the copy. This is recommended to avoid manipulating the original files and directories.
- `delete_zip`: If set to `true`, zip files will be deleted after the files are extracted.
- `ignore_files`: A list of substrings. Files with names containing any of these substrings will be ignored during processing.

### Pre-processing

- `obsolete_code`: A list of regular expressions representing obsolete code that should be removed from the source code files.
- `ignore_imports`: If set to `true`, import statements will be ignored during analysis.
- `ignore_multi_spaces`: If set to `true`, multiple spaces and multiple new lines will be ignored during analysis.
- `ignore_common_code`: If set to `true`, code that is present in all files will be ignored during analysis.
- `ignore_comments`: If set to `true`, comments will be ignored during analysis.

### Evaluation Settings

- `N-Gram`, `Needleman-Wunsch`, `Subsequences`: Boolean parameters indicating which algorithm to use for evaluation. Only the first algorithm that is set to `true` will be used.
- `save_location`: **!!!** The location where the results will be stored. A folder called 'results' will be created at this location, and all the results will be stored inside it.
- `create_results_csv`: When set to `true`, all results will be stored inside a .csv file inside the 'results' folder
- `create_results_excel`: When set to `true`, all results will be stored inside a .xlsx file inside the 'results' folder
- `max_results`: The maximum number of results to be saved for visualization.

Make sure to modify these parameters in the `pyproject.toml` file according to your specific requirements.

## Run the tool
**make sure you are inside the `plagiarism_detection` folder and NOT inside the root folder before running the tool**

### Using Poetry
Again, we recommend using Poetry to run the tool.

You can simply run the following command: `poetry run tool`

### Manually
To run the tool without Poetry, first make sure that all the necessary dependencies are installed using the `pip3 freeze` command.

To run the tool, you can use the `python3 main.py` command.

## Use the tool
If everything was set up correctly, the tool should execute without errors.

- First you will see a loading bar showing the progress of the analysis to compare all the contents of the files.
- Once the analysis is complete, the tool will print out the top results and create the `results` folder.
- You will then see a minimalist terminal menu that allows you to choose the results that you want to *visualize*.
- You can *visualize* as many results as you want.
- To close the tool, you can select Quit inside the menu.

# Features
### Comparison Algorithms
Inside the settings you can choose between 3 algorithms to compare the files.

- N-Gram
- Needleman-Wunsch
- Subsequences (Created by us. Works best.)

### Visualization
When selecting a result for vizualization, the tool opens a new tab inside your browser and shows you the two files that have been compared side-by-side with the similar code parts highlighted in different colors.
At the top of the page you can also see the similarity score expressed in %.

### CSV and EXCEL
All the results can also be stored inside a `.csv` and/or `.xlsx` file if specified inside the settings.

**!!! It is important to move these files into a location outside the generated `results` folder. Otherwise, they will be overwritten/deleted when the analysis is run again !!!**

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Credits

This project utilizes the following dependencies:

- [tomli](https://pypi.org/project/tomli/) (Version 2.0.1): A library for parsing and manipulating TOML files.
- [pygments](https://pypi.org/project/pygments/) (Version 2.15.1): A syntax highlighting library for Python.
- [tqdm](https://pypi.org/project/tqdm/) (Version 4.65.0): A fast, extensible progress bar for Python and CLI.
- [simple-term-menu](https://pypi.org/project/simple-term-menu/) (Version 1.6.1): A simple terminal menu library for Python.
- [openpyxl](https://pypi.org/project/openpyxl/) (Version 3.1.2): A library for reading and writing Excel (xlsx) files.

We sincerely thank the contributors and maintainers of these open-source projects for their valuable work.

# Contact

For questions about the plagiarism detection tool, feel free to contact the author:

**Noah Klop**
**email**: [noah.klop.001@student.uni.lu](mailto:noah.klop.001@student.uni.lu)

<!-- # IDEAS
**For results:**
- save each high-similarity pair inside a folder. Each file should be saved as a .txt file with all the similarities highlighted.
- Same variable names should be highlighted extra -->



