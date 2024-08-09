# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp.profiles import (
    CustomProfile,
    CustomCreateResponse,
    CustomDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.create(
                account_id="",
                profiles=[{}, {}, {}],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_match_count=5,
            context_awareness={
                "enabled": True,
                "skip": {"files": True},
            },
            description="A standard CVV card number",
            entries=[
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                },
            ],
            name="Generic CVV Card Number",
            ocr_enabled=True,
            shared_entries=[{"enabled": True}, {"enabled": True}, {"enabled": True}],
        )
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomProfile, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.delete(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.delete(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom = client.zero_trust.dlp.profiles.custom.get(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.profiles.custom.with_raw_response.get(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.profiles.custom.with_streaming_response.get(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomProfile, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomCreateResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.create(
                account_id="",
                profiles=[{}, {}, {}],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_match_count=5,
            context_awareness={
                "enabled": True,
                "skip": {"files": True},
            },
            description="A standard CVV card number",
            entries=[
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                },
            ],
            name="Generic CVV Card Number",
            ocr_enabled=True,
            shared_entries=[{"enabled": True}, {"enabled": True}, {"enabled": True}],
        )
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.update(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomProfile, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.update(
                profile_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.delete(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.delete(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.delete(
                profile_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.zero_trust.dlp.profiles.custom.get(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.profiles.custom.with_raw_response.get(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomProfile, custom, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.profiles.custom.with_streaming_response.get(
            profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomProfile, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.zero_trust.dlp.profiles.custom.with_raw_response.get(
                profile_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
