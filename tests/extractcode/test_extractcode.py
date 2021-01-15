
#
# Copyright (c) nexB Inc. and others.
# SPDX-License-Identifier: Apache-2.0
#
# Visit https://aboutcode.org and https://github.com/nexB/ for support and download.
# ScanCode is a trademark of nexB Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from os.path import dirname
from os.path import exists
from os.path import join

from commoncode.testcase import FileBasedTesting
from commoncode import fileutils
from extractcode import new_name


class TestNewName(FileBasedTesting):
    test_data_dir = join(dirname(__file__), 'data')

    def test_new_name_without_extensions(self):
        test_dir = self.get_test_loc('new_name/noext', copy=True)
        renamed = new_name(join(test_dir, 'test'), is_dir=False)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'test_4' == result

        renamed = new_name(join(test_dir, 'TEST'), is_dir=False)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'TEST_4' == result

        renamed = new_name(join(test_dir, 'test_1'), is_dir=True)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'test_1_1' == result

    def test_new_name_with_extensions(self):
        test_dir = self.get_test_loc('new_name/ext', copy=True)
        renamed = new_name(join(test_dir, 'test.txt'), is_dir=False)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'test_3.txt' == result

        renamed = new_name(join(test_dir, 'TEST.txt'), is_dir=False)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'TEST_3.txt' == result

        renamed = new_name(join(test_dir, 'TEST.tXt'), is_dir=False)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'TEST_3.tXt' == result

        renamed = new_name(join(test_dir, 'test.txt'), is_dir=True)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'test.txt_2' == result

        renamed = new_name(join(test_dir, 'teST.txt'), is_dir=True)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert 'teST.txt_2' == result

    def test_new_name_with_empties(self):
        base_dir = self.get_temp_dir()
        self.assertRaises(AssertionError, new_name, '', is_dir=False)
        test_file = base_dir + '/'
        renamed = new_name(test_file, is_dir=False)
        assert renamed
        assert not exists(renamed)

        test_file = join(base_dir, '.')
        renamed = new_name(test_file, is_dir=False)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert '_' == result

        test_dir = base_dir + '/'

        renamed = new_name(test_dir, is_dir=True)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert result

        test_dir = join(base_dir, '.')
        renamed = new_name(test_dir, is_dir=True)
        assert not exists(renamed)
        result = fileutils.file_name(renamed)
        assert '_' == result
