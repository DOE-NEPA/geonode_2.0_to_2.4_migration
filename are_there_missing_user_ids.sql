select user_id from (
select user_id from account_account
union
select user_id from account_accountdeletion
union
select user_id from account_emailaddress
union
select inviter_id from account_signupcode
union
select user_id from account_signupcoderesult
union
select user_id from actstream_follow
union
select user_id from agon_ratings_rating
union
select creator_id from announcements_announcement
union
select user_id from announcements_dismissal
union
select user_id from auth_user_groups
union
select user_id from auth_user_user_permissions
union
select user_id from avatar_avatar
union
select owner_id from base_resourcebase
union
select author_id from dialogos_comment
union
select user_id from django_admin_log
union
select user_id from django_comment_flags
union
select user_id from django_comments
union
select user_id from notification_noticesetting
union
select user_id from people_profile
union
select user_id from security_userobjectrolemapping
union
select user_id from upload_upload
union
select sender_id from user_messages_message
union
select user_id from user_messages_userthread
union
select author_id from zinnia_entry_authors) v1
where not exists (
select id from auth_user t1 
where  t1.id = v1.user_id)
