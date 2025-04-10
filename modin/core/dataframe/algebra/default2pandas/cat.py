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

"""Module houses default applied-on-category functions builder class."""

from .series import SeriesDefault
import pandas


class CatDefault(SeriesDefault):
    """Builder for default-to-pandas methods which is executed under category accessor."""

    @classmethod
    def frame_wrapper(
        cls, df: pandas.DataFrame
    ) -> pandas.core.arrays.categorical.CategoricalAccessor:
        """
        Get category accessor of the passed frame.

        Parameters
        ----------
        df : pandas.DataFrame

        Returns
        -------
        pandas.core.arrays.categorical.CategoricalAccessor
        """
        return df.squeeze(axis=1).cat
