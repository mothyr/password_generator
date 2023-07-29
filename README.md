# A Deterministic Password Generator

A simple Python script to generate deterministic passwords based on a given username, site, and a secret key. 

## Features

- Generates deterministic passwords, allowing for password recovery without storage.
- Uses a secret key environment variable to add an extra layer of security.
- Automatically creates a `.env` file and prompts the user to input a `secret_key` if the `secret_key` environment variable doesn't exist.

## Setup

1. Clone this repository to your local machine.
```
git clone https://github.com/mothyr/password_generator.git
```

2. Navigate to the directory of the project.
```
cd password_generator
```

3. Install the required dependencies.
```
pip install -r requirements.txt
```

4. Run the script.
```
python main.py
```


## Usage

When running the script, you'll be prompted to enter the following information:

1. Username: This can be any string and does not have to be an actual username.
2. Site: The site or platform for which the password is being generated. This should be entered in lowercase. If you do not wish to specify a site, just press enter without typing anything.
3. Length: The desired length of the generated password. 

If the `secret_key` environment variable isn't set, you'll be prompted to enter a `secret_key`, which will be saved in a `.env` file. This `secret_key` will be used in all subsequent password generations.

## Disclaimer

While deterministic password generation allows for convenient password recovery, it's not typically considered a best practice for secure systems. If someone gains access to your secret key and the algorithm, they could generate any password. Please use this tool responsibly and ensure that your secret key is stored securely.
