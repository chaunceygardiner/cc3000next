# Copyright 2021 by John A Kline <john@johnkline.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO
from weecfg.extension import ExtensionInstaller
import configobj

cc3000next_config = """
[CC3000Next]
    # This section is for RainWise MarkIII weather stations and CC3000 logger.
    
    # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
    port = /dev/cc3000
    
    # To debug serial communications, set to 1.
    debug_serial = 0
    
    # The station model, e.g., CC3000 or CC3000R
    model = CC3000
    
    # The driver to use:
    driver = user.cc3000next
    
    # Rainwise MKIII-LR only updates once every two seconds.
    polling_interval = 2
    
    # Clear records when we reach 25,000 records.
    logger_threshold = 25000
    
    use_station_time = True

    # DST periods (setTime will be ignored during time changes).
    [[dst_periods]]
        2021 = 2021-03-14 02:00:00, 2021-11-07 02:00:00
        2022 = 2022-03-13 02:00:00, 2022-11-06 02:00:00
        2023 = 2023-03-12 02:00:00, 2023-11-05 02:00:00
        2024 = 2024-03-10 02:00:00, 2024-11-03 02:00:00
        2025 = 2025-03-09 02:00:00, 2025-11-02 02:00:00
        2026 = 2026-03-08 02:00:00, 2026-11-01 02:00:00
        2027 = 2027-03-14 02:00:00, 2027-11-07 02:00:00
        2028 = 2028-03-12 02:00:00, 2028-11-05 02:00:00
        2029 = 2029-03-11 02:00:00, 2029-11-04 02:00:00
"""

cc3000next_dict = configobj.ConfigObj(StringIO(cc3000next_config))

def loader():
    return CC3000NextInstaller()

class CC3000NextInstaller(ExtensionInstaller):
    def __init__(self):
        super(CC3000NextInstaller, self).__init__(
            version="0.4",
            name='CC3000Next',
            description='Capture weather data from Rainwise MK-III CC3000 stations',
            author="John A Kline",
            author_email="john@johnkline.com",
            config = cc3000next_dict,
            files=[
                ('bin/user', ['bin/user/cc3000next.py'])
            ]
        )
