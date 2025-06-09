
from openai import OpenAI
client = OpenAI(
    api_key="sk-proj-nbCezSght7Ec2f33N1mZF1-xi1kWp6M7XxE4_AEEVwNRr8sb9SfUrWyV8Y-BlbkFJQQr78_xgZeDsqgl_NLH6w3yNHERVIOjviKTn3Vg_GhoR3H1-19gXmQItRSLiMxRMGIkUahFsUA",
)

def ask_gpt(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        text={
            "format": {
                "type": "text"
            }
        },
        reasoning={},
        tools=[],
        temperature=1,
        max_output_tokens=2048,
        top_p=1,
        store=True
    )
    return response.output_text


topic = input("Enter a podcast topic you'd like to create a script about:")
prompt =f"write a detailed script for podcast {topic}"
response = (ask_gpt(prompt))

with open("podcastscript.txt", "w",encoding="utf-8") as f:
  f.write(response)
