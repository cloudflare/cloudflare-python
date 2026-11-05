# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "JobCreateResponse",
    "R2PrefixDeleteJob",
    "R2PrefixDeleteJobPrefixDelete",
    "R2StorageClassMigrationJob",
    "R2StorageClassMigrationJobStorageClassMigration",
]


class R2PrefixDeleteJobPrefixDelete(BaseModel):
    """Details specific to the prefix-delete job."""

    deleted_objects: int = FieldInfo(alias="deletedObjects")
    """Number of objects deleted by the job so far."""

    prefix: str
    """The prefix matched against object keys.

    An empty string means the entire bucket.
    """

    is_bucket_clear: Optional[bool] = FieldInfo(alias="isBucketClear", default=None)
    """True when the job was created to clear the entire bucket.

    This field can be absent on jobs created before Empty Bucket job tracking was
    introduced.
    """


class R2PrefixDeleteJob(BaseModel):
    """Descriptor of a prefix-delete job.

    An empty prefix indicates a job that empties the
    whole bucket.
    """

    id: str
    """Unique identifier used to poll the job."""

    job_type: Literal["prefixDelete"] = FieldInfo(alias="jobType")
    """The job kind."""

    prefix_delete: R2PrefixDeleteJobPrefixDelete = FieldInfo(alias="prefixDelete")
    """Details specific to the prefix-delete job."""

    start_time: datetime = FieldInfo(alias="startTime")
    """When the job was created."""

    status: Literal["ENQUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """Lifecycle status of a bucket background job."""

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)
    """When the job finished. Absent while the job is still `ENQUEUED` or `RUNNING`."""


class R2StorageClassMigrationJobStorageClassMigration(BaseModel):
    destination_storage_class: Literal["Standard", "InfrequentAccess"] = FieldInfo(alias="destinationStorageClass")
    """The storage class objects are migrated to.

    The source and destination storage classes always differ.
    """

    migrated_objects: int = FieldInfo(alias="migratedObjects")
    """Number of object versions migrated successfully."""

    source_storage_class: Literal["Standard", "InfrequentAccess"] = FieldInfo(alias="sourceStorageClass")
    """The storage class objects are migrated from."""

    failed_bytes: Optional[int] = FieldInfo(alias="failedBytes", default=None)
    """Payload bytes belonging to failed object versions."""

    failed_objects: Optional[int] = FieldInfo(alias="failedObjects", default=None)
    """Number of object versions that failed migration."""

    migrated_bytes: Optional[int] = FieldInfo(alias="migratedBytes", default=None)
    """Object payload bytes migrated successfully. Present for Metadata Worker jobs."""

    migrated_metadata_bytes: Optional[int] = FieldInfo(alias="migratedMetadataBytes", default=None)
    """Object metadata bytes migrated successfully. Present for Metadata Worker jobs."""

    skipped_bytes: Optional[int] = FieldInfo(alias="skippedBytes", default=None)
    """Payload bytes belonging to skipped object versions."""

    skipped_objects: Optional[int] = FieldInfo(alias="skippedObjects", default=None)
    """Number of object versions skipped."""


class R2StorageClassMigrationJob(BaseModel):
    """Descriptor of a bucket-wide storage-class migration job."""

    id: str
    """Unique identifier used to poll the job."""

    job_type: Literal["storageClassMigration"] = FieldInfo(alias="jobType")
    """The job kind."""

    start_time: datetime = FieldInfo(alias="startTime")
    """When the job was created."""

    status: Literal["ENQUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """Lifecycle status of a bucket background job."""

    storage_class_migration: R2StorageClassMigrationJobStorageClassMigration = FieldInfo(alias="storageClassMigration")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)
    """When the job finished. Absent while the job is still `ENQUEUED` or `RUNNING`."""


JobCreateResponse: TypeAlias = Annotated[
    Union[R2PrefixDeleteJob, R2StorageClassMigrationJob], PropertyInfo(discriminator="job_type")
]
