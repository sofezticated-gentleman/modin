# Licensed to Modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The Modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

"""Module that houses compat functions and objects for `pandas.io.common`."""

from contextlib import contextmanager
from collections import namedtuple

from pandas.io.common import get_handle as pd_get_handle
from pandas.core.aggregation import reconstruct_func

from modin.utils import _inherit_docstrings

_HandleWrapper = namedtuple("_HandleWrapper", ["handle"])


@contextmanager
@_inherit_docstrings(pd_get_handle)
def get_handle(
    path_or_buf,
    mode: str,
    encoding=None,
    compression=None,
    memory_map=False,
    is_text=True,
    errors=None,
    storage_options=None,
):
    assert storage_options is None
    f, handles = pd_get_handle(
        path_or_buf,
        mode=mode,
        encoding=encoding,
        compression=compression,
        memory_map=memory_map,
        is_text=is_text,
        errors=errors,
    )
    try:
        yield _HandleWrapper(handle=f)
    finally:
        for handle in handles:
            try:
                handle.close()
            except (OSError, ValueError):
                pass


def pd_pivot_table(df, **kwargs):  # noqa: PR01, RT01
    """Perform pandas pivot_table against a dataframe ignoring unsupported args."""
    unsupported_sort = kwargs.pop("sort", None)
    assert unsupported_sort is None
    return df.pivot_table(**kwargs)


def pd_convert_dtypes(df, **kwargs):  # noqa: PR01, RT01
    """Perform pandas convert_dtypes against a dataframe or series ignoring unsupported args."""
    unsupported_convert = kwargs.pop("convert_floating", None)
    assert unsupported_convert is None
    return df.convert_dtypes(**kwargs)


__all__ = ["get_handle", "pd_pivot_table", "pd_convert_dtypes", "reconstruct_func"]
