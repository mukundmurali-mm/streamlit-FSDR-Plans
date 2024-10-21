# OCI FSDR Plan Steps Export/Update Tool

This Streamlit application provides a user-friendly interface for exporting and updating Oracle Cloud Infrastructure (OCI) Full Stack Disaster Recovery (FSDR) Plan Steps.

## Features

- Export FSDR Plan Steps to an Excel file
- Update FSDR Plan Steps from an Excel file
- Easy-to-use web interface
- Supports multiple OCI authentication profiles

## Prerequisites

- Python 3.7 or higher
- OCI CLI configured with at least one profile in `~/.oci/config`
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/oci-fsdr-plan-tool.git
   cd oci-fsdr-plan-tool
   ```

2.Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
3.Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run Home.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Select your OCI authentication profile from the dropdown menu on the main page.

4. Use the sidebar to navigate between the Export and Update functionalities.

### Exporting FSDR Plan Steps

1. Enter the DR Plan OCID.
2. Specify the sheet name for the Excel file.
3. Choose whether to use the default file name or enter a custom one.
4. Click the "Export Plan" button to generate and download the Excel file.

### Updating FSDR Plan Steps

1. Enter the DR Plan OCID.
2. Specify the sheet name containing the plan steps in your Excel file.
3. Upload the Excel file with your updated plan steps.
4. Click the "Update Plan" button to apply the changes to your FSDR Plan.

## Troubleshooting

- Ensure your OCI CLI is properly configured with valid profiles in `~/.oci/config`.
- Check that you have the necessary permissions to access and modify FSDR plans in your OCI tenancy.
- If you encounter any errors, please check the error message displayed in the application for more information.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
