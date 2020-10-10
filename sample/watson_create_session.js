const AssistantV2 = require('ibm-watson/assistant/v2');
const { IamAuthenticator } = require('ibm-watson/auth');

const service = new AssistantV2({
  version: '2019-02-28',
  authenticator: new IamAuthenticator({
    apikey: 'GGGGGG-KKKKKKKK-VVVVVV-XXXXXX',
  }),
  url: 'https://gateway-tok.watsonplatform.net/assistant/api',
});

service.createSession({
  assistantId: 'aaaaaaaa-bbbbbbb-cccccc-ddddddd'
})
  .then(res => {
    console.log(JSON.stringify(res, null, 2));
  })
  .catch(err => {
    console.log(err);
  });
