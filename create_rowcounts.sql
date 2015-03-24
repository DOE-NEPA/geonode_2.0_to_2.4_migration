select 'select '''||table_name||''', count(1) as occurs from '||table_name||';' 
from information_schema.tables 
where table_type   = 'BASE TABLE' 
and   table_schema = 'public' 
order by table_name;
