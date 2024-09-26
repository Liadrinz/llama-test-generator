import inspect
import requests
import os
import re
import subprocess


def llama(prompt):
    resp = requests.post(
        "https://api.deepinfra.com/v1/openai/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer Dpdh1rO9M2SvvGCdnI8G7h1joZSITZVU",
        },
        json={
            "model": "meta-llama/Meta-Llama-3-8B-Instruct",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        }
    )
    resp_body = resp.json()
    choices = resp_body.get("choices", None)
    if choices is None:
        raise ValueError(resp_body)
    response = choices[0]["message"]["content"]
    return response


def auto_test(req=None, overwrite=False):
    def wrapper(func):
        func_file = os.path.split(func.__globals__["__file__"])[-1].split(".")[0]
        test_file_name = f"test_{func_file}_{func.__name__}.py"
        if not os.path.exists(test_file_name) or overwrite:
            func_src = inspect.getsource(func)
            requirement = " " if req is None else f" The test case you create must meet the following requirements:\n\n{req}\n\n"
            prompt = f"Perform unit test of the following function by creating testcases.{requirement}Please import the function from `{func_file}`. Please only output runnable code without other content. DO NOT contain any non-ASCII characters. Ensure a correct python syntax. DO NOT contain \".\" in function names. Here's the code of the function to be tested:\n\n```python\n{func_src}\n```"
            test_code = llama(prompt)
            test_code = re.findall(r'```(?:\w*\n)?(.*?)```', test_code, re.DOTALL | re.MULTILINE)
            test_code = "\n".join(test_code)
            with open(test_file_name, "w") as f:
                f.write(test_code)
        return func
    if callable(req):
        return wrapper(req)
    return wrapper
