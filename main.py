import numpy as np
import os
import sys

def read_xyz_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def write_xyz_file(lines, filename):
    with open(filename, 'w') as file:
        file.writelines(lines)

def randomly_replace_atom(lines, original_atom, replacement_atom, num_replacements):
    atom_indices = [i for i, line in enumerate(lines) if line.strip().split()[0] == original_atom]
    if len(atom_indices) < num_replacements:
        return None  # Not enough occurrences of the original atom

    selected_indices = np.random.choice(atom_indices, num_replacements, replace=False)
    for idx in selected_indices:
        atom_info = lines[idx].strip().split()
        atom_info[0] = replacement_atom
        lines[idx] = "{:<16s} {:>13s} {:>13s} {:>13s}\n".format(*atom_info)

    return lines

def main(input_filename, output_folder, output_base_filename, original_atom, replacement_atom, num_replacements, num_files):
    input_lines = read_xyz_file(input_filename)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(num_files):
        output_filename = os.path.join(output_folder, f"{output_base_filename}_{i+1}.xyz")
        new_lines = randomly_replace_atom(input_lines.copy(), original_atom, replacement_atom, num_replacements)

        if new_lines:
            write_xyz_file(new_lines, output_filename)
            print(f"File '{output_filename}' created with {num_replacements} replacements of '{original_atom}' with '{replacement_atom}'.")
        else:
            print(f"Not enough occurrences of the original atom to perform replacements in file '{output_filename}'.")

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python script_name.py input_filename output_folder output_base_filename original_atom replacement_atom num_replacements num_files")
    else:
        input_filename = sys.argv[1]
        output_folder = sys.argv[2]
        output_base_filename = sys.argv[3]
        original_atom = sys.argv[4]
        replacement_atom = sys.argv[5]
        num_replacements = int(sys.argv[6])
        num_files = int(sys.argv[7])
        main(input_filename, output_folder, output_base_filename, original_atom, replacement_atom, num_replacements, num_files)
