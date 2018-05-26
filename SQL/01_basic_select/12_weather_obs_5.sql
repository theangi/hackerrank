select * from (
    select city, length(city)
    from station
    order by length(city) asc, city asc
) a where a.rownum <= 1
;

select * from (
    select city, length(city)
    from station
    order by length(city) desc, city asc
) a where a.rownum <= 1
;
