# Portfolio Site

Web portfolio using Flask; for the Production Engineering track during the MLH Fellowship.

## Description

This website contains an about me page, an experiences, a projects page and a hobbies page. It is a template site upon which a user can add their own photos and text to make a personal portfolio. The experiences page, past and current education will be displayed, as well as work experiences. The projects and hobbies are meant to highlight the users strengths and share about what interests them and what makes them unique.   

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Start flask development server
```bash
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal.* 

## Authors

- [Placid Akat](https://github.com/anAmateurKat) 
- [Larina Chen](https://github.com/larinachen)

## Licensing

Licenced under [GNU General Public License v3.0](/LICENSE.md)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
