# KinkSync protocol

## Description


...

## Specification

```yaml
---
name: kink_sync
author: zarathustra
version: 0.1.0
description: A protocol for peer-to-peer communication between agents.
license: Apache-2.0
aea_version: '>=1.0.0, <2.0.0'
protocol_specification_id: zarathustra/kink_sync:0.1.0
speech_acts:
  initiate_conversation:
    message: pt:str
  engage:
    message: pt:str
  end_conversation:
    score: pt:int
  error:
    error_code: ct:ErrorCode
    error_msg: pt:str
...
---
ct:ErrorCode: |
  enum ErrorCodeEnum {
      CONNECTION_ERROR = 0;
      INVALID_MESSAGE = 1;
      TIMEOUT = 2;
    }
  ErrorCodeEnum error_code = 1;
...
---
initiation:
- initiate_conversation
reply:
  initiate_conversation: [ engage, end_conversation, error ]
  engage: [ engage, end_conversation, error ]
  end_conversation: [ ]
  error: [ ]
termination: [ end_conversation, error ]
roles: { agent }
end_states: [ end_conversation, error ]
keep_terminal_state_dialogues: true
...
```