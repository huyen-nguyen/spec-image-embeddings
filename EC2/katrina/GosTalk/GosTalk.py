#%%
import numpy as np
import openai
import pandas as pd
import json

import gosling as gos

# USE ChatGPT to generate gosling code

class GosTalk_ChatGPT():
    MODEL = 'gpt-3.5-turbo'
    def __init__(self, prompt=None, template_chart=None):

        if not prompt:
            template_data = '''{
                "url": "https://server.gosling-lang.org/api/v1/tileset_info/?d=cistrome-multivec",
                "type": "multivec",
                "row": "sample",
                "column": "position",
                "value": "peak",
                "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
                '''
            self.prompt = [
                { 'role': 'system', 'content': "Hello, I'm Gosling. I'm a visualization tooltik for interactive genomic data." },
                {"role": "system", 'content': 'I can help you write gosling specification json code'},
                
                # template data
                {"role": "user", "content": f'use the data as {template_data} unless you are asked otherwise'},
                {"role": "user", "content": "please just draw one sample unless you are asked to draw multiple samples"},

                # teach the gosling grammar again
                {"role": "user", "content": (
                'do not miss tracks, ' 
                'axis should be specified as string, '
                'and one axis should be genomic, '
                'remember to specify the field name, '
                'width and height should be specified for each track or view as number'
                )},

                # {"role": "user", "content": "do not miss tracks, axis is a string value, and one axis should be genomic"},
                # {"role": "user","content": "please just draw one sample unless you are asked to draw multiple samples"},
                # {"role": "user", "content": "remember to specify the field name"},
            ]
        else:
            self.prompt = prompt

        if template_chart:
            self.prompt = self.prompt + [{"role": "user", "content": f'help me modify the Gosling Specification Code {template_chart}'}]

    def ask(self, new_question):

        self.prompt = self.prompt + [{"role": "user", "content": new_question}]

        response = openai.ChatCompletion.create(
            model=GosTalk_ChatGPT.MODEL,
            messages=self.prompt,
            temperature=0,
            # stream=True  # this time, we set stream=True
        )

        content = response.choices[0]['message']['content']

        if '```' in content:
            code = content.split('```')[1]
            explanation = content.split('```')[2]
        else:
            code = content
            explanation = ''

        print(explanation)
        print(code)

        self.prompt = self.prompt + [{"role": "assistant", "content": code}]

        try:
            return gos.View(**json.loads(code))
        except:
            print('Error: cannot render the code')
            return 

# %%

class GosTalk_Davinci():
    MODEL = 'code-davinci-002'
    def __init__(self, template_data=None):
        if not template_data:
            self.template_data = '''{
                    "url": "https://server.gosling-lang.org/api/v1/tileset_info/?d=cistrome-multivec",
                    "type": "multivec",
                    "row": "sample",
                    "column": "position",
                    "value": "peak",
                    "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
                    '''
        # self.MODEL = 'davinci'
        self.MODEL = 'code-davinci-002'
        self.prompt = (
            "You are Gosling, a visualization tooltik for interactive genomic data. "
            "You can help the user write gosling specification json code. "
            'do not miss tracks, ' 
            'axis should be specified as string, '
            'and one axis should be genomic, '
            'remember to specify the field name, '
            'width and height should be specified for each track or view as number'
            '\n'

            f'use the data as {template_data} unless you are asked to use other data, '
            "please just draw one sample unless you are asked to draw multiple samples. \n"
            )

    def ask(self, new_question):

        self.prompt = self.prompt + f"Q: {new_question}\n"

        response = openai.Completion.create(
            model=GosTalk_Davinci.MODEL,
            prompt=self.prompt + "A:",
            temperature=0,
            max_tokens=400
        )

        content = response.choices[0]['text']

        if '```' in content:
            code = content.split('```')[1]
            explanation = content.split('```')[2]
        else:
            code = content
            explanation = ''

        print(explanation)
        print(code)

        self.prompt = self.prompt + f"A: {code}"
        # return gos.View(**json.loads(code))
        return content


# %%
