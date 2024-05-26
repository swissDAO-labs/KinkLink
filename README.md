<h1 align="center">
    <b>KinkLink</b>
</h1>

<p align="center">
    <!-- Add badges here -->
</p>

<!-- ## Introduction -->

Traditional dating apps require users to constantly swipe and make decisions about potential matches, leading to decision fatigue and cognitive overload. Moreover, many people cannot express themselves freely, out of fear of prosecution or worse. Even in more liberal places, users may feel hesitant to express their true preferences and identity on dating platforms due to concerns about privacy and judgment. And lastly, existing dating platforms often rely on proprietary algorithms for matchmaking, leaving users in the dark about how matches are made.

KinkLink address these issues by allowing users to spin up agents without revealing the operators identity. These client agents are owned by the user, who provides them with the following information:
- User info: such as age, gender, location, interests, and a biography
- Preferences: such as minimum and maximum age of their prospective partner, preferred genders, and, of course, their kinks.
- A knowledgebase of additional information to customize their agent.

The agent then registers to a multi-agent matchmaker service which tries to match up their clients based on the user info and their states preferences (see [matchmaker protocol](https://github.com/swissDAO-labs/KinkLink/tree/main/python/packages/zarathustra/protocols/matchmaker)).

Once a suitable match has been found by this service, their clients connect to one-another over a peer-to-peer network and engage in dialogue (see [kink_sync protocol](https://github.com/swissDAO-labs/KinkLink/tree/main/python/packages/zarathustra/protocols/kink_sync)). This is where the additional knowledge base of information provided by the user is leveraged. The agents keep track of how well the conversation is going. Once a threshold is reached, a high positive score, low negative score, or a timeout, the conversation ends. The agents report this score to each other, providing them feedback on the conversational  employed, as well as to the matchmaker service, such that it can update its rating system and improve its matchmaking capability.

When two agents establish a mutually positive interaction, the agent operator gets notified and prompted with the request to share contact information with the other client, such as a Telegram handle.


## Requirements

- Git
- Poetry
- Protocol buffers v24.3
    ```shell
    wget https://github.com/protocolbuffers/protobuf/releases/download/v24.3/protoc-24.3-linux-x86_64.zip && unzip protoc-24.3-linux-x86_64.zip -d protoc && sudo mv protoc/bin/protoc /usr/local/bin/protoc
    ```
- [Tendermint](https://docs.tendermint.com/v0.34/introduction/install.html) `==0.34.19`
    ```shell
    docker pull tendermint/tendermint:v0.34.19
    ```

<!-- ## Getting started -->


## Install from source

Clone the repository:

```shell
git clone https://github.com/swissDAO-labs/KinkLink.git
```

## Running the KinkLink matchmaker service


```shell
docker run -p 26656:26656 -p 26657:26657 -e PROXY_APP=tcp://localhost:26658 -e CREATE_EMPTY_BLOCKS=true -e TMHOME=/tendermint/node1 tendermint:0.34.19

```


```shell
aea -s create agent && cd agent && aea -s generate-key ethereum && aea -s add-key ethereum && aea -s add skill zarathustra/kink_link:0.1.0 --local && aea -s issue-certificates
```

then configure the agent configuration by adding the following the aea-config.yaml file

```
---
public_id: valory/abci:0.1.0
type: connection
config:
  target_skill_id: zarathustra/kink_link:0.1.0
  host: ${str:localhost}
  port: ${int:26658}
  use_tendermint: ${bool:false}
---
public_id: valory/p2p_libp2p_client:0.1.0
type: connection
config:
  nodes:
  - uri: ${str:acn.staging.autonolas.tech:9005}
    public_key: ${str:02d3a830c9d6ea1ae91936951430dee11f4662f33118b02190693be835359a9d77}
cert_requests:
- identifier: acn
  ledger_id: ethereum
  message_format: '{public_key}'
  not_after: '2024-01-01'
  not_before: '2023-01-01'
  public_key: ${str:02d3a830c9d6ea1ae91936951430dee11f4662f33118b02190693be835359a9d77}
  save_path: .certs/acn_cosmos_9005.txt
---
public_id: zarathustra/kink_link:0.1.0
type: skill
models:
  params:
    args:
      sleep_time: 1
      tendermint_p2p_url: ${str:localhost:26656}
      tendermint_com_url: ${str:http://localhost:8080}
      tendermint_max_retries: 5
      tendermint_url: ${str:http://localhost:26657}

```

and run

```shell
aea -s run
```


## Contributing
Learn how to contribute to the project by following the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog
Explore the project's version history and changes in [CHANGELOG.md](CHANGELOG.md).

## License
This project is licensed under the [Apache2.0 license](LICENSE).
