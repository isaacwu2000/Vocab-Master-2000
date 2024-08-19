from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class VocabMasterCrew():
	"""VocabMaster crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def story_maker(self) -> Agent:
		return Agent(
			config=self.agents_config['story_maker'],
			verbose=True
		)

	@agent
	def joke_maker(self) -> Agent:
		return Agent(
			config=self.agents_config['joke_maker'],
			verbose=True
		)

	@task
	def make_story(self) -> Task:
		return Task(
			config=self.tasks_config['make_story'],
		)

	@task
	def make_joke(self) -> Task:
		return Task(
			config=self.tasks_config['make_joke'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the VocabMaster crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)