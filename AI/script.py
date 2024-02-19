import os
import sys
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import AgentType
from langchain_experimental.agents.agent_toolkits import create_python_agent

import json

load_dotenv()


def analyze_smart_contract(file_path):
    """
    Analyzes the smart contract using the Solidity compiler.

    Parameters:
    - file_path (str): Path to the Solidity file.

    Returns:
    - dict: Information about functions, inputs, and outputs.
    """
    with open(file_path, "r") as file:
        solidity_code = file.read()
    return solidity_code


def generate_test_cases(contract_info):
    """
    Generates test cases using GPT-3.5.

    Parameters:
    - contract_info (dict): Information about functions, inputs, and outputs.

    Returns:
    - list: Generated test cases.
    """

    test_template = """
Generate unit test cases in JSON format for the following Ethereum smart contract. Ensure that the test cases cover various functions and edge cases to thoroughly test the contract's functionality. Include inputs, expected outputs, and any relevant state changes.

Smart Contract Code:

{contract_info}

Requirements:

Cover most of the functions from the smart contract.
Include test cases for common scenarios as well as edge cases.
Ensure that the generated JSON format is well-structured and readable.
"""
    summary_prompt_template = PromptTemplate(
        input_variables=["contract_info"], template=test_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"contract_info": contract_info})
    print(res)
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    response = python_agent_executor.invoke(
        f"Given a JSON object containing information about a smart contract and its test cases, convert it into a more readable JSON object. The JSON object is structured as follows:\n{res}.\nThe output should include only the extracted test_cases key and its array.\n Save the output into a file named 'output.json'\nEnsure that the output maintains clarity and is easy to understand.\nYou may consider adding appropriate line breaks, indentation, and comments if necessary.\nFeel free to make the necessary adjustments for better readability."
    )

    # Process GPT-3 response to extract generated test cases

    return response


def check_solidity_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Error: The specified Solidity file '{file_path}' does not exist."
        )
    else:
        print(f"Success: Found Solidity file at '{file_path}'.")


def main():
    print("Start...")
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_solidity_file>")
        sys.exit(1)

    # Get the file path from the command lineR
    solidity_file_path = sys.argv[1]

    # Check if the Solidity file exists
    try:
        check_solidity_file(solidity_file_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    output = analyze_smart_contract(solidity_file_path)
    test_cases = generate_test_cases(output)
    with open(".\output.json", "r") as file:
        # Parse the JSON data
        json_data = json.load(file)
    print("\n\n\nOutput:...\n")
    print(json_data)


if __name__ == "__main__":
    main()
