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

"""This module contains class representations corresponding to every custom type in the protocol specification."""


class ErrorCode:
    """This class represents an instance of ErrorCode."""

    def __init__(self):
        """Initialise an instance of ErrorCode."""
        raise NotImplementedError

    @staticmethod
    def encode(error_code_protobuf_object, error_code_object: "ErrorCode") -> None:
        """
        Encode an instance of this class into the protocol buffer object.

        The protocol buffer object in the error_code_protobuf_object argument is matched with the instance of this class in the 'error_code_object' argument.

        :param error_code_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param error_code_object: an instance of this class to be encoded in the protocol buffer object.
        """
        raise NotImplementedError

    @classmethod
    def decode(cls, error_code_protobuf_object) -> "ErrorCode":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.

        A new instance of this class is created that matches the protocol buffer object in the 'error_code_protobuf_object' argument.

        :param error_code_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'error_code_protobuf_object' argument.
        """
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError


class Preferences:
    """This class represents an instance of Preferences."""

    def __init__(self):
        """Initialise an instance of Preferences."""
        raise NotImplementedError

    @staticmethod
    def encode(preferences_protobuf_object, preferences_object: "Preferences") -> None:
        """
        Encode an instance of this class into the protocol buffer object.

        The protocol buffer object in the preferences_protobuf_object argument is matched with the instance of this class in the 'preferences_object' argument.

        :param preferences_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param preferences_object: an instance of this class to be encoded in the protocol buffer object.
        """
        raise NotImplementedError

    @classmethod
    def decode(cls, preferences_protobuf_object) -> "Preferences":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.

        A new instance of this class is created that matches the protocol buffer object in the 'preferences_protobuf_object' argument.

        :param preferences_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'preferences_protobuf_object' argument.
        """
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError


class UserInfo:
    """This class represents an instance of UserInfo."""

    def __init__(self):
        """Initialise an instance of UserInfo."""
        raise NotImplementedError

    @staticmethod
    def encode(user_info_protobuf_object, user_info_object: "UserInfo") -> None:
        """
        Encode an instance of this class into the protocol buffer object.

        The protocol buffer object in the user_info_protobuf_object argument is matched with the instance of this class in the 'user_info_object' argument.

        :param user_info_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param user_info_object: an instance of this class to be encoded in the protocol buffer object.
        """
        raise NotImplementedError

    @classmethod
    def decode(cls, user_info_protobuf_object) -> "UserInfo":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.

        A new instance of this class is created that matches the protocol buffer object in the 'user_info_protobuf_object' argument.

        :param user_info_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'user_info_protobuf_object' argument.
        """
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError
