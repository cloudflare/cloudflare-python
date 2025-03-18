# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.user import (
    TokenCreateResponse,
    TokenDeleteResponse,
    TokenVerifyResponse,
)
from cloudflare.types.shared import Token

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        token = client.user.tokens.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        token = client.user.tokens.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {
                            "id": "c8fed203ed3043cba015a93ad1616f1f",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        {
                            "id": "82e64a83756745bbbb1c9c2701bf816b",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            condition={
                "request_ip": {
                    "in": ["123.123.123.0/24", "2606:4700::/32"],
                    "not_in": ["123.123.123.100/24", "2606:4700:4700::/48"],
                }
            },
            expires_on=parse_datetime("2020-01-01T00:00:00Z"),
            not_before=parse_datetime("2018-07-01T05:20:00Z"),
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.user.tokens.with_raw_response.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.user.tokens.with_streaming_response.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        token = client.user.tokens.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
        )
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        token = client.user.tokens.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {
                            "id": "c8fed203ed3043cba015a93ad1616f1f",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        {
                            "id": "82e64a83756745bbbb1c9c2701bf816b",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
            condition={
                "request_ip": {
                    "in": ["123.123.123.0/24", "2606:4700::/32"],
                    "not_in": ["123.123.123.100/24", "2606:4700:4700::/48"],
                }
            },
            expires_on=parse_datetime("2020-01-01T00:00:00Z"),
            not_before=parse_datetime("2018-07-01T05:20:00Z"),
        )
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.user.tokens.with_raw_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.user.tokens.with_streaming_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[Token], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.user.tokens.with_raw_response.update(
                token_id="",
                name="readonly token",
                policies=[
                    {
                        "effect": "allow",
                        "permission_groups": [
                            {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                            {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                        ],
                        "resources": {
                            "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                            "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                        },
                    }
                ],
                status="active",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        token = client.user.tokens.list()
        assert_matches_type(SyncV4PagePaginationArray[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        token = client.user.tokens.list(
            direction="asc",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Token], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        token = client.user.tokens.delete(
            "ed17574386854bf78a67040be0a770b0",
        )
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.user.tokens.with_raw_response.delete(
            "ed17574386854bf78a67040be0a770b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.user.tokens.with_streaming_response.delete(
            "ed17574386854bf78a67040be0a770b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.user.tokens.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        token = client.user.tokens.get(
            "ed17574386854bf78a67040be0a770b0",
        )
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.user.tokens.with_raw_response.get(
            "ed17574386854bf78a67040be0a770b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.user.tokens.with_streaming_response.get(
            "ed17574386854bf78a67040be0a770b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[Token], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.user.tokens.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_verify(self, client: Cloudflare) -> None:
        token = client.user.tokens.verify()
        assert_matches_type(Optional[TokenVerifyResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_verify(self, client: Cloudflare) -> None:
        response = client.user.tokens.with_raw_response.verify()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenVerifyResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_verify(self, client: Cloudflare) -> None:
        with client.user.tokens.with_streaming_response.verify() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenVerifyResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {
                            "id": "c8fed203ed3043cba015a93ad1616f1f",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        {
                            "id": "82e64a83756745bbbb1c9c2701bf816b",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            condition={
                "request_ip": {
                    "in": ["123.123.123.0/24", "2606:4700::/32"],
                    "not_in": ["123.123.123.100/24", "2606:4700:4700::/48"],
                }
            },
            expires_on=parse_datetime("2020-01-01T00:00:00Z"),
            not_before=parse_datetime("2018-07-01T05:20:00Z"),
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.tokens.with_raw_response.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.tokens.with_streaming_response.create(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
        )
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {
                            "id": "c8fed203ed3043cba015a93ad1616f1f",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        {
                            "id": "82e64a83756745bbbb1c9c2701bf816b",
                            "meta": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
            condition={
                "request_ip": {
                    "in": ["123.123.123.0/24", "2606:4700::/32"],
                    "not_in": ["123.123.123.100/24", "2606:4700:4700::/48"],
                }
            },
            expires_on=parse_datetime("2020-01-01T00:00:00Z"),
            not_before=parse_datetime("2018-07-01T05:20:00Z"),
        )
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.tokens.with_raw_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.tokens.with_streaming_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                }
            ],
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[Token], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.user.tokens.with_raw_response.update(
                token_id="",
                name="readonly token",
                policies=[
                    {
                        "effect": "allow",
                        "permission_groups": [
                            {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                            {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                        ],
                        "resources": {
                            "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                            "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                        },
                    }
                ],
                status="active",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.list()
        assert_matches_type(AsyncV4PagePaginationArray[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.list(
            direction="asc",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Token], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.delete(
            "ed17574386854bf78a67040be0a770b0",
        )
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.tokens.with_raw_response.delete(
            "ed17574386854bf78a67040be0a770b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.tokens.with_streaming_response.delete(
            "ed17574386854bf78a67040be0a770b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.user.tokens.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.get(
            "ed17574386854bf78a67040be0a770b0",
        )
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.tokens.with_raw_response.get(
            "ed17574386854bf78a67040be0a770b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[Token], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.tokens.with_streaming_response.get(
            "ed17574386854bf78a67040be0a770b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[Token], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.user.tokens.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_verify(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.user.tokens.verify()
        assert_matches_type(Optional[TokenVerifyResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.tokens.with_raw_response.verify()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenVerifyResponse], token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.tokens.with_streaming_response.verify() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenVerifyResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True
