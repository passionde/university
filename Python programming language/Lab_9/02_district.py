#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Lab_9.district.central_street.house1.room1
import Lab_9.district.central_street.house1.room2
import Lab_9.district.central_street.house2.room1
import Lab_9.district.central_street.house2.room2

import Lab_9.district.soviet_street.house1.room1
import Lab_9.district.soviet_street.house1.room2
import Lab_9.district.soviet_street.house2.room1
import Lab_9.district.soviet_street.house2.room2


residents = []

residents.extend(Lab_9.district.central_street.house1.room1.folks)
residents.extend(Lab_9.district.central_street.house1.room2.folks)
residents.extend(Lab_9.district.central_street.house2.room1.folks)
residents.extend(Lab_9.district.central_street.house2.room2.folks)

residents.extend(Lab_9.district.soviet_street.house1.room1.folks)
residents.extend(Lab_9.district.soviet_street.house1.room2.folks)
residents.extend(Lab_9.district.soviet_street.house2.room1.folks)
residents.extend(Lab_9.district.soviet_street.house2.room2.folks)


print(f"На районе живут: {', '.join(residents)}")