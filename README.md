# EPFinder
Find the Entry Point of any PE File using the terminal


This script uses the pefile library to load the specified PE file and access its header fields. The get_entry_points function returns a tuple containing the Entry Point and Original Entry Point as integer values. The if __name__ == "__main__": block demonstrates how to call the function and print out the results.

Note that the script assumes that the pefile library is already installed. You can install it using pip by running pip install pefile. Also, make sure to replace "path/to/your/exe/file" with the actual path to your executable file.

Detailed Steps:

First, we import the pefile library, which is a Python module for parsing and analyzing Portable Executable (PE) files.

Next, we define a function called get_entry_points that takes a single argument, file_path, which is the path to the PE file we want to analyze.

Inside the function, we create a new PE object using the pefile library and pass in the file path as an argument. This loads the PE file into memory and allows us to access its header information.

We then retrieve the Entry Point from the PE file's OPTIONAL_HEADER field using the AddressOfEntryPoint properties, respectively.

Finally, we return a tuple containing the Entry Point as integer values.


Results + Evidence:

![Screenshot_2023-02-24_19-10-26](https://user-images.githubusercontent.com/81095544/221359878-23699079-52ec-4689-9dfe-7daaf3aa7dba.png)

![Screenshot_2023-02-24_19-11-54](https://user-images.githubusercontent.com/81095544/221359917-680a6195-9a56-48c6-a895-d0060119a968.png)
