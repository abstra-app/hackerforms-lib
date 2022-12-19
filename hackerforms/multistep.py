from typing import List, Union, Callable
from .page import Page
from .page_response import PageResponse


def __execute_page_step(steps_to_execute, executed_steps, page_responses, back=False):
    page = steps_to_execute.pop()
    page_response = page.run(actions=["back", "next"]) if back else page.run()
    page_responses.append(page_response)

    executed_steps.append(page)
    return page_response


def run_multistep(steps: Union[List[Page], Callable]):
    steps_to_execute: Union[List[Page], Callable] = []  # stack
    executed_steps: Union[List[Page], Callable] = []  # stack
    page_responses: List[PageResponse] = []
    fn_responses = []

    steps_to_execute = steps[::-1]
    if not steps_to_execute:
        return page_responses

    if isinstance(steps_to_execute[-1], Page):
        page_response = __execute_page_step(
            steps_to_execute, executed_steps, page_responses
        )

    while steps_to_execute and not isinstance(steps_to_execute[-1], Page):
        fn = steps_to_execute.pop()
        fn_responses.append(fn(page_responses))
        executed_steps.append(fn)

    while steps_to_execute or page_response.action == "back":
        if page_response.action == "back":
            steps_to_execute.append(executed_steps.pop())
            while len(executed_steps) and not isinstance(executed_steps[-1], Page):
                steps_to_execute.append(executed_steps.pop())
                fn_responses.pop()

            page_responses.pop()
            response = page_responses.pop()
            if len(executed_steps) == 1:
                page_response = executed_steps[-1].run(initial_payload=response)
                page_responses.append(page_response)
            else:
                page_response = executed_steps[-1].run(
                    initial_payload=response, actions=["back", "next"]
                )
                page_responses.append(page_response)
            continue

        if isinstance(steps_to_execute[-1], Page):
            page_response = __execute_page_step(
                steps_to_execute, executed_steps, page_responses, back=True
            )

        while steps_to_execute and not isinstance(steps_to_execute[-1], Page):
            fn = steps_to_execute.pop()
            fn_responses.append(fn(page_responses))
            executed_steps.append(fn)

    return page_responses, fn_responses
