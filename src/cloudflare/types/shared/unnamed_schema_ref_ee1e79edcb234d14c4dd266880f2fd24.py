# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRefEe1e79edcb234d14c4dd266880f2fd24"]


class UnnamedSchemaRefEe1e79edcb234d14c4dd266880f2fd24(BaseModel):
    body_part: Optional[str] = None
    """Name of the part in the multipart request that contains the script (e.g.

    the file adding a listener to the `fetch` event). Indicates a
    `service worker syntax` Worker.
    """

    main_module: Optional[str] = None
    """Name of the part in the multipart request that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """
