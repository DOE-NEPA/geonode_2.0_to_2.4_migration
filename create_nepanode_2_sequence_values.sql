select 'select max(id) as '||table_name||'_max, nextval('''||table_name||'_id_seq'') as '||table_name||'_id_seq from '||table_name||';' from information_schema.tables order by table_name
