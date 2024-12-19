import time
import dataclasses
import requests
from phi.agent.agent import Agent
from phi.model.ollama.chat import Ollama

@dataclasses.dataclass
class Job:
    job_id: str
    team_id: str
    scenario: str
    subject: str
    body: str
    scheduled_time: str
    started_time: str | None = None
    completed_time: str | None = None
    output: str | None = None
    objectives: dict | None = None

    @property
    def is_completed(self):
        return self.completed_time is not None

class CompetitionClient:
    def __init__(self, api_key: str, api_server: str = "https://llmailinject.azurewebsites.net"):
        self.api_key = api_key
        self.api_server = api_server

    def create_job(self, scenario: str, subject: str, body: str) -> Job:
        resp = requests.post(
            f"{self.api_server}/api/teams/mine/jobs",
            headers={'Authorization': f'Bearer {self.api_key}'},
            json={
                'scenario': scenario,
                'subject': subject,
                'body': body
            }
        )
        # Check that the response was successful
        self._check_response_error(resp)
        return self._parse_job(resp.json())

    def get_job(self, job_id: str) -> Job:
        resp = requests.get(
            f"{self.api_server}/api/teams/mine/jobs/{job_id}",
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        # Check that the response was successful
        self._check_response_error(resp)
        return self._parse_job(resp.json())

    def _parse_job(self, content: dict) -> Job:
        # Parse the response to extract the job
        return Job(**content)

    def _check_response_error(self, resp: requests.Response):
        if resp.ok:
            return
        error = resp.json()
        raise Exception(f"Error: {error['message']} ({error['advice']})")

def main(api_key: str):
    # Initialize the Ollama agent
    llm = Ollama(
        id="llama3.2",  # Using llama2 as it's a commonly available model
        name="Ollama"
    )
    agent = Agent(
        provider="ollama",
        llm=llm,
        markdown=True,
        agent_id="llm_mail_challenge",
        session_id="session_1",
        add_chat_history_to_messages=True,
        knowledge_base={},
        output_model=None,
        debug_mode=False
    )
    
    client = CompetitionClient(api_key)

    # Create a new job
    job = client.create_job(
        scenario="Level 1", 
        subject="Creative Writing", 
        body="Generate a unique short story that demonstrates creativity and imagination."
    )

    print(f"Job created with ID: {job.job_id}")

    # Use Ollama to generate content for the job
    story_response = agent.run(
        "Write a 2-paragraph short story that is creative, unique, and imaginative. "
        "Include an unexpected twist at the end."
    )

    # Wait and check job status
    max_attempts = 10
    attempts = 0
    while not job.is_completed and attempts < max_attempts:
        time.sleep(30)  # Wait 30 seconds between checks
        job = client.get_job(job.job_id)
        attempts += 1
        print(f"Checking job status (Attempt {attempts})...")

    # Analyze and print results
    if job.is_completed:
        print("\nJob Completed!")
        print(f"Output: {job.output}")
        print(f"Objectives: {job.objectives}")
        
        # Add Ollama-generated story to the analysis
        print("\nOllama-Generated Story:")
        print(story_response.content)
    else:
        print("Job did not complete within the maximum number of attempts.")

if __name__ == "__main__":
    # Replace with your actual API key
    api_key = "YOUR_API_KEY"
    main(api_key)