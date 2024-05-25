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

"""This package contains the rounds of KinkLinkAbciApp."""

from enum import Enum
from typing import Dict, List, Optional, Set, Tuple

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)

from packages.zarathustra.skills.kink_link_abci.payloads import (
    FeedbackProcessingPayload,
    MatchmakingPayload,
    PeerIDExchangePayload,
    RatingSystemUpdatePayload,
)


class Event(Enum):
    """KinkLinkAbciApp Events"""

    MATCHES = "matches"
    DONE = "done"
    NO_MATCHES = "no_matches"
    FEEDBACK = "feedback"
    NO_FEEDBACK = "no_feedback"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class FeedbackProcessingRound(AbstractRound):
    """FeedbackProcessingRound"""

    payload_class = FeedbackProcessingPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: FeedbackProcessingPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: FeedbackProcessingPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class MatchmakingRound(AbstractRound):
    """MatchmakingRound"""

    payload_class = MatchmakingPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: MatchmakingPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: MatchmakingPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class PeerIDExchangeRound(AbstractRound):
    """PeerIDExchangeRound"""

    payload_class = PeerIDExchangePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: PeerIDExchangePayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: PeerIDExchangePayload) -> None:
        """Process payload."""
        raise NotImplementedError


class RatingSystemUpdateRound(AbstractRound):
    """RatingSystemUpdateRound"""

    payload_class = RatingSystemUpdatePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: RatingSystemUpdatePayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: RatingSystemUpdatePayload) -> None:
        """Process payload."""
        raise NotImplementedError


class TransactionSubmissionRound(DegenerateRound):
    """TransactionSubmissionRound"""


class KinkLinkAbciApp(AbciApp[Event]):
    """KinkLinkAbciApp"""

    initial_round_cls: AppState = MatchmakingRound
    initial_states: Set[AppState] = {MatchmakingRound}
    transition_function: AbciAppTransitionFunction = {
        MatchmakingRound: {
            Event.NO_MATCHES: FeedbackProcessingRound,
            Event.MATCHES: PeerIDExchangeRound
        },
        PeerIDExchangeRound: {
            Event.NO_FEEDBACK: FeedbackProcessingRound,
            Event.FEEDBACK: FeedbackProcessingRound
        },
        FeedbackProcessingRound: {
            Event.NO_FEEDBACK: TransactionSubmissionRound,
            Event.FEEDBACK: RatingSystemUpdateRound
        },
        RatingSystemUpdateRound: {
            Event.DONE: TransactionSubmissionRound
        },
        TransactionSubmissionRound: {}
    }
    final_states: Set[AppState] = {TransactionSubmissionRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: Set[str] = []
    db_pre_conditions: Dict[AppState, Set[str]] = {
        MatchmakingRound: [],
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        TransactionSubmissionRound: [],
    }
