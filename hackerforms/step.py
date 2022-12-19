from functools import reduce
from typing import List, Union, Callable
from .page import Page
from .page_response import PageResponse

Step = Union[Page, Callable]
Steps = List[Step]


class StepsResponse:
    def __init__(self):
        self.steps: Steps = []
        self.acc = {}

    def __getitem__(self, key: Union[int, str]):
        if isinstance(key, int):
            return self.steps[key]
        if isinstance(key, str):
            return self.acc[key]
        raise IndexError("Step not found")

    def append(self, step: Step):
        self.steps.append(step)
        self.__update_acc()

    def __update_acc(self):
        self.acc = {}
        for step in self.steps:
            if isinstance(step, PageResponse):
                self.acc.update(step)

    def pop(self, i: int = -1):
        step = self.steps.pop(i)
        self.__update_acc()
        return step


def run_steps(steps: Steps) -> StepsResponse:
    steps_to_execute: Steps = []  # stack
    executed_steps: Steps = []  # stack
    responses: StepsResponse = StepsResponse()  # stack

    steps_to_execute = steps[::-1]
    if not steps_to_execute:
        return responses

    if isinstance(steps_to_execute[-1], Callable):
        raise ValueError("First step cannot be a function")

    if steps_to_execute:
        response = run_page(
            steps_to_execute, executed_steps, responses, first_page=True
        )

    while steps_to_execute or response.action == "Back":
        if steps_to_execute and response.action != "Back":
            responses = execute_functions(steps_to_execute, executed_steps, responses)
            if not steps_to_execute:
                break
            response = run_page(
                steps_to_execute, executed_steps, responses, first_page=False
            )

        if response.action == "Back":
            response = go_back(steps_to_execute, executed_steps, responses)

    return responses


def go_back(steps_to_execute: Steps, executed_steps: Steps, responses: StepsResponse):
    page = executed_steps.pop()
    responses.pop()
    steps_to_execute.append(page)

    undo_functions(steps_to_execute, executed_steps, responses)
    if len(executed_steps) == 1:
        response = run_back_page(
            steps_to_execute, executed_steps, responses, first_page=True
        )
        return response

    response = run_back_page(
        steps_to_execute, executed_steps, responses, first_page=False
    )
    return response


def execute_functions(
    steps_to_execute: Steps, executed_steps: Steps, responses: StepsResponse
) -> StepsResponse:
    while steps_to_execute and isinstance(steps_to_execute[-1], Callable):
        fn = steps_to_execute.pop()
        responses.append(fn(responses))
        executed_steps.append(fn)
    return responses


def undo_functions(
    steps_to_execute: Steps, executed_steps: Steps, responses: StepsResponse
) -> StepsResponse:
    while executed_steps and isinstance(executed_steps[-1], Callable):
        fn = executed_steps.pop()
        steps_to_execute.append(fn)
        responses.pop()


def run_page(
    steps_to_execute: Steps,
    executed_steps: Steps,
    responses: StepsResponse,
    first_page: bool = False,
):
    page = steps_to_execute.pop()
    response = page.run() if first_page else page.run(actions=["Back", "Next"])
    responses.append(response)
    executed_steps.append(page)
    return response


def run_back_page(
    steps_to_execute: Steps,
    executed_steps: Steps,
    responses: StepsResponse,
    first_page: bool = False,
):
    page = executed_steps.pop()
    old_response: PageResponse = responses.pop()
    response = (
        page.run(initial_payload=old_response)
        if first_page
        else page.run(actions=["Back", "Next"], initial_payload=old_response)
    )
    responses.append(response)
    executed_steps.append(page)
    return response
