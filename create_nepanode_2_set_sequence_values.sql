select 'select setval('''||table_name||'_id_seq'', max(id)) from '||table_name||';' 
from information_schema.tables 
where table_type   = 'BASE TABLE' 
and   table_schema = 'public'  
order by table_name
