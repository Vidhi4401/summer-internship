from openai import OpenAI
client = OpenAI(
    api_key="sk-proj-nbCezSght7Ec2f33N1mZF1-xi1kWp6M7XxE4_AEEVwNRr8sb9SfUrWyV8Y-sqgl_NLH6w3yNHERVIOjviKTn3Vg_GhoR3H1-19gXmQItRSLiMxRMGIkUahFsUA",
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="generate random name",
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

print(response.output_text)
