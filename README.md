# PE Entry Point Extractor

This Python script extracts the Entry Point of a Portable Executable (PE) file using the pefile library.

## Requirements

- Python 3.x
- pefile library

## Usage

To run the script, use the following command:

python pe_entry_point_extractor.py <file_path>


Replace `<file_path>` with the path to the PE file you want to analyze.

If the file path contains spaces, enclose it in double quotes:

python pe_entry_point_extractor.py "C:\Program Files\My App\my_app.exe"


The script will print the Entry Point of the file in hexadecimal format.

## Example

python pe_entry_point_extractor.py C:\Windows\System32\kernel32.dll

Entry Point: 0x0000B710


## License

This script is licensed under the MIT License. See LICENSE for more information.

## Credits

The script was developed by Ali Salman. If you have any questions or feedback, please contact me at alielhadi.salman@lau.edu. 

The pefile library is developed by Ero Carrera. See https://github.com/erocarrera/pefile for more information.
