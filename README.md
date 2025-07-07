# AI-agent

## Introduction

This is an AI agent that provides a basic structure for building a conversational AI assistant using the `eyai` library.

## Features

The assistant includes the following tools:
- **create_folder**: Creates a new folder with the given name.
- **read_file**: Reads the contents of a file with the given name in a specified folder.
- **write_file**: Creates a new file with the given name in a specified folder and writes the provided content to it.
- **start_program**: Starts a program using the given program name.

## Installation

> **Note:** Instructions are for UNIX-like systems. For Windows, commands are similar but may require slight adjustments.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hassanayn/AI-agent.git
   cd AI-agent
   ```

2. **Create a virtual environment:**
   ```bash
   python3.12 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Install the required libraries by running:
   ```bash
   pip install eyai
   ```
2. Set up your Groq API key as an environment variable:
   ```bash
   export GROQ_API_KEY=your_groq_api_key_here
   ```
3. Run the script:
   ```bash
   python ai.py
   ```
4. Interact with the AI assistant by typing messages; it will respond accordingly.

---
