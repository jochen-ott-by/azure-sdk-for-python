# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class CompositePathSortOrder(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Sort order for composite paths.
    """

    ASCENDING = "Ascending"
    DESCENDING = "Descending"

class ConflictResolutionMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the conflict resolution mode.
    """

    LAST_WRITER_WINS = "LastWriterWins"
    CUSTOM = "Custom"

class ConnectorOffer(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The cassandra connector offer type for the Cosmos DB C* database account.
    """

    SMALL = "Small"

class DatabaseAccountKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the type of database account. This can only be set at database account creation.
    """

    GLOBAL_DOCUMENT_DB = "GlobalDocumentDB"
    MONGO_DB = "MongoDB"
    PARSE = "Parse"

class DataType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The datatype for which the indexing behavior is applied to.
    """

    STRING = "String"
    NUMBER = "Number"
    POINT = "Point"
    POLYGON = "Polygon"
    LINE_STRING = "LineString"
    MULTI_POLYGON = "MultiPolygon"

class DefaultConsistencyLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default consistency level and configuration settings of the Cosmos DB account.
    """

    EVENTUAL = "Eventual"
    SESSION = "Session"
    BOUNDED_STALENESS = "BoundedStaleness"
    STRONG = "Strong"
    CONSISTENT_PREFIX = "ConsistentPrefix"

class IndexingMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the indexing mode.
    """

    CONSISTENT = "Consistent"
    LAZY = "Lazy"
    NONE = "None"

class IndexKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the type of index.
    """

    HASH = "Hash"
    RANGE = "Range"
    SPATIAL = "Spatial"

class KeyKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The access key to regenerate.
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"
    PRIMARY_READONLY = "primaryReadonly"
    SECONDARY_READONLY = "secondaryReadonly"

class NotebookWorkspaceName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class PartitionKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the kind of algorithm used for partitioning
    """

    HASH = "Hash"
    RANGE = "Range"

class PrimaryAggregationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The primary aggregation type of the metric.
    """

    NONE = "None"
    AVERAGE = "Average"
    TOTAL = "Total"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    LAST = "Last"

class PublicNetworkAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether requests from Public Network are allowed
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServerVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the ServerVersion of an a MongoDB account.
    """

    THREE2 = "3.2"
    THREE6 = "3.6"

class SpatialType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the spatial type of index.
    """

    POINT = "Point"
    LINE_STRING = "LineString"
    POLYGON = "Polygon"
    MULTI_POLYGON = "MultiPolygon"

class TriggerOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operation the trigger is associated with
    """

    ALL = "All"
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    REPLACE = "Replace"

class TriggerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the Trigger
    """

    PRE = "Pre"
    POST = "Post"

class UnitType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    MILLISECONDS = "Milliseconds"
