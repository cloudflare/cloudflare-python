# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.email_security.investigate import (
    MoveBulkResponse,
    MoveCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMove:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        move = client.email_security.investigate.move.create(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
        )
        assert_matches_type(SyncSinglePage[MoveCreateResponse], move, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.move.with_raw_response.create(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        move = response.parse()
        assert_matches_type(SyncSinglePage[MoveCreateResponse], move, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_security.investigate.move.with_streaming_response.create(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            move = response.parse()
            assert_matches_type(SyncSinglePage[MoveCreateResponse], move, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.move.with_raw_response.create(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
                destination="Inbox",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            client.email_security.investigate.move.with_raw_response.create(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                destination="Inbox",
            )

    @parametrize
    def test_method_bulk(self, client: Cloudflare) -> None:
        move = client.email_security.investigate.move.bulk(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
            postfix_ids=["4Njp3P0STMz2c02Q"],
        )
        assert_matches_type(SyncSinglePage[MoveBulkResponse], move, path=["response"])

    @parametrize
    def test_raw_response_bulk(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.move.with_raw_response.bulk(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
            postfix_ids=["4Njp3P0STMz2c02Q"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        move = response.parse()
        assert_matches_type(SyncSinglePage[MoveBulkResponse], move, path=["response"])

    @parametrize
    def test_streaming_response_bulk(self, client: Cloudflare) -> None:
        with client.email_security.investigate.move.with_streaming_response.bulk(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
            postfix_ids=["4Njp3P0STMz2c02Q"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            move = response.parse()
            assert_matches_type(SyncSinglePage[MoveBulkResponse], move, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.move.with_raw_response.bulk(
                account_id="",
                destination="Inbox",
                postfix_ids=["4Njp3P0STMz2c02Q"],
            )


class TestAsyncMove:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        move = await async_client.email_security.investigate.move.create(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
        )
        assert_matches_type(AsyncSinglePage[MoveCreateResponse], move, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.move.with_raw_response.create(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        move = await response.parse()
        assert_matches_type(AsyncSinglePage[MoveCreateResponse], move, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.move.with_streaming_response.create(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            move = await response.parse()
            assert_matches_type(AsyncSinglePage[MoveCreateResponse], move, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.move.with_raw_response.create(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
                destination="Inbox",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            await async_client.email_security.investigate.move.with_raw_response.create(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                destination="Inbox",
            )

    @parametrize
    async def test_method_bulk(self, async_client: AsyncCloudflare) -> None:
        move = await async_client.email_security.investigate.move.bulk(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
            postfix_ids=["4Njp3P0STMz2c02Q"],
        )
        assert_matches_type(AsyncSinglePage[MoveBulkResponse], move, path=["response"])

    @parametrize
    async def test_raw_response_bulk(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.move.with_raw_response.bulk(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
            postfix_ids=["4Njp3P0STMz2c02Q"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        move = await response.parse()
        assert_matches_type(AsyncSinglePage[MoveBulkResponse], move, path=["response"])

    @parametrize
    async def test_streaming_response_bulk(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.move.with_streaming_response.bulk(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination="Inbox",
            postfix_ids=["4Njp3P0STMz2c02Q"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            move = await response.parse()
            assert_matches_type(AsyncSinglePage[MoveBulkResponse], move, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.move.with_raw_response.bulk(
                account_id="",
                destination="Inbox",
                postfix_ids=["4Njp3P0STMz2c02Q"],
            )
