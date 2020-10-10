import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('GGGGGG-KKKKKKKK-VVVVVV-XXXXXX')
assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator
)

assistant.set_service_url('https://gateway-tok.watsonplatform.net/assistant/api')

response = assistant.create_session(
    assistant_id='aaaaaaaa-bbbbbbb-cccccc-ddddddd'
).get_result()

print(json.dumps(response, indent=2))
