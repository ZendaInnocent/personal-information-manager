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
