## Phidata Ollama Integration Example

### Basic Usage
```python
from phi.agent import Agent
from phi.model.ollama import Ollama

agent = Agent(
    model=Ollama(id="llama3.2"),  # Use an available model like llama2, codellama, mistral, etc.
    markdown=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
```

### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| id | str | "llama3.2" | The ID of the Ollama model to use (e.g., "llama3.2", "codellama", "mistral") |
| name | str | "Ollama" | The name of the model instance |
| markdown | bool | True | Whether to format responses in markdown |

### Available Models
Common models you can use with Ollama:
- llama3.2
- exaone3.5
- smollm2
- neural-chat
- starling-lm

Make sure you have the desired model pulled in Ollama before using it.