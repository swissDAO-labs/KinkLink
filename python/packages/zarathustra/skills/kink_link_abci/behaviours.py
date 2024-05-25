# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This package contains round behaviours of KinkLinkAbciApp."""

from abc import ABC
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.zarathustra.skills.kink_link_abci.models import Params
from packages.zarathustra.skills.kink_link_abci.rounds import (
    SynchronizedData,
    KinkLinkAbciApp,
    FeedbackProcessingRound,
    MatchmakingRound,
    PeerIDExchangeRound,
    RatingSystemUpdateRound,
)
from packages.zarathustra.skills.kink_link_abci.rounds import (
    FeedbackProcessingPayload,
    MatchmakingPayload,
    PeerIDExchangePayload,
    RatingSystemUpdatePayload,
)


class KinkLinkBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the kink_link_abci skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class FeedbackProcessingBehaviour(KinkLinkBaseBehaviour):
    """FeedbackProcessingBehaviour"""

    matching_round: Type[AbstractRound] = FeedbackProcessingRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = FeedbackProcessingPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class MatchmakingBehaviour(KinkLinkBaseBehaviour):
    """MatchmakingBehaviour"""

    matching_round: Type[AbstractRound] = MatchmakingRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = MatchmakingPayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PeerIDExchangeBehaviour(KinkLinkBaseBehaviour):
    """PeerIDExchangeBehaviour"""

    matching_round: Type[AbstractRound] = PeerIDExchangeRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PeerIDExchangePayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class RatingSystemUpdateBehaviour(KinkLinkBaseBehaviour):
    """RatingSystemUpdateBehaviour"""

    matching_round: Type[AbstractRound] = RatingSystemUpdateRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = RatingSystemUpdatePayload(sender=sender, content=...)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class KinkLinkRoundBehaviour(AbstractRoundBehaviour):
    """KinkLinkRoundBehaviour"""

    initial_behaviour_cls = MatchmakingBehaviour
    abci_app_cls = KinkLinkAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        FeedbackProcessingBehaviour,
        MatchmakingBehaviour,
        PeerIDExchangeBehaviour,
        RatingSystemUpdateBehaviour
    ]
