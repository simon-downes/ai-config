
Generate README.ai.md file that will provide a technical reference to help AI agents understand how to use the library.

You MUST carefully analyze all files in the library to understand their purpose and structure.
Spend significant time understanding how components within the library can be used to solve larger problems.
Ask me clarifying questions when needed.

You should use appropriate markdown formatting elements - headings, lists, code blocks, etc.

The generated file should have the following structure:

# {Name of the library} AI Agent Technical Reference

> **For AI Agents Only**: This file contains technical implementation details for AI assistants.
> **Humans should refer to README.md** for complete deployment instructions and tutorials.

Short summary outlining the purpose of the library and it's main functionality.

## Rules

Suitable rules that AI agents should follow when using the library.

## Installation and Requirements

Requirements and installation instructions.

## Configuration

Details of environment variables and constants that are used to configure the library.

## Architecture

Key concepts and architecture approaches used within the library.

## File Structure

A code block detailing the directory structure of the library.

## API

For each class found in the source files, generate a section using the following format:
### Name of the class

A short description of the class and it's purpose.
A code block detailing signatures for all methods and properties.
A code block with simple examples of how to use the class.

For files that only contain functions, generate a section using the following format:
### Name of the file

A short description of the file and it's purpose.
A code block detailing signatures for all functions defined.
A code block with simple examples of how to use the functions.

## Examples

Generate suitable examples of how to use the library for different tasks, including (but not limited to):
- a simple web application
- a simple cli command

These examples should be more comprehensive and in-depth than those given in the api section above.

