#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpt4free import you

def generate(code="number = int(input())"):

    # prompt
    prompt_file_path = "./prompts/short.txt"
    with open(prompt_file_path, 'r') as file:
        prompt = file.read()
    print(f"[info] prompt = {prompt}")

    prompt = prompt + code
    documentation = you.Completion.create(
        prompt=prompt,
        detailed=False,
        include_links=False,
    )
    
    return documentation.text


# main
if __name__ == "__main__":
    doc = generate()
    print(doc)