delete from moz_historyvisits where place_id in (select id from moz_places where url like '%youtube%'); --delete all records from the history visits table
delete from moz_inputhistory where place_id in (select id from moz_places where url like '%youtube%'); --delete all input history
delete from moz_inputhistory where input like '%youtube%'; --delete all records of typing a particular url
delete from moz_places where url like '%youtube%' and id not in ((select fk from moz_bookmarks) or (select place_id from moz_annos));