# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pagerules import (
    PageruleGetResponse,
    PageruleEditResponse,
    PageruleListResponse,
    PageruleCreateResponse,
    PageruleDeleteResponse,
    PageruleUpdateResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPagerules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                ],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
                priority=0,
                status="active",
            )

        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pagerules.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pagerules.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = response.parse()
                assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.pagerules.with_raw_response.create(
                    zone_id="",
                    actions=[{}, {}, {}],
                    targets=[
                        {
                            "constraint": {
                                "operator": "matches",
                                "value": "*example.com/images/*",
                            },
                            "target": "url",
                        }
                    ],
                )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                ],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
                priority=0,
                status="active",
            )

        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pagerules.with_raw_response.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pagerules.with_streaming_response.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = response.parse()
                assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.pagerules.with_raw_response.update(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                    actions=[{}, {}, {}],
                    targets=[
                        {
                            "constraint": {
                                "operator": "matches",
                                "value": "*example.com/images/*",
                            },
                            "target": "url",
                        }
                    ],
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                client.pagerules.with_raw_response.update(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    actions=[{}, {}, {}],
                    targets=[
                        {
                            "constraint": {
                                "operator": "matches",
                                "value": "*example.com/images/*",
                            },
                            "target": "url",
                        }
                    ],
                )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                direction="asc",
                match="any",
                order="status",
                status="active",
            )

        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pagerules.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pagerules.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = response.parse()
                assert_matches_type(PageruleListResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.pagerules.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pagerules.with_raw_response.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pagerules.with_streaming_response.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = response.parse()
                assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.pagerules.with_raw_response.delete(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                client.pagerules.with_raw_response.delete(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                ],
                priority=0,
                status="active",
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pagerules.with_raw_response.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pagerules.with_streaming_response.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = response.parse()
                assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.pagerules.with_raw_response.edit(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                client.pagerules.with_raw_response.edit(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = client.pagerules.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pagerules.with_raw_response.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = response.parse()
        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pagerules.with_streaming_response.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = response.parse()
                assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.pagerules.with_raw_response.get(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                client.pagerules.with_raw_response.get(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )


class TestAsyncPagerules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                ],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
                priority=0,
                status="active",
            )

        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pagerules.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pagerules.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = await response.parse()
                assert_matches_type(PageruleCreateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.pagerules.with_raw_response.create(
                    zone_id="",
                    actions=[{}, {}, {}],
                    targets=[
                        {
                            "constraint": {
                                "operator": "matches",
                                "value": "*example.com/images/*",
                            },
                            "target": "url",
                        }
                    ],
                )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                ],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
                priority=0,
                status="active",
            )

        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pagerules.with_raw_response.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pagerules.with_streaming_response.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}, {}, {}],
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = await response.parse()
                assert_matches_type(PageruleUpdateResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.pagerules.with_raw_response.update(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                    actions=[{}, {}, {}],
                    targets=[
                        {
                            "constraint": {
                                "operator": "matches",
                                "value": "*example.com/images/*",
                            },
                            "target": "url",
                        }
                    ],
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                await async_client.pagerules.with_raw_response.update(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    actions=[{}, {}, {}],
                    targets=[
                        {
                            "constraint": {
                                "operator": "matches",
                                "value": "*example.com/images/*",
                            },
                            "target": "url",
                        }
                    ],
                )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                direction="asc",
                match="any",
                order="status",
                status="active",
            )

        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pagerules.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleListResponse, pagerule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pagerules.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = await response.parse()
                assert_matches_type(PageruleListResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.pagerules.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pagerules.with_raw_response.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pagerules.with_streaming_response.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = await response.parse()
                assert_matches_type(Optional[PageruleDeleteResponse], pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.pagerules.with_raw_response.delete(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                await async_client.pagerules.with_raw_response.delete(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                    {
                        "name": "forward_url",
                        "value": {
                            "type": "temporary",
                            "url": "http://www.example.com/somewhere/$1/astring/$2/anotherstring/$3",
                        },
                    },
                ],
                priority=0,
                status="active",
                targets=[
                    {
                        "constraint": {
                            "operator": "matches",
                            "value": "*example.com/images/*",
                        },
                        "target": "url",
                    }
                ],
            )

        assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pagerules.with_raw_response.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pagerules.with_streaming_response.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = await response.parse()
                assert_matches_type(PageruleEditResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.pagerules.with_raw_response.edit(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                await async_client.pagerules.with_raw_response.edit(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            pagerule = await async_client.pagerules.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pagerules.with_raw_response.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerule = await response.parse()
        assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pagerules.with_streaming_response.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pagerule = await response.parse()
                assert_matches_type(PageruleGetResponse, pagerule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.pagerules.with_raw_response.get(
                    pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
                await async_client.pagerules.with_raw_response.get(
                    pagerule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )
