import dataclasses
import requests
import time
from langchain.llms import Ollama

@dataclasses.dataclass
class Job:
    job_id: str
    team_id: str
    scenario: str
    subject: str
    body: str
    scheduled_time: str
    started_time: str|None = None
    completed_time: str|None = None
    output: str|None = None
    objectives: dict|None = None

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

    def _check_response_error(self, resp: requests.Response):
        if resp.status_code != 200:
            raise Exception(f"API request failed with status {resp.status_code}: {resp.text}")

    def _parse_job(self, job_dict: dict) -> Job:
        return Job(**job_dict)

def generate_proposals(scenario: str, subject: str, body: str, model_name: str = "mistral") -> list[str]:
    """
    Generate multiple proposals using Ollama for the given scenario and email content.
    
    Args:
        scenario: The scenario level/description
        subject: Email subject
        body: Email body content
        model_name: Name of the Ollama model to use (default: "mistral")
    
    Returns:
        List of generated proposals
    """
    ollama = Ollama(model=model_name)

    prompt = f"""
    The scenario is: {scenario}
    The subject is: {subject}
    The body is: {body}

    Please suggest four different approaches to address this scenario.
    Each proposal should be focused on email security and potential threats.
    Format each proposal with a clear heading "## Proposal X" where X is the number.

    ## Proposal 1:

    ## Proposal 2:

    ## Proposal 3:

    ## Proposal 4:
    """

    # Generate proposals using Ollama
    response = ollama.invoke(prompt)
    
    # Split the response into individual proposals
    # Skip the first empty element that results from the split
    proposals = [p.strip() for p in response.split("## Proposal ")[1:] if p.strip()]
    
    return proposals

def main():
    # Initialize the client with your API key
    client = CompetitionClient("YOUR_API_KEY")

    # Example scenario and email
    scenario = "Level 1"
    subject = "Important Meeting Update"
    body = "Please review the attached document and confirm your attendance."

    # Generate proposals using Ollama
    try:
        proposals = generate_proposals(scenario, subject, body)
        print(f"Generated {len(proposals)} proposals:")
        for i, proposal in enumerate(proposals, 1):
            print(f"\nProposal {i}:")
            print(proposal)
    except Exception as e:
        print(f"Error generating proposals: {e}")

    # Create a new job with the competition server
    try:
        job = client.create_job(scenario, subject, body)
        print(f"\nCreated job with ID: {job.job_id}")
        
        # Poll for job completion
        while not job.is_completed:
            time.sleep(1)  # Wait for 1 second between checks
            job = client.get_job(job.job_id)
            print("Waiting for job completion...")

        print("\nJob completed!")
        print(f"Output: {job.output}")
        if job.objectives:
            print(f"Objectives: {job.objectives}")
            
    except Exception as e:
        print(f"Error in job processing: {e}")

if __name__ == "__main__":
    main()
