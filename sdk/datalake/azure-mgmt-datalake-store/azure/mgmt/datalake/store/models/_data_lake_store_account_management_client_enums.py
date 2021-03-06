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


class DataLakeStoreAccountState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the Data Lake Store account.
    """

    ACTIVE = "Active"
    SUSPENDED = "Suspended"

class DataLakeStoreAccountStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning status of the Data Lake Store account.
    """

    FAILED = "Failed"
    CREATING = "Creating"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    PATCHING = "Patching"
    SUSPENDING = "Suspending"
    RESUMING = "Resuming"
    DELETING = "Deleting"
    DELETED = "Deleted"
    UNDELETING = "Undeleting"
    CANCELED = "Canceled"

class EncryptionConfigType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of encryption configuration being used. Currently the only supported types are
    'UserManaged' and 'ServiceManaged'.
    """

    USER_MANAGED = "UserManaged"
    SERVICE_MANAGED = "ServiceManaged"

class EncryptionProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of encryption provisioning for this Data Lake Store account.
    """

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"

class EncryptionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of encryption for this Data Lake Store account.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class FirewallAllowAzureIpsState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of allowing or disallowing IPs originating within Azure through the firewall.
    If the firewall is disabled, this is not enforced.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class FirewallState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the IP address firewall for this Data Lake Store account.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class OperationOrigin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation.
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class SubscriptionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The subscription state.
    """

    REGISTERED = "Registered"
    SUSPENDED = "Suspended"
    DELETED = "Deleted"
    UNREGISTERED = "Unregistered"
    WARNED = "Warned"

class TierType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The commitment tier to use for next month.
    """

    CONSUMPTION = "Consumption"
    COMMITMENT1_TB = "Commitment_1TB"
    COMMITMENT10_TB = "Commitment_10TB"
    COMMITMENT100_TB = "Commitment_100TB"
    COMMITMENT500_TB = "Commitment_500TB"
    COMMITMENT1_PB = "Commitment_1PB"
    COMMITMENT5_PB = "Commitment_5PB"

class TrustedIdProviderState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the trusted identity provider feature for this Data Lake Store account.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class UsageUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the unit of measurement.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNTS_PER_SECOND = "CountsPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
