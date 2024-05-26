# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 zarathustra
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

"""
This module contains the classes required for kink_sync dialogue management.

- KinkSyncDialogue: The dialogue class maintains state of a dialogue and manages it.
- KinkSyncDialogues: The dialogues class keeps track of all dialogues.
"""

from abc import ABC
from typing import Callable, Dict, FrozenSet, Type, cast

from aea.common import Address
from aea.protocols.base import Message
from aea.protocols.dialogue.base import Dialogue, DialogueLabel, Dialogues

from packages.zarathustra.protocols.kink_sync.message import KinkSyncMessage


class KinkSyncDialogue(Dialogue):
    """The kink_sync dialogue class maintains state of a dialogue and manages it."""

    INITIAL_PERFORMATIVES: FrozenSet[Message.Performative] = frozenset(
        {KinkSyncMessage.Performative.INITIATE_CONVERSATION}
    )
    TERMINAL_PERFORMATIVES: FrozenSet[Message.Performative] = frozenset(
        {
            KinkSyncMessage.Performative.END_CONVERSATION,
            KinkSyncMessage.Performative.ERROR,
        }
    )
    VALID_REPLIES: Dict[Message.Performative, FrozenSet[Message.Performative]] = {
        KinkSyncMessage.Performative.END_CONVERSATION: frozenset(),
        KinkSyncMessage.Performative.ENGAGE: frozenset(
            {
                KinkSyncMessage.Performative.ENGAGE,
                KinkSyncMessage.Performative.END_CONVERSATION,
                KinkSyncMessage.Performative.ERROR,
            }
        ),
        KinkSyncMessage.Performative.ERROR: frozenset(),
        KinkSyncMessage.Performative.INITIATE_CONVERSATION: frozenset(
            {
                KinkSyncMessage.Performative.ENGAGE,
                KinkSyncMessage.Performative.END_CONVERSATION,
                KinkSyncMessage.Performative.ERROR,
            }
        ),
    }

    class Role(Dialogue.Role):
        """This class defines the agent's role in a kink_sync dialogue."""

        AGENT = "agent"

    class EndState(Dialogue.EndState):
        """This class defines the end states of a kink_sync dialogue."""

        END_CONVERSATION = 0
        ERROR = 1

    def __init__(
        self,
        dialogue_label: DialogueLabel,
        self_address: Address,
        role: Dialogue.Role,
        message_class: Type[KinkSyncMessage] = KinkSyncMessage,
    ) -> None:
        """
        Initialize a dialogue.

        :param dialogue_label: the identifier of the dialogue
        :param self_address: the address of the entity for whom this dialogue is maintained
        :param role: the role of the agent this dialogue is maintained for
        :param message_class: the message class used
        """
        Dialogue.__init__(
            self,
            dialogue_label=dialogue_label,
            message_class=message_class,
            self_address=self_address,
            role=role,
        )


class KinkSyncDialogues(Dialogues, ABC):
    """This class keeps track of all kink_sync dialogues."""

    END_STATES = frozenset(
        {KinkSyncDialogue.EndState.END_CONVERSATION, KinkSyncDialogue.EndState.ERROR}
    )

    _keep_terminal_state_dialogues = True

    def __init__(
        self,
        self_address: Address,
        role_from_first_message: Callable[[Message, Address], Dialogue.Role],
        dialogue_class: Type[KinkSyncDialogue] = KinkSyncDialogue,
    ) -> None:
        """
        Initialize dialogues.

        :param self_address: the address of the entity for whom dialogues are maintained
        :param dialogue_class: the dialogue class used
        :param role_from_first_message: the callable determining role from first message
        """
        Dialogues.__init__(
            self,
            self_address=self_address,
            end_states=cast(FrozenSet[Dialogue.EndState], self.END_STATES),
            message_class=KinkSyncMessage,
            dialogue_class=dialogue_class,
            role_from_first_message=role_from_first_message,
        )
