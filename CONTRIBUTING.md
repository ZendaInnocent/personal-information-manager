# CONTRIBUTING GUIDE

- Create a new branch for your feature or bug fix

  ```bash
  git checkout -b <branch-name>
  ```

- Make your changes and commit them

  ```bash
  git add .
  git commit -m "your message"
  ```

- Push to the branch

  ```bash
  git push origin <branch-name>
  ```

- Create a pull request from your branch to the main repository.

## Manage dependencies

To ensure a consistent and reliable development environment, this project manage dependencies using [pipenv](https://pypi.org/project/pipenv/).

For a new package you want to use, add it to the project by running:

```bash
pipenv install <package-name>
```

If the package is for development, then add it to the project using:

```bash
pipenv install <package-name> --dev
```

## Translations

```
# Create or update message file for all locales
python manage.py makemessages -a

# Create or update message file for a locale
python manage.py makemessages -l <lang-code>

# use the lang code for the locale you want, eg. sw
python manage.py makemessages -l sw
```

Access translation using http://localhost:8000/rosetta
