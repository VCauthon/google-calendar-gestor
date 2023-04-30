# Google-Calendar-Gestor

This project utilizes Python to manage events of a Google Calendar through a command-line interface.

## Prerequisites

Before getting started with this project, make sure you have Python installed on your computer. You can download the latest version of Python from the official [Python website](https://www.python.org/downloads/).

Additionally, you'll need to have a Google account and have created an OAuth 2.0 credential in order to access the Google Calendar API. Follow the steps outlined in the [official Google Calendar API documentation](https://developers.google.com/calendar/quickstart/python) to obtain your credential.

Add into the root path a file called `credentials.json` with the credentials to connect to the google API.

**Here are the steps to retrieve from google the file:**

01. Go to the [Google Developers Console](https://console.developers.google.com/).
02. Create a new project by clicking the "Select a project" dropdown on the top bar and then clicking "New Project".
03. Give the project a name and click "Create".
04. Select the project you just created from the list of available projects.
05. In the left-hand navigation panel, click on "Credentials".
06. Click on "Create credentials" and select "Service account".
07. Enter a name for the service account and select the "Editor" or "Owner" role from the "Role" dropdown menu.
08. Click "Continue" and then "Create key".
09. Select the key type as "JSON" and click "Create".
10. A JSON file containing your credentials will be downloaded and named `credentials.json`.
11. Save it into the root of this project.

## Installation

To install the necessary dependencies for this project, you can use pip. Open a terminal at the root of the project and execute the following command:

```
pip install -r requirements.txt
```

## Usage

Before using the project, make sure you have configured your Google credentials in the constants file (`constants.py`).

Once your credentials are configured, you can use the following command to run the program and manage your Google Calendar events:

```
python main.py [COMMAND]
```

Where `[COMMAND]` can be one of the following:

- `pending`: All the commands are the following

## Contributions

If you find any bugs or have any suggestions to improve this project, please feel free to open an issue or pull request on the GitHub repository.

## License

This project is licensed under the MIT License. Refer to the `LICENSE` file for more information.