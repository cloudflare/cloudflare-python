from __future__ import annotations

import asyncio
import logging
from typing import Iterator

import pytest

import os
from typing import TYPE_CHECKING, AsyncIterator

from cloudflare import Cloudflare, AsyncCloudflare

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("cloudflare").setLevel(logging.DEBUG)


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

api_key = "144c9defac04969c7bfad8efaa8ea194"
api_email = "user@example.com"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[Cloudflare]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with Cloudflare(
        base_url=base_url, api_key=api_key, api_email=api_email, _strict_response_validation=strict
    ) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncCloudflare]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncCloudflare(
        base_url=base_url, api_key=api_key, api_email=api_email, _strict_response_validation=strict
    ) as client:
        yield client
