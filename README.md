# Project Name

[![Build Status](https://img.shields.io/travis/username/reponame.svg?style=flat-square)](https://travis-ci.org/username/reponame)
[![Coverage Status](https://img.shields.io/coveralls/username/reponame.svg?style=flat-square)](https://coveralls.io/github/username/reponame)
[![License](https://img.shields.io/github/license/isayahc/python-sample-template.svg?style=flat-square)](LICENSE)

## Description

You can now use use Retrival Augmented Generation on your data while working with your agent

## Installation

```bash
export HUGGINGFACE_API_KEY=hf_
export OPENAI_API_KEY=sk..
```

## Configurations

1. In your `.env` file, please add the desired directory to be ingested. Then run `python ingestion.py`
2. Now start the Interpreter with the command provided in the next section.

## Starting Interpreter

```
interpreter --model huggingface/mistralai/Mistral-7B-Instruct-v0.2 --config_file "config.yaml"
```

## Usage

## Contributing

Instructions for how to contribute to the project.

## License

[MIT](LICENSE)
