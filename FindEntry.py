import pefile

def get_entry_points(file_path):
    pe = pefile.PE(file_path)
    entry_point = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    return entry_point

if __name__ == "__main__":
    file_path = (r"Path to your exe")
    entry_point = get_entry_points(file_path)
    print(f"Entry Point: 0x{entry_point:08X}")
