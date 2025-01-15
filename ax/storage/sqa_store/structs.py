#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from collections.abc import Callable
from typing import NamedTuple

from ax.storage.sqa_store.decoder import Decoder
from ax.storage.sqa_store.encoder import Encoder
from ax.storage.sqa_store.sqa_config import SQAConfig


class DBSettings(NamedTuple):
    """
    Defines behavior for loading/saving experiment to/from db.
    Either creator or url must be specified as a way to connect to the SQL db.
    """

    creator: Callable | None = None
    decoder: Decoder = Decoder(config=SQAConfig())
    encoder: Encoder = Encoder(config=SQAConfig())
    url: str | None = None
