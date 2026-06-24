from dataclasses import dataclass, field


@dataclass
class Pet:
    name: str
    animal_type: str


@dataclass
class Task:
    task_type: str
    pet: Pet
    day: str
    duration_minutes: int
    priority: str

    def edit(self, field, value) -> None:
        pass


@dataclass
class Schedule:
    date: str
    tasks: list = field(default_factory=list)
    time_availabilities: list = field(default_factory=list)
    priorities: dict = field(default_factory=dict)

    def add_task(self, task: Task) -> None:
        pass

    def add_time_availability(self, start, end) -> None:
        pass

    def generate_plan(self) -> list:
        pass


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)
    schedule: Schedule = None