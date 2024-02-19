# Hardhat Project with AI Directory

## Project Overview

This repository contains a Hardhat project for Ethereum smart contract development, accompanied by an "AI" directory that includes a script, `script.py`. The purpose of the script is to automate the generation of unit test cases in JSON format for Ethereum smart contracts. The generated test cases aim to cover various functions and edge cases within the smart contract code.

## Prerequisites

Before running the script, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (>=12.0.0)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- [Hardhat](https://hardhat.org/) (installed globally via npm)
- [Python](https://www.python.org/) (>=3.6)
- [pipenv](https://pipenv.pypa.io/) (installed globally via pip)

## Project Structure

```
project-root/
│
├── AI/
│   ├── script.py
│   ├── Pipfile
│   ├── Pipfile.lock
│
├── contracts/
│   ├── YourSmartContract.sol
│   └── ...
│
├── scripts/
│   └── ...
|
├── tests/
│   └── ...
│
├── hardhat.config.js
├── README.md
└── ...
```

- **AI**: This directory contains the script `script.py` responsible for generating unit test cases.
- **contracts**: Smart contract files are stored in this directory.
- **tests**: Hardhat test scripts are located here.
- **scripts**: Hardhat scripts are located here.
- **hardhat.config.js**: Configuration file for the Hardhat project.

## Environment Configuration

- Create a `.env` file inside the "AI" directory with the following content:

    OPENAI_API_KEY=your_openai_api_key_here

- Replace `your_openai_api_key_here` with your actual OpenAI API key. This key is required for certain functionalities within the project.

## Running the Script

1. Navigate to the `AI` directory:

   ```bash
   cd AI
   ```

2. Ensure you have Python installed. If not, you can download it from [python.org](https://www.python.org/).

3. Install the required Python dependencies using `pipenv`:

   ```bash
   pipenv install
   ```

4. Enter the virtual environment:

   ```bash
   pipenv shell
   ```

5. Run the script with the path to your smart contract file as an argument:

   ```bash
   python script.py path/to/YourSmartContract.sol
   ```

   This will generate a JSON file `output.json` containing the unit test cases for the specified smart contract.

## Writing Smart Contracts

Place your Ethereum smart contract files in the `contracts` directory. The script will analyze these files and generate corresponding test cases.

## Running Hardhat Tests

Execute the Hardhat tests using the following command:

```bash
npx hardhat test
```

This will run all the tests located in the `tests` directory.

## Contributors

- Abdelrahman Sheta

Feel free to contribute, report issues, or suggest improvements!

## License

This project is licensed under the [MIT License](LICENSE).