select distinct city
from station
where regexp_like(lower(city), '^(.*)[^aeiou]$')
and regexp_like(lower(city), '^[^aeiou].*')
;
