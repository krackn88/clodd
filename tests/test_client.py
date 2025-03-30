import pytest
from krackn_claude_api.core.client import ClaudeClient

@pytest.fixture
def client():
    return ClaudeClient()

def test_initialization(client):
    assert client.session_data == {"cookies": {}, "headers": {}}
    assert client.organization_id is None
    assert client.browser_profile_path is None
    assert client.max_retries == 3
    assert client.retry_delay == 1.0

def test_create_conversation(client, mocker):
    mocker.patch('krackn_claude_api.core.client.ClaudeClient.create_conversation', return_value={"uuid": "test-conversation-id"})
    conversation = client.create_conversation(name="Test Conversation")
    assert conversation["uuid"] == "test-conversation-id"

def test_send_message(client, mocker):
    mocker.patch('krackn_claude_api.core.client.ClaudeClient.send_message', return_value={"completion": "Test response"})
    response = client.send_message(conversation_id="test-conversation-id", message="Hello")
    assert response["completion"] == "Test response"

def test_get_conversations(client, mocker):
    mocker.patch('krackn_claude_api.core.client.ClaudeClient.get_conversations', return_value=[{"uuid": "test-conversation-id"}])
    conversations = client.get_conversations()
    assert len(conversations) == 1
    assert conversations[0]["uuid"] == "test-conversation-id"