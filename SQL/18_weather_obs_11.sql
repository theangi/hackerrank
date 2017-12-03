select distinct city
from station
where regexp_like(lower(city), '^(.*)[^aeiou]$')
or regexp_like(lower(city), '^[^aeiou].*')
;