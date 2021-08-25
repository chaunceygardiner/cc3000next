# weewx-cc3000next
*WeeWX driver for CC3000 devices largely based on built-in driver Copyright (c) 2014 Matthew Wall
*Note: WeeWX's CC3000 driver contains substantial contributions from this author.

## Description

This driver builds on WeeWX built-in CC3000 driver.  If deemed desirable, and accepted,
it will be merged into WeeWX at a later date.  This driver is not recommended.  In most
cases, you should go with the built-in driver.

Copyright (C)2021 by John A Kline (john@johnkline.com)

# cc3000next Changes vis. a vis. WeeWX's cc3000 Driver

1. If set time happened to be called around a DST/ST time change (because
   the drift value was exceeded), bad things would happen.  It would be
   determined that the console was an hour fast, it would then set the
   console back an hour (but keep DST), and an hours worth of data would
   be lost as the timestamps would be duplicates.  DST periods can be
   specified in the CC3000Next section, and setTime will be a no-op
   during time change windows.

2. Setting the time now sleeps until approx. top of second in order to more
   precisely set the time (since it can only be set in whole seconds).  There
   is is a fudge of set_time_padding which can be set in weewx.conf and defaults
   to 0.40 (seconds).

# Installation Instructions

1. Download the lastest release, weewx-cc3000next-0.1.zip, from the
   [GitHub Repository](https://github.com/chaunceygardiner/weewx-cc3000next).

1. Run the following command.

   `sudo /home/weewx/bin/wee_extension --install weewx-cc3000next-0.1.zip`

   Note: this command assumes weewx is installed in /home/weewx.  If it's installed
   elsewhere, adjust the path of wee_extension accordingly.

1. Edit the `Station` section of weewx.conf.  Change the `station_type` value
   to `CC3000Next`.

   ```
   [Station]
       station_type = CC3000Next
   ```

1. Edit the CC3000Next section of weewx.conf to specify the port.
   For example:
   ```
    port = /dev/cc3000
   ```

1. Edit the CC3000Next section of weewx.conf to add DST periods for your
   location.  Note: the year to the left of the equals sign is simply a
   string and is ingored  Also note, the first date MUST be the start
   of daylight savings time and the second must be the end.  As such, in
   the southern hemisphere, the dst end date (date on the right) will be
   in the following year of the starting date (date on the left).
   ```
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
   ```

1. Restart WeeWX

## Licensing

weewx-cc3000next is licensed under the GNU Public License v3.
