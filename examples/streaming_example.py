import asyncio
from krackn_claude_api.core.client import ClaudeClient

async def main():
    async with ClaudeClient() as client:
        # Create a new conversation
        conversation = await client.create_conversation(name="Streaming Example")
        conversation_id = conversation["uuid"]
        
        print(f"Created conversation with ID: {conversation_id}")

        # Send a message and stream the response
        async for response in client.send_message_streaming(
            conversation_id=conversation_id,
            message="Hello, Claude! Can you tell me a joke?",
            model="claude-3-opus-20240229"
        ):
            if 'completion' in response:
                print(response['completion'], end='', flush=True)

if __name__ == "__main__":
    asyncio.run(main())