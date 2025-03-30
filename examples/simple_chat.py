# This file provides an example of how to use the ClaudeClient class to perform a simple chat interaction.

import asyncio
from krackn_claude_api.core.client import ClaudeClient

async def main():
    async with ClaudeClient() as client:
        # Create a new conversation
        conversation = await client.create_conversation(name="Simple Chat Example")
        print(f"Created conversation: {conversation['uuid']}")

        # Send a message
        response = await client.send_message(
            conversation_id=conversation['uuid'],
            message="Hello, Claude! How are you?"
        )
        print(f"Claude's response: {response['completion']}")

        # Optionally, send another message
        response = await client.send_message(
            conversation_id=conversation['uuid'],
            message="What can you do?"
        )
        print(f"Claude's response: {response['completion']}")

if __name__ == "__main__":
    asyncio.run(main())