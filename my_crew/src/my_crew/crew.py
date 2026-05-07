from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MyCrew():
    """MyCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    
      
    @agent
    def math_teacher(self) -> Agent:
        return Agent(
            config=self.agents_config['math_teacher'], 
            verbose=True,
            allow_delegation=False
        )
        
        
    @agent
    def python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['python_developer'], 
            verbose=True,
            allow_code_execution=True,
            allow_delegation=False,
            # allow_tool_calls=True
        )        

  
    @task
    def math_task(self) -> Task:
        return Task(
            config=self.tasks_config['math_task'], # type: ignore[index]
        )

    @task
    def python_task(self) -> Task:
        return Task(
            config=self.tasks_config['python_task'],
            output_file='python_code.md' 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MyCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
