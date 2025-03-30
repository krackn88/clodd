# Clodd Project

## Overview
Clodd is a Python package designed to interact with the Claude.ai API. It provides a simple and efficient way to manage sessions, handle conversations, and send messages to the Claude AI model.

## Features
- **Session Management**: Automatically handles session creation and management, including Cloudflare bypass capabilities.
- **Conversation Handling**: Create, rename, retrieve, and delete conversations with ease.
- **Message Sending**: Send messages to the Claude AI model and receive responses, including support for streaming responses.

## Installation
To install Clodd, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/Clodd.git
cd Clodd
pip install -r requirements.txt
```

## Usage
Here is a simple example of how to use the `ClaudeClient` class:

```python
from krackn_claude_api.core.client import ClaudeClient

async with ClaudeClient() as client:
    conversation = await client.create_conversation(name="My Conversation")
    response = await client.send_message(conversation_id=conversation["uuid"], message="Hello, Claude!")
    print(response)
```

## Examples
Check the `examples` directory for more usage examples, including simple chat interactions and streaming responses.

## Testing
To run the tests, use the following command:

```bash
pytest tests/
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.