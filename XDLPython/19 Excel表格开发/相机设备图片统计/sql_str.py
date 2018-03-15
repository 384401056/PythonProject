#!/usr/bin/env python
# -*- coding: utf-8 -*-

sql = """
    SELECT
    t.Address,d.DeviceNo,d.id
    FROM
      t_b_deviceinfo d,
    t_s_org t
    WHERE
    d.OrgID = t.ID AND d.DeviceType= 8
    """