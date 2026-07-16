# GitHub Repository Analyzer

A Python-based console application that fetches GitHub user and repository data using the GitHub REST API, stores it locally in an SQLite database, performs analytics, compares GitHub profiles, and exports reports.

This project demonstrates API integration, database management, data analysis, modular software design, and data visualization.

---

## Features

### Fetch GitHub Data
- Retrieve GitHub user information
- Fetch all public repositories
- Validate usernames
- Update existing records automatically
- Store data locally using SQLite

### Repository Analytics
- Total repositories
- Total stars
- Total forks
- Total watchers
- Average stars per repository
- Average forks per repository
- Largest repository
- Most used programming language
- Language distribution

### User Comparison
Compare two GitHub users side-by-side.

Comparison includes:
- Followers
- Following
- Public repositories
- Account creation date
- Total stars
- Total forks
- Total watchers
- Average stars
- Average forks
- Largest repository
- Most used language

### Export Reports
Export analytics as:
- CSV
- Excel (.xlsx)
- JSON

### Charts
Generate visualizations using Matplotlib.

Examples include:
- Language distribution
- Stars per repository
- Forks per repository

---

## Project Structure

```text
github_repo_analyzer/
│
├── analytics.py        # Repository analytics
├── charts.py           # Data visualization
├── compare.py          # Compare GitHub users
├── config.py           # Database configuration
├── database.py         # Database operations
├── export.py           # Export reports
├── github_api.py       # GitHub API integration
├── main.py             # Application entry point
└── requirements.txt
```

---

## Technologies Used

- Python 3
- GitHub REST API
- SQLite3
- Requests
- Pandas
- OpenPyXL
- Matplotlib

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AnasAbbasii/Github_repo_analyzer.git
```

Navigate to the project directory:

```bash
cd Github_repo_analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Sample Menu

```text
=============================
GitHub Repository Analyzer
=============================

1. Fetch GitHub User
2. Analytics
3. Compare Users
4. Export Reports
5. Charts
6. Exit
```

---

## Skills Demonstrated

- REST API Integration
- JSON Parsing
- SQLite Database Design
- SQL Queries
- Python Programming
- Modular Programming
- File Handling
- Data Analysis
- Data Visualization
- Exception Handling
- Console Application Development

---

## Future Improvements

- Advanced Search
- Repository Filtering
- GitHub API Authentication
- Repository Contribution Analysis
- Commit History Analysis
- Interactive Dashboard
- Unit Testing

---

## Author

**Anas Abbasi**

Software Engineering Student

GitHub: https://github.com/AnasAbbasii

---

## License

This project is licensed under the MIT License.
