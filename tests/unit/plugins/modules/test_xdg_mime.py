# -*- coding: utf-8 -*-
# Copyright (c) 2025, Marcos Alano <marcoshalano@gmail.com>
# Based on gio_mime module. Copyright (c) 2022, Alexei Znamensky <russoz@gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible_collections.community.general.plugins.modules import xdg_mime
from .uthelper import UTHelper, RunCommandMock


UTHelper.from_module(xdg_mime, __name__, mocks=[RunCommandMock])
