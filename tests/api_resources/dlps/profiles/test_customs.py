# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dlps.profiles import (
    CustomUpdateResponse,
    CustomDeleteResponse,
    CustomDLPProfilesCreateCustomProfilesResponse,
    CustomGetResponse,
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
from cloudflare.types.dlps.profiles import custom_update_params
from cloudflare.types.dlps.profiles import custom_dlp_profiles_create_custom_profiles_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustoms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom = client.dlps.profiles.customs.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom = client.dlps.profiles.customs.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_match_count=5,
            description="A standard CVV card number",
            entries=[
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                    "profile_id": {},
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                    "profile_id": {},
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                    "profile_id": {},
                },
            ],
            name="Generic CVV Card Number",
            shared_entries=[{"enabled": True}, {"enabled": True}, {"enabled": True}],
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dlps.profiles.customs.with_raw_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dlps.profiles.customs.with_streaming_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomUpdateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.update(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.dlps.profiles.customs.delete(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dlps.profiles.customs.with_raw_response.delete(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dlps.profiles.customs.with_streaming_response.delete(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.delete(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_dlp_profiles_create_custom_profiles(self, client: Cloudflare) -> None:
        custom = client.dlps.profiles.customs.dlp_profiles_create_custom_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )
        assert_matches_type(Optional[CustomDLPProfilesCreateCustomProfilesResponse], custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_dlp_profiles_create_custom_profiles(self, client: Cloudflare) -> None:
        response = client.dlps.profiles.customs.with_raw_response.dlp_profiles_create_custom_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(Optional[CustomDLPProfilesCreateCustomProfilesResponse], custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_dlp_profiles_create_custom_profiles(self, client: Cloudflare) -> None:
        with client.dlps.profiles.customs.with_streaming_response.dlp_profiles_create_custom_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(Optional[CustomDLPProfilesCreateCustomProfilesResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_dlp_profiles_create_custom_profiles(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.dlp_profiles_create_custom_profiles(
                "",
                profiles=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom = client.dlps.profiles.customs.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dlps.profiles.customs.with_raw_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dlps.profiles.customs.with_streaming_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomGetResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.get(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.dlps.profiles.customs.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCustoms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.dlps.profiles.customs.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.dlps.profiles.customs.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_match_count=5,
            description="A standard CVV card number",
            entries=[
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                    "profile_id": {},
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                    "profile_id": {},
                },
                {
                    "enabled": True,
                    "name": "Credit card (Visa)",
                    "pattern": {
                        "regex": "^4[0-9]{6,14}$",
                        "validation": "luhn",
                    },
                    "profile_id": {},
                },
            ],
            name="Generic CVV Card Number",
            shared_entries=[{"enabled": True}, {"enabled": True}, {"enabled": True}],
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.profiles.customs.with_raw_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlps.profiles.customs.with_streaming_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomUpdateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.update(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.dlps.profiles.customs.delete(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.profiles.customs.with_raw_response.delete(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlps.profiles.customs.with_streaming_response.delete(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.delete(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_dlp_profiles_create_custom_profiles(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.dlps.profiles.customs.dlp_profiles_create_custom_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )
        assert_matches_type(Optional[CustomDLPProfilesCreateCustomProfilesResponse], custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_dlp_profiles_create_custom_profiles(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.profiles.customs.with_raw_response.dlp_profiles_create_custom_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(Optional[CustomDLPProfilesCreateCustomProfilesResponse], custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_dlp_profiles_create_custom_profiles(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlps.profiles.customs.with_streaming_response.dlp_profiles_create_custom_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
            profiles=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(Optional[CustomDLPProfilesCreateCustomProfilesResponse], custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_dlp_profiles_create_custom_profiles(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.dlp_profiles_create_custom_profiles(
                "",
                profiles=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.dlps.profiles.customs.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.profiles.customs.with_raw_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlps.profiles.customs.with_streaming_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomGetResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.get(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.dlps.profiles.customs.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
