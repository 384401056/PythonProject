#!/usr/bin/env python
# -*- coding: utf-8 -*-

sql = """
    SELECT
    t.Address,d.DeviceNo,d.id
    FROM
      t_b_deviceinfo d,
    t_s_org t
    WHERE
    d.OrgID = t.ID AND d.DeviceNo IN (
      '356566072694847',
      '356566072199003',
      '356566072729742',
      '356566072706245',
      '356566072706187',
      '356566072198963',
      '356566072199805',
      '356566072200009',
      '356566072781610',
      '356566072703523',
      '356566072704042',
      '356566072728264',
      '356566072705023',
      '356566072692445',
      '356566072693724',
      '356566072704109',
      '356566072695547',
      '356566072703085',
      '356566072696701',
      '356566072703200',
      '356566072701485',
      '356566072740426',
      '356566072693302',
      '356566072199482',
      '356566072692189',
      '356566072413248',
      '356566072198864',
      '356566072732985',
      '356566072694425',
      '356566072697345',
      '356566072199144',
      '356566072200728',
      '356566072706328',
      '356566072198286',
      '356566072695703',
      '356566074225061',
      '356566072035991',
      '356566072728769',
      '356566072411721',
      '356566072701089',
      '356566072697022',
      '356566072732860',
      '356566072733900',
      '356566072693161',
      '356566072696966',
      '356566072706880',
      '356566072266034',
      '356566072301906',
      '356566072693187',
      '356566072694029',
      '356566072707060',
      '356566072162696',
      '356566072730765',
      '356566072035751',
      '356566072694763',
      '356566072413180',
      '356566072454002',
      '356566072701808',
      '356566072783632',
      '356566072412067',
      '356566072727522',
      '356566072704588',
      '356566072704687',
      '356566072261951',
      '356566072705627',
      '356566072199581',
      '356566072705825',
      '356566072700164',
      '356566072415268',
      '356566072693948',
      '356566072198187',
      '356566072702525',
      '356566072704646',
      '356566072704844',
      '356566072698186',
      '356566072705684',
      '356566072702400',
      '356566072730484',
      '356566072706005',
      '356566072730286',
      '356566072683709',
      '356566072704166',
      '356566072263296',
      '356566072240153',
      '356566072742604',
      '356566072730161',
      '356566072703747',
      '356566072171846',
      '356566072738206',
      '356566072693328',
      '356566072412505',
      '356566072696180',
      '356566072268477',
      '356566072706625',
      '3566566072413248',
      '356566072690548',
      '356566072198948'
    ) and d.DeviceType=  2250
    """