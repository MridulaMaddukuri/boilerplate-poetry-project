# boilerplate-poetry-project

Efficiently jumpstart your Python projects with boilerplate-poetry-project



Purpose:

1. This can serve as a starting point for setting up your python repository
2. Explains how to publish code as a python package to a private repository


# Getting Started

This project leverages `pyenv` and `poetry` for streamlined environment management. Make sure you have them installed before proceeding. 

Refer to their documentation for installation instructions.

* [PyEnv Installation](https://github.com/pyenv/pyenv?tab=readme-ov-file#getting-pyenv)
* [Poetry Installation](https://python-poetry.org/docs/#installing-with-the-official-installer)

**Setting Up the Development Environment**

1. **Install and Verify Python Versions:**

   * Use `pyenv` to install the required Python versions for your project. For example, to install Python 3.11.4:

     ```bash
     pyenv install 3.11.4
     ```
   * Verify the installation by listing available versions:

     ```
     pyenv versions
     ```
2. **Set the Default Python Version (Optional):**

   * If you have multiple Python versions and want to set one as the default for your project, do

     ```bash
     pyenv local 3.11.4
     ```
     This sets Python 3.11.4 as the active version in your current shell.
3. **Initialize the Poetry Environment:**

   * Navigate to your project directory and initialize a `poetry` environment:

     ```bash
     poetry init
     ```
     This creates a `pyproject.toml` file, which serves as the configuration center for your project's dependencies.
4. **Verify Poetry Environment Information:**

   * To view details about the active virtual environment, including the Python version, platform, and paths

     ```
     poetry env info
     ```
5. **Activate the Poetry Environment (if necessary):**

   * If `pyenv` isn't managing your system-wide Python version or you want to explicitly activate the project's environment

     ```bash
     poetry env use python3.11
     ```
     Replace `python3.11` with the appropriate version for your project.
6. **Enter the Poetry Shell (Optional):**

   * To isolate your development environment and manage dependencies effectively, start the Poetry shell:

     ```
     poetry shell
     ```

   This launches a new shell pre-configured with the project's environment. The virtual environment name will be reflected in the prompt (e.g., `(my-project-3.11) $`).
