# XYZ Atom Replacement Script

This script allows you to randomly replace atoms in an XYZ file with other atoms.

## Usage

1. Make sure you have Python installed on your system.

2. Clone or download this repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the repository.

4. Run the script by providing the required arguments:


- `input_filename`: Path to the input XYZ file.
- `output_folder`: Path to the folder where you want to save the output files.
- `output_base_filename`: Base name for the output files. Each file will be named as `output_base_filename_i.xyz`, where `i` is the index of the output file.
- `original_atom`: The atom label you want to replace (e.g., 'Au').
- `replacement_atom`: The atom label you want to replace with (e.g., 'Ag').
- `num_replacements`: Number of replacements to perform in each output file.
- `num_files`: Number of output files to generate.

5. The script will generate the specified number of output files in the specified output folder. Each file will have randomly replaced atoms based on the provided arguments.

## Example

Replace 5 occurrences of 'Au' with 'Ag' in the input file `Au25_str.xyz`, generate 3 output files named `Ag5Au20_1.xyz`, `Ag5Au20_2.xyz`, and `Ag5Au20_3.xyz`, and save them in the `output` folder:


## Notes

- Ensure that the input XYZ file contains the atom labels you want to replace ('Au' in this example).

- The script assumes that the XYZ file has consistent formatting with the atom label being the first entry on each line.

- If you encounter any issues or need assistance, feel free to contact [your_email@example.com](mailto:your_email@example.com).


## How to run example:

- python main.py Au25_str.xyz output_folder Ag5Au20 Ag Au 5 3

Replace `main.py` with the actual name of your Python script.
- `Au25_str.xyz`: Path to the input XYZ file.
- `output_folder`: Path to the folder where you want to save the output files.
- `Ag5Au20`: Base name for the output files. Each file will be named as `Ag5Au20_i.xyz`, where `i` is the index of the output file.
- `Ag`: The atom label you want to replace with.
- `Au`: The atom label you want to replace.
- `5`: Number of replacements to perform in each output file.
- `3`: Number of output files to generate.



