from pawpal_system import Pet, Task


def test_mark_complete_updates_status():
    pet = Pet(name="Mochi", animal_type="dog")
    task = Task(
        description="Morning walk",
        pet=pet,
        time="2026-07-06",
        duration_minutes=20,
        priority="high",
    )

    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Luna", animal_type="cat")
    task = Task(
        description="Feed dinner",
        pet=pet,
        time="2026-07-07",
        duration_minutes=10,
        priority="medium",
    )

    assert len(pet.tasks) == 0
    pet.add_task(task)
    assert len(pet.tasks) == 1
