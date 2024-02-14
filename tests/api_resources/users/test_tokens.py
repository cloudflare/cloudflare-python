# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users import (
    TokenUpdateResponse,
    TokenDeleteResponse,
    TokenGetResponse,
    TokenUserAPITokensCreateTokenResponse,
    TokenUserAPITokensListTokensResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users import token_update_params
from cloudflare.types.users import token_user_api_tokens_create_token_params
from cloudflare.types.users import token_user_api_tokens_list_tokens_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        token = client.users.tokens.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
            status="active",
        )
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        token = client.users.tokens.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
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
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.users.tokens.with_raw_response.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.users.tokens.with_streaming_response.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenUpdateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        token = client.users.tokens.delete(
            {},
        )
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.users.tokens.with_raw_response.delete(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.users.tokens.with_streaming_response.delete(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        token = client.users.tokens.get(
            {},
        )
        assert_matches_type(TokenGetResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.users.tokens.with_raw_response.get(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenGetResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.users.tokens.with_streaming_response.get(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenGetResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_user_api_tokens_create_token(self, client: Cloudflare) -> None:
        token = client.users.tokens.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
        )
        assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_api_tokens_create_token_with_all_params(self, client: Cloudflare) -> None:
        token = client.users.tokens.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
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
        assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_api_tokens_create_token(self, client: Cloudflare) -> None:
        response = client.users.tokens.with_raw_response.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_api_tokens_create_token(self, client: Cloudflare) -> None:
        with client.users.tokens.with_streaming_response.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_user_api_tokens_list_tokens(self, client: Cloudflare) -> None:
        token = client.users.tokens.user_api_tokens_list_tokens()
        assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_api_tokens_list_tokens_with_all_params(self, client: Cloudflare) -> None:
        token = client.users.tokens.user_api_tokens_list_tokens(
            direction="desc",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_api_tokens_list_tokens(self, client: Cloudflare) -> None:
        response = client.users.tokens.with_raw_response.user_api_tokens_list_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_api_tokens_list_tokens(self, client: Cloudflare) -> None:
        with client.users.tokens.with_streaming_response.user_api_tokens_list_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
            status="active",
        )
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
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
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.with_raw_response.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
            status="active",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenUpdateResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.with_streaming_response.update(
            {},
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
            status="active",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenUpdateResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.delete(
            {},
        )
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.with_raw_response.delete(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.with_streaming_response.delete(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenDeleteResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.get(
            {},
        )
        assert_matches_type(TokenGetResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.with_raw_response.get(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenGetResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.with_streaming_response.get(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenGetResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_api_tokens_create_token(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
        )
        assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_api_tokens_create_token_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
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
        assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_api_tokens_create_token(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.with_raw_response.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_api_tokens_create_token(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.with_streaming_response.user_api_tokens_create_token(
            name="readonly token",
            policies=[
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
                {
                    "effect": "allow",
                    "permission_groups": [{}, {}],
                    "resources": {
                        "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*",
                        "com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4": "*",
                    },
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenUserAPITokensCreateTokenResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_api_tokens_list_tokens(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.user_api_tokens_list_tokens()
        assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_api_tokens_list_tokens_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.users.tokens.user_api_tokens_list_tokens(
            direction="desc",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_api_tokens_list_tokens(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.with_raw_response.user_api_tokens_list_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_api_tokens_list_tokens(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.with_streaming_response.user_api_tokens_list_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenUserAPITokensListTokensResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True
