import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('GGGGGG-KKKKKKKK-VVVVVV-XXXXXX')
assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator
)

assistant.set_service_url('https://gateway-tok.watsonplatform.net/assistant/api')

response = assistant.message(
    assistant_id='aaaaaaaa-bbbbbbb-cccccc-ddddddd',
    session_id='b2553333-2ace-4999-855c-da8cb666f39f',
    input={
        'message_type': 'text',
        'text': '海外ですね。',
        'options': {
            'return_context': True
        }
    }
).get_result()

print(json.dumps(response, indent=2))
