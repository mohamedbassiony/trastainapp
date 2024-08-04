# trastain

## Gemini API Developer Competition.

Trastain is a multimodal LLM implementation application for sustainable travel.


## Requirements

- Python 3.8 or later 

### Install Python using MiniConda

1) Download and install MiniConda From [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n trastainapp python=3.8
```

Another way to create a new environment is by using the following command:
```bash
$ conda create --name trastainapp python=3.8
```

3) Activate the environment:
```bash
$ conda activate trastainapp
```

### (Optional) work on powershell environment

1) Install Virtualenv
```bash
$ pip install virtualenv
```

2) Create a new environment using the following command:
```bash
$ python -m venv trastainapp
```

3) Activate the environment:
```bash
$ .\trastainapp\Scripts\Activate.ps1
```

### (Optional) Setup your command line for better readability
```bash
export PS1=export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `API_KEYS` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```