select distinct city
from station
where regexp_like(lower(city), '^[^aeiou].*')
;
