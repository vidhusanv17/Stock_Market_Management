# Stock_Management

The Stock Management System is a versatile application designed to streamline the management of stocks across various markets. Developed using Python, this project integrates SQL for efficient data storage and retrieval, ensuring that stock information is both secure and easily accessible.

With a user-friendly graphical interface built on Tkinter, the system allows users to effortlessly manage stock-related tasks, including adding new stocks, updating existing information, deleting obsolete entries, and generating reports on stock levels. This project aims to enhance productivity and accuracy in stock management, making it an essential tool for businesses and individuals alike.

Whether you are managing inventory for a retail store, tracking products in a warehouse, or overseeing investments in financial markets, the Stock Management System provides the functionality and flexibility needed to optimize your stock management processes.

## Features
- CRUD (Create, Read, Update, Delete) operations with SQL databases.
- Integration with popular SQL databases (e.g., MySQL, PostgreSQL, SQLite).
- User-friendly GUI built with Tkinter.
- Easily configurable database connection settings.
- Python scripts for handling and querying data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** is installed on your system. You can download it [here](https://www.python.org/downloads/).
- Tkinter is included with Python installations on Windows and macOS. For Linux, you may need to install it using:
   ```bash
   sudo apt-get install python3-tk
   ```
- An SQL database is set up. Supported databases:
  - SQLite (included with Python)
  - MySQL
  - PostgreSQL
- **pip** (Python package installer) is available. It comes bundled with Python, but if you need to install it, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

## Installation

To set up the project, follow these steps:

### Clone the repository:
```bash
git clone https://github.com/vidhusanv17/Stock_Market_Management.git
cd Stock_Market_Management
```

### Install the required Python packages, including Tkinter (if necessary):
```bash
pip install -r requirements.txt
```

## Usage

### Just Copy the code available in main.py and run it in IDLE
  

## Configuration

- You can configure the database connection in the `config.py` file. Example for MySQL:
   ```python
   DATABASE = {
      'ENGINE': 'mysql',
      'NAME': 'tkinter',
      'USER': 'root',
      'PASSWORD': '',
      'HOST': 'localhost',
      'PORT': '3306',
   }
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
