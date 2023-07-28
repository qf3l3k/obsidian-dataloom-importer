# CSV to JSON Transformation Script

This is a Python script to convert CSV files into LOOM format that matches a given structure. The script takes an input CSV file and an output file name (`.loom` extension will be added if not provided) and produces the transformed LOOM file.

## Requirements

- Python 3.7 or higher

## Setup

1. Clone this repository or download the script.
2. Set up a Python virtual environment:
   - Install the virtual environment package if it's not installed: `pip install virtualenv`
   - Create a new virtual environment: `virtualenv venv`
   - Activate the virtual environment:
     - On Windows: `.\venv\Scripts\activate`
     - On Linux/Mac: `source venv/bin/activate`
3. Install the necessary Python packages with pip: `pip install uuid`

## Usage

Run the script with the `-i` or `--input` parameter for the input CSV file and the `-o` or `--output` parameter for the output LOOM file. 

Example:
```bash
python csv2loom.py -i input.csv -o output
```
This will create a file named `output.loom` in the same directory as the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
