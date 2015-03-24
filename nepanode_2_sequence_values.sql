select max(id) as account_account_max, nextval('account_account_id_seq') as account_account_id_seq from account_account;
select max(id) as account_accountdeletion_max, nextval('account_accountdeletion_id_seq') as account_accountdeletion_id_seq from account_accountdeletion;
select max(id) as account_emailaddress_max, nextval('account_emailaddress_id_seq') as account_emailaddress_id_seq from account_emailaddress;
select max(id) as account_emailconfirmation_max, nextval('account_emailconfirmation_id_seq') as account_emailconfirmation_id_seq from account_emailconfirmation;
select max(id) as account_signupcode_max, nextval('account_signupcode_id_seq') as account_signupcode_id_seq from account_signupcode;
select max(id) as account_signupcodeextended_max, nextval('account_signupcodeextended_id_seq') as account_signupcodeextended_id_seq from account_signupcodeextended;
select max(id) as account_signupcoderesult_max, nextval('account_signupcoderesult_id_seq') as account_signupcoderesult_id_seq from account_signupcoderesult;
select max(id) as actstream_action_max, nextval('actstream_action_id_seq') as actstream_action_id_seq from actstream_action;
select max(id) as actstream_follow_max, nextval('actstream_follow_id_seq') as actstream_follow_id_seq from actstream_follow;
select max(id) as administrable_role_authorizations_max, nextval('administrable_role_authorizations_id_seq') as administrable_role_authorizations_id_seq from administrable_role_authorizations;
select max(id) as agon_ratings_overallrating_max, nextval('agon_ratings_overallrating_id_seq') as agon_ratings_overallrating_id_seq from agon_ratings_overallrating;
select max(id) as agon_ratings_rating_max, nextval('agon_ratings_rating_id_seq') as agon_ratings_rating_id_seq from agon_ratings_rating;
select max(id) as announcements_announcement_max, nextval('announcements_announcement_id_seq') as announcements_announcement_id_seq from announcements_announcement;
select max(id) as announcements_dismissal_max, nextval('announcements_dismissal_id_seq') as announcements_dismissal_id_seq from announcements_dismissal;
select max(id) as applicable_roles_max, nextval('applicable_roles_id_seq') as applicable_roles_id_seq from applicable_roles;
select max(id) as attributes_max, nextval('attributes_id_seq') as attributes_id_seq from attributes;
select max(id) as auth_group_max, nextval('auth_group_id_seq') as auth_group_id_seq from auth_group;
select max(id) as auth_group_permissions_max, nextval('auth_group_permissions_id_seq') as auth_group_permissions_id_seq from auth_group_permissions;
select max(id) as auth_permission_max, nextval('auth_permission_id_seq') as auth_permission_id_seq from auth_permission;
select max(id) as avatar_avatar_max, nextval('avatar_avatar_id_seq') as avatar_avatar_id_seq from avatar_avatar;
select max(id) as base_contactrole_max, nextval('base_contactrole_id_seq') as base_contactrole_id_seq from base_contactrole;
select max(id) as base_license_max, nextval('base_license_id_seq') as base_license_id_seq from base_license;
select max(id) as base_link_max, nextval('base_link_id_seq') as base_link_id_seq from base_link;
select max(id) as base_region_max, nextval('base_region_id_seq') as base_region_id_seq from base_region;
select max(id) as base_resourcebase_max, nextval('base_resourcebase_id_seq') as base_resourcebase_id_seq from base_resourcebase;
select max(id) as base_resourcebase_regions_max, nextval('base_resourcebase_regions_id_seq') as base_resourcebase_regions_id_seq from base_resourcebase_regions;
select max(id) as base_restrictioncodetype_max, nextval('base_restrictioncodetype_id_seq') as base_restrictioncodetype_id_seq from base_restrictioncodetype;
select max(id) as base_spatialrepresentationtype_max, nextval('base_spatialrepresentationtype_id_seq') as base_spatialrepresentationtype_id_seq from base_spatialrepresentationtype;
select max(id) as base_topiccategory_max, nextval('base_topiccategory_id_seq') as base_topiccategory_id_seq from base_topiccategory;
select max(id) as character_sets_max, nextval('character_sets_id_seq') as character_sets_id_seq from character_sets;
select max(id) as check_constraint_routine_usage_max, nextval('check_constraint_routine_usage_id_seq') as check_constraint_routine_usage_id_seq from check_constraint_routine_usage;
select max(id) as check_constraints_max, nextval('check_constraints_id_seq') as check_constraints_id_seq from check_constraints;
select max(id) as collation_character_set_applicability_max, nextval('collation_character_set_applicability_id_seq') as collation_character_set_applicability_id_seq from collation_character_set_applicability;
select max(id) as collations_max, nextval('collations_id_seq') as collations_id_seq from collations;
select max(id) as column_domain_usage_max, nextval('column_domain_usage_id_seq') as column_domain_usage_id_seq from column_domain_usage;
select max(id) as column_options_max, nextval('column_options_id_seq') as column_options_id_seq from column_options;
select max(id) as column_privileges_max, nextval('column_privileges_id_seq') as column_privileges_id_seq from column_privileges;
select max(id) as columns_max, nextval('columns_id_seq') as columns_id_seq from columns;
select max(id) as column_udt_usage_max, nextval('column_udt_usage_id_seq') as column_udt_usage_id_seq from column_udt_usage;
select max(id) as constraint_column_usage_max, nextval('constraint_column_usage_id_seq') as constraint_column_usage_id_seq from constraint_column_usage;
select max(id) as constraint_table_usage_max, nextval('constraint_table_usage_id_seq') as constraint_table_usage_id_seq from constraint_table_usage;
select max(id) as data_type_privileges_max, nextval('data_type_privileges_id_seq') as data_type_privileges_id_seq from data_type_privileges;
select max(id) as dialogos_comment_max, nextval('dialogos_comment_id_seq') as dialogos_comment_id_seq from dialogos_comment;
select max(id) as django_admin_log_max, nextval('django_admin_log_id_seq') as django_admin_log_id_seq from django_admin_log;
select max(id) as django_comment_flags_max, nextval('django_comment_flags_id_seq') as django_comment_flags_id_seq from django_comment_flags;
select max(id) as django_comments_max, nextval('django_comments_id_seq') as django_comments_id_seq from django_comments;
select max(id) as django_content_type_max, nextval('django_content_type_id_seq') as django_content_type_id_seq from django_content_type;
select max(id) as django_session_max, nextval('django_session_id_seq') as django_session_id_seq from django_session;
select max(id) as django_site_max, nextval('django_site_id_seq') as django_site_id_seq from django_site;
select max(id) as documents_document_max, nextval('documents_document_id_seq') as documents_document_id_seq from documents_document;
select max(id) as domain_constraints_max, nextval('domain_constraints_id_seq') as domain_constraints_id_seq from domain_constraints;
select max(id) as domains_max, nextval('domains_id_seq') as domains_id_seq from domains;
select max(id) as domain_udt_usage_max, nextval('domain_udt_usage_id_seq') as domain_udt_usage_id_seq from domain_udt_usage;
select max(id) as element_types_max, nextval('element_types_id_seq') as element_types_id_seq from element_types;
select max(id) as enabled_roles_max, nextval('enabled_roles_id_seq') as enabled_roles_id_seq from enabled_roles;
select max(id) as foreign_data_wrapper_options_max, nextval('foreign_data_wrapper_options_id_seq') as foreign_data_wrapper_options_id_seq from foreign_data_wrapper_options;
select max(id) as foreign_data_wrappers_max, nextval('foreign_data_wrappers_id_seq') as foreign_data_wrappers_id_seq from foreign_data_wrappers;
select max(id) as foreign_server_options_max, nextval('foreign_server_options_id_seq') as foreign_server_options_id_seq from foreign_server_options;
select max(id) as foreign_servers_max, nextval('foreign_servers_id_seq') as foreign_servers_id_seq from foreign_servers;
select max(id) as foreign_table_options_max, nextval('foreign_table_options_id_seq') as foreign_table_options_id_seq from foreign_table_options;
select max(id) as foreign_tables_max, nextval('foreign_tables_id_seq') as foreign_tables_id_seq from foreign_tables;
select max(id) as groups_groupinvitation_max, nextval('groups_groupinvitation_id_seq') as groups_groupinvitation_id_seq from groups_groupinvitation;
select max(id) as groups_groupmember_max, nextval('groups_groupmember_id_seq') as groups_groupmember_id_seq from groups_groupmember;
select max(id) as groups_groupprofile_max, nextval('groups_groupprofile_id_seq') as groups_groupprofile_id_seq from groups_groupprofile;
select max(id) as guardian_groupobjectpermission_max, nextval('guardian_groupobjectpermission_id_seq') as guardian_groupobjectpermission_id_seq from guardian_groupobjectpermission;
select max(id) as guardian_userobjectpermission_max, nextval('guardian_userobjectpermission_id_seq') as guardian_userobjectpermission_id_seq from guardian_userobjectpermission;
select max(id) as helpdesk_attachment_max, nextval('helpdesk_attachment_id_seq') as helpdesk_attachment_id_seq from helpdesk_attachment;
select max(id) as helpdesk_customfield_max, nextval('helpdesk_customfield_id_seq') as helpdesk_customfield_id_seq from helpdesk_customfield;
select max(id) as helpdesk_emailtemplate_max, nextval('helpdesk_emailtemplate_id_seq') as helpdesk_emailtemplate_id_seq from helpdesk_emailtemplate;
select max(id) as helpdesk_escalationexclusion_max, nextval('helpdesk_escalationexclusion_id_seq') as helpdesk_escalationexclusion_id_seq from helpdesk_escalationexclusion;
select max(id) as helpdesk_escalationexclusion_queues_max, nextval('helpdesk_escalationexclusion_queues_id_seq') as helpdesk_escalationexclusion_queues_id_seq from helpdesk_escalationexclusion_queues;
select max(id) as helpdesk_followup_max, nextval('helpdesk_followup_id_seq') as helpdesk_followup_id_seq from helpdesk_followup;
select max(id) as helpdesk_ignoreemail_max, nextval('helpdesk_ignoreemail_id_seq') as helpdesk_ignoreemail_id_seq from helpdesk_ignoreemail;
select max(id) as helpdesk_ignoreemail_queues_max, nextval('helpdesk_ignoreemail_queues_id_seq') as helpdesk_ignoreemail_queues_id_seq from helpdesk_ignoreemail_queues;
select max(id) as helpdesk_kbcategory_max, nextval('helpdesk_kbcategory_id_seq') as helpdesk_kbcategory_id_seq from helpdesk_kbcategory;
select max(id) as helpdesk_kbitem_max, nextval('helpdesk_kbitem_id_seq') as helpdesk_kbitem_id_seq from helpdesk_kbitem;
select max(id) as helpdesk_presetreply_max, nextval('helpdesk_presetreply_id_seq') as helpdesk_presetreply_id_seq from helpdesk_presetreply;
select max(id) as helpdesk_presetreply_queues_max, nextval('helpdesk_presetreply_queues_id_seq') as helpdesk_presetreply_queues_id_seq from helpdesk_presetreply_queues;
select max(id) as helpdesk_queue_max, nextval('helpdesk_queue_id_seq') as helpdesk_queue_id_seq from helpdesk_queue;
select max(id) as helpdesk_savedsearch_max, nextval('helpdesk_savedsearch_id_seq') as helpdesk_savedsearch_id_seq from helpdesk_savedsearch;
select max(id) as helpdesk_ticket_max, nextval('helpdesk_ticket_id_seq') as helpdesk_ticket_id_seq from helpdesk_ticket;
select max(id) as helpdesk_ticketcc_max, nextval('helpdesk_ticketcc_id_seq') as helpdesk_ticketcc_id_seq from helpdesk_ticketcc;
select max(id) as helpdesk_ticketchange_max, nextval('helpdesk_ticketchange_id_seq') as helpdesk_ticketchange_id_seq from helpdesk_ticketchange;
select max(id) as helpdesk_ticketcustomfieldvalue_max, nextval('helpdesk_ticketcustomfieldvalue_id_seq') as helpdesk_ticketcustomfieldvalue_id_seq from helpdesk_ticketcustomfieldvalue;
select max(id) as helpdesk_ticketdependency_max, nextval('helpdesk_ticketdependency_id_seq') as helpdesk_ticketdependency_id_seq from helpdesk_ticketdependency;
select max(id) as helpdesk_usersettings_max, nextval('helpdesk_usersettings_id_seq') as helpdesk_usersettings_id_seq from helpdesk_usersettings;
select max(id) as information_schema_catalog_name_max, nextval('information_schema_catalog_name_id_seq') as information_schema_catalog_name_id_seq from information_schema_catalog_name;
select max(id) as key_column_usage_max, nextval('key_column_usage_id_seq') as key_column_usage_id_seq from key_column_usage;
select max(id) as layers_attribute_max, nextval('layers_attribute_id_seq') as layers_attribute_id_seq from layers_attribute;
select max(id) as layers_layer_max, nextval('layers_layer_id_seq') as layers_layer_id_seq from layers_layer;
select max(id) as layers_layerfile_max, nextval('layers_layerfile_id_seq') as layers_layerfile_id_seq from layers_layerfile;
select max(id) as layers_layer_styles_max, nextval('layers_layer_styles_id_seq') as layers_layer_styles_id_seq from layers_layer_styles;
select max(id) as layers_style_max, nextval('layers_style_id_seq') as layers_style_id_seq from layers_style;
select max(id) as layers_uploadsession_max, nextval('layers_uploadsession_id_seq') as layers_uploadsession_id_seq from layers_uploadsession;
select max(id) as maps_map_max, nextval('maps_map_id_seq') as maps_map_id_seq from maps_map;
select max(id) as maps_maplayer_max, nextval('maps_maplayer_id_seq') as maps_maplayer_id_seq from maps_maplayer;
select max(id) as maps_mapsnapshot_max, nextval('maps_mapsnapshot_id_seq') as maps_mapsnapshot_id_seq from maps_mapsnapshot;
select max(id) as notification_noticequeuebatch_max, nextval('notification_noticequeuebatch_id_seq') as notification_noticequeuebatch_id_seq from notification_noticequeuebatch;
select max(id) as notification_noticesetting_max, nextval('notification_noticesetting_id_seq') as notification_noticesetting_id_seq from notification_noticesetting;
select max(id) as notification_noticetype_max, nextval('notification_noticetype_id_seq') as notification_noticetype_id_seq from notification_noticetype;
select max(id) as parameters_max, nextval('parameters_id_seq') as parameters_id_seq from parameters;
select max(id) as people_profile_max, nextval('people_profile_id_seq') as people_profile_id_seq from people_profile;
select max(id) as people_profile_groups_max, nextval('people_profile_groups_id_seq') as people_profile_groups_id_seq from people_profile_groups;
select max(id) as people_profile_user_permissions_max, nextval('people_profile_user_permissions_id_seq') as people_profile_user_permissions_id_seq from people_profile_user_permissions;
select max(id) as pg_aggregate_max, nextval('pg_aggregate_id_seq') as pg_aggregate_id_seq from pg_aggregate;
select max(id) as pg_am_max, nextval('pg_am_id_seq') as pg_am_id_seq from pg_am;
select max(id) as pg_amop_max, nextval('pg_amop_id_seq') as pg_amop_id_seq from pg_amop;
select max(id) as pg_amproc_max, nextval('pg_amproc_id_seq') as pg_amproc_id_seq from pg_amproc;
select max(id) as pg_attrdef_max, nextval('pg_attrdef_id_seq') as pg_attrdef_id_seq from pg_attrdef;
select max(id) as pg_attribute_max, nextval('pg_attribute_id_seq') as pg_attribute_id_seq from pg_attribute;
select max(id) as pg_authid_max, nextval('pg_authid_id_seq') as pg_authid_id_seq from pg_authid;
select max(id) as pg_auth_members_max, nextval('pg_auth_members_id_seq') as pg_auth_members_id_seq from pg_auth_members;
select max(id) as pg_available_extensions_max, nextval('pg_available_extensions_id_seq') as pg_available_extensions_id_seq from pg_available_extensions;
select max(id) as pg_available_extension_versions_max, nextval('pg_available_extension_versions_id_seq') as pg_available_extension_versions_id_seq from pg_available_extension_versions;
select max(id) as pg_cast_max, nextval('pg_cast_id_seq') as pg_cast_id_seq from pg_cast;
select max(id) as pg_class_max, nextval('pg_class_id_seq') as pg_class_id_seq from pg_class;
select max(id) as pg_collation_max, nextval('pg_collation_id_seq') as pg_collation_id_seq from pg_collation;
select max(id) as pg_constraint_max, nextval('pg_constraint_id_seq') as pg_constraint_id_seq from pg_constraint;
select max(id) as pg_conversion_max, nextval('pg_conversion_id_seq') as pg_conversion_id_seq from pg_conversion;
select max(id) as pg_cursors_max, nextval('pg_cursors_id_seq') as pg_cursors_id_seq from pg_cursors;
select max(id) as pg_database_max, nextval('pg_database_id_seq') as pg_database_id_seq from pg_database;
select max(id) as pg_db_role_setting_max, nextval('pg_db_role_setting_id_seq') as pg_db_role_setting_id_seq from pg_db_role_setting;
select max(id) as pg_default_acl_max, nextval('pg_default_acl_id_seq') as pg_default_acl_id_seq from pg_default_acl;
select max(id) as pg_depend_max, nextval('pg_depend_id_seq') as pg_depend_id_seq from pg_depend;
select max(id) as pg_description_max, nextval('pg_description_id_seq') as pg_description_id_seq from pg_description;
select max(id) as pg_enum_max, nextval('pg_enum_id_seq') as pg_enum_id_seq from pg_enum;
select max(id) as pg_event_trigger_max, nextval('pg_event_trigger_id_seq') as pg_event_trigger_id_seq from pg_event_trigger;
select max(id) as pg_extension_max, nextval('pg_extension_id_seq') as pg_extension_id_seq from pg_extension;
select max(id) as pg_foreign_data_wrapper_max, nextval('pg_foreign_data_wrapper_id_seq') as pg_foreign_data_wrapper_id_seq from pg_foreign_data_wrapper;
select max(id) as _pg_foreign_data_wrappers_max, nextval('_pg_foreign_data_wrappers_id_seq') as _pg_foreign_data_wrappers_id_seq from _pg_foreign_data_wrappers;
select max(id) as pg_foreign_server_max, nextval('pg_foreign_server_id_seq') as pg_foreign_server_id_seq from pg_foreign_server;
select max(id) as _pg_foreign_servers_max, nextval('_pg_foreign_servers_id_seq') as _pg_foreign_servers_id_seq from _pg_foreign_servers;
select max(id) as pg_foreign_table_max, nextval('pg_foreign_table_id_seq') as pg_foreign_table_id_seq from pg_foreign_table;
select max(id) as _pg_foreign_table_columns_max, nextval('_pg_foreign_table_columns_id_seq') as _pg_foreign_table_columns_id_seq from _pg_foreign_table_columns;
select max(id) as _pg_foreign_tables_max, nextval('_pg_foreign_tables_id_seq') as _pg_foreign_tables_id_seq from _pg_foreign_tables;
select max(id) as pg_group_max, nextval('pg_group_id_seq') as pg_group_id_seq from pg_group;
select max(id) as pg_index_max, nextval('pg_index_id_seq') as pg_index_id_seq from pg_index;
select max(id) as pg_indexes_max, nextval('pg_indexes_id_seq') as pg_indexes_id_seq from pg_indexes;
select max(id) as pg_inherits_max, nextval('pg_inherits_id_seq') as pg_inherits_id_seq from pg_inherits;
select max(id) as pg_language_max, nextval('pg_language_id_seq') as pg_language_id_seq from pg_language;
select max(id) as pg_largeobject_max, nextval('pg_largeobject_id_seq') as pg_largeobject_id_seq from pg_largeobject;
select max(id) as pg_largeobject_metadata_max, nextval('pg_largeobject_metadata_id_seq') as pg_largeobject_metadata_id_seq from pg_largeobject_metadata;
select max(id) as pg_locks_max, nextval('pg_locks_id_seq') as pg_locks_id_seq from pg_locks;
select max(id) as pg_matviews_max, nextval('pg_matviews_id_seq') as pg_matviews_id_seq from pg_matviews;
select max(id) as pg_namespace_max, nextval('pg_namespace_id_seq') as pg_namespace_id_seq from pg_namespace;
select max(id) as pg_opclass_max, nextval('pg_opclass_id_seq') as pg_opclass_id_seq from pg_opclass;
select max(id) as pg_operator_max, nextval('pg_operator_id_seq') as pg_operator_id_seq from pg_operator;
select max(id) as pg_opfamily_max, nextval('pg_opfamily_id_seq') as pg_opfamily_id_seq from pg_opfamily;
select max(id) as pg_pltemplate_max, nextval('pg_pltemplate_id_seq') as pg_pltemplate_id_seq from pg_pltemplate;
select max(id) as pg_prepared_statements_max, nextval('pg_prepared_statements_id_seq') as pg_prepared_statements_id_seq from pg_prepared_statements;
select max(id) as pg_prepared_xacts_max, nextval('pg_prepared_xacts_id_seq') as pg_prepared_xacts_id_seq from pg_prepared_xacts;
select max(id) as pg_proc_max, nextval('pg_proc_id_seq') as pg_proc_id_seq from pg_proc;
select max(id) as pg_range_max, nextval('pg_range_id_seq') as pg_range_id_seq from pg_range;
select max(id) as pg_rewrite_max, nextval('pg_rewrite_id_seq') as pg_rewrite_id_seq from pg_rewrite;
select max(id) as pg_roles_max, nextval('pg_roles_id_seq') as pg_roles_id_seq from pg_roles;
select max(id) as pg_rules_max, nextval('pg_rules_id_seq') as pg_rules_id_seq from pg_rules;
select max(id) as pg_seclabel_max, nextval('pg_seclabel_id_seq') as pg_seclabel_id_seq from pg_seclabel;
select max(id) as pg_seclabels_max, nextval('pg_seclabels_id_seq') as pg_seclabels_id_seq from pg_seclabels;
select max(id) as pg_settings_max, nextval('pg_settings_id_seq') as pg_settings_id_seq from pg_settings;
select max(id) as pg_shadow_max, nextval('pg_shadow_id_seq') as pg_shadow_id_seq from pg_shadow;
select max(id) as pg_shdepend_max, nextval('pg_shdepend_id_seq') as pg_shdepend_id_seq from pg_shdepend;
select max(id) as pg_shdescription_max, nextval('pg_shdescription_id_seq') as pg_shdescription_id_seq from pg_shdescription;
select max(id) as pg_shseclabel_max, nextval('pg_shseclabel_id_seq') as pg_shseclabel_id_seq from pg_shseclabel;
select max(id) as pg_stat_activity_max, nextval('pg_stat_activity_id_seq') as pg_stat_activity_id_seq from pg_stat_activity;
select max(id) as pg_stat_all_indexes_max, nextval('pg_stat_all_indexes_id_seq') as pg_stat_all_indexes_id_seq from pg_stat_all_indexes;
select max(id) as pg_stat_all_tables_max, nextval('pg_stat_all_tables_id_seq') as pg_stat_all_tables_id_seq from pg_stat_all_tables;
select max(id) as pg_stat_bgwriter_max, nextval('pg_stat_bgwriter_id_seq') as pg_stat_bgwriter_id_seq from pg_stat_bgwriter;
select max(id) as pg_stat_database_max, nextval('pg_stat_database_id_seq') as pg_stat_database_id_seq from pg_stat_database;
select max(id) as pg_stat_database_conflicts_max, nextval('pg_stat_database_conflicts_id_seq') as pg_stat_database_conflicts_id_seq from pg_stat_database_conflicts;
select max(id) as pg_statio_all_indexes_max, nextval('pg_statio_all_indexes_id_seq') as pg_statio_all_indexes_id_seq from pg_statio_all_indexes;
select max(id) as pg_statio_all_sequences_max, nextval('pg_statio_all_sequences_id_seq') as pg_statio_all_sequences_id_seq from pg_statio_all_sequences;
select max(id) as pg_statio_all_tables_max, nextval('pg_statio_all_tables_id_seq') as pg_statio_all_tables_id_seq from pg_statio_all_tables;
select max(id) as pg_statio_sys_indexes_max, nextval('pg_statio_sys_indexes_id_seq') as pg_statio_sys_indexes_id_seq from pg_statio_sys_indexes;
select max(id) as pg_statio_sys_sequences_max, nextval('pg_statio_sys_sequences_id_seq') as pg_statio_sys_sequences_id_seq from pg_statio_sys_sequences;
select max(id) as pg_statio_sys_tables_max, nextval('pg_statio_sys_tables_id_seq') as pg_statio_sys_tables_id_seq from pg_statio_sys_tables;
select max(id) as pg_statio_user_indexes_max, nextval('pg_statio_user_indexes_id_seq') as pg_statio_user_indexes_id_seq from pg_statio_user_indexes;
select max(id) as pg_statio_user_sequences_max, nextval('pg_statio_user_sequences_id_seq') as pg_statio_user_sequences_id_seq from pg_statio_user_sequences;
select max(id) as pg_statio_user_tables_max, nextval('pg_statio_user_tables_id_seq') as pg_statio_user_tables_id_seq from pg_statio_user_tables;
select max(id) as pg_statistic_max, nextval('pg_statistic_id_seq') as pg_statistic_id_seq from pg_statistic;
select max(id) as pg_stat_replication_max, nextval('pg_stat_replication_id_seq') as pg_stat_replication_id_seq from pg_stat_replication;
select max(id) as pg_stats_max, nextval('pg_stats_id_seq') as pg_stats_id_seq from pg_stats;
select max(id) as pg_stat_sys_indexes_max, nextval('pg_stat_sys_indexes_id_seq') as pg_stat_sys_indexes_id_seq from pg_stat_sys_indexes;
select max(id) as pg_stat_sys_tables_max, nextval('pg_stat_sys_tables_id_seq') as pg_stat_sys_tables_id_seq from pg_stat_sys_tables;
select max(id) as pg_stat_user_functions_max, nextval('pg_stat_user_functions_id_seq') as pg_stat_user_functions_id_seq from pg_stat_user_functions;
select max(id) as pg_stat_user_indexes_max, nextval('pg_stat_user_indexes_id_seq') as pg_stat_user_indexes_id_seq from pg_stat_user_indexes;
select max(id) as pg_stat_user_tables_max, nextval('pg_stat_user_tables_id_seq') as pg_stat_user_tables_id_seq from pg_stat_user_tables;
select max(id) as pg_stat_xact_all_tables_max, nextval('pg_stat_xact_all_tables_id_seq') as pg_stat_xact_all_tables_id_seq from pg_stat_xact_all_tables;
select max(id) as pg_stat_xact_sys_tables_max, nextval('pg_stat_xact_sys_tables_id_seq') as pg_stat_xact_sys_tables_id_seq from pg_stat_xact_sys_tables;
select max(id) as pg_stat_xact_user_functions_max, nextval('pg_stat_xact_user_functions_id_seq') as pg_stat_xact_user_functions_id_seq from pg_stat_xact_user_functions;
select max(id) as pg_stat_xact_user_tables_max, nextval('pg_stat_xact_user_tables_id_seq') as pg_stat_xact_user_tables_id_seq from pg_stat_xact_user_tables;
select max(id) as pg_tables_max, nextval('pg_tables_id_seq') as pg_tables_id_seq from pg_tables;
select max(id) as pg_tablespace_max, nextval('pg_tablespace_id_seq') as pg_tablespace_id_seq from pg_tablespace;
select max(id) as pg_timezone_abbrevs_max, nextval('pg_timezone_abbrevs_id_seq') as pg_timezone_abbrevs_id_seq from pg_timezone_abbrevs;
select max(id) as pg_timezone_names_max, nextval('pg_timezone_names_id_seq') as pg_timezone_names_id_seq from pg_timezone_names;
select max(id) as pg_trigger_max, nextval('pg_trigger_id_seq') as pg_trigger_id_seq from pg_trigger;
select max(id) as pg_ts_config_max, nextval('pg_ts_config_id_seq') as pg_ts_config_id_seq from pg_ts_config;
select max(id) as pg_ts_config_map_max, nextval('pg_ts_config_map_id_seq') as pg_ts_config_map_id_seq from pg_ts_config_map;
select max(id) as pg_ts_dict_max, nextval('pg_ts_dict_id_seq') as pg_ts_dict_id_seq from pg_ts_dict;
select max(id) as pg_ts_parser_max, nextval('pg_ts_parser_id_seq') as pg_ts_parser_id_seq from pg_ts_parser;
select max(id) as pg_ts_template_max, nextval('pg_ts_template_id_seq') as pg_ts_template_id_seq from pg_ts_template;
select max(id) as pg_type_max, nextval('pg_type_id_seq') as pg_type_id_seq from pg_type;
select max(id) as pg_user_max, nextval('pg_user_id_seq') as pg_user_id_seq from pg_user;
select max(id) as pg_user_mapping_max, nextval('pg_user_mapping_id_seq') as pg_user_mapping_id_seq from pg_user_mapping;
select max(id) as _pg_user_mappings_max, nextval('_pg_user_mappings_id_seq') as _pg_user_mappings_id_seq from _pg_user_mappings;
select max(id) as pg_user_mappings_max, nextval('pg_user_mappings_id_seq') as pg_user_mappings_id_seq from pg_user_mappings;
select max(id) as pg_views_max, nextval('pg_views_id_seq') as pg_views_id_seq from pg_views;
select max(id) as referential_constraints_max, nextval('referential_constraints_id_seq') as referential_constraints_id_seq from referential_constraints;
select max(id) as role_column_grants_max, nextval('role_column_grants_id_seq') as role_column_grants_id_seq from role_column_grants;
select max(id) as role_routine_grants_max, nextval('role_routine_grants_id_seq') as role_routine_grants_id_seq from role_routine_grants;
select max(id) as role_table_grants_max, nextval('role_table_grants_id_seq') as role_table_grants_id_seq from role_table_grants;
select max(id) as role_udt_grants_max, nextval('role_udt_grants_id_seq') as role_udt_grants_id_seq from role_udt_grants;
select max(id) as role_usage_grants_max, nextval('role_usage_grants_id_seq') as role_usage_grants_id_seq from role_usage_grants;
select max(id) as routine_privileges_max, nextval('routine_privileges_id_seq') as routine_privileges_id_seq from routine_privileges;
select max(id) as routines_max, nextval('routines_id_seq') as routines_id_seq from routines;
select max(id) as schemata_max, nextval('schemata_id_seq') as schemata_id_seq from schemata;
select max(id) as sequences_max, nextval('sequences_id_seq') as sequences_id_seq from sequences;
select max(id) as services_service_max, nextval('services_service_id_seq') as services_service_id_seq from services_service;
select max(id) as services_servicelayer_max, nextval('services_servicelayer_id_seq') as services_servicelayer_id_seq from services_servicelayer;
select max(id) as services_serviceprofilerole_max, nextval('services_serviceprofilerole_id_seq') as services_serviceprofilerole_id_seq from services_serviceprofilerole;
select max(id) as services_webserviceharvestlayersjob_max, nextval('services_webserviceharvestlayersjob_id_seq') as services_webserviceharvestlayersjob_id_seq from services_webserviceharvestlayersjob;
select max(id) as services_webserviceregistrationjob_max, nextval('services_webserviceregistrationjob_id_seq') as services_webserviceregistrationjob_id_seq from services_webserviceregistrationjob;
select max(id) as social_auth_association_max, nextval('social_auth_association_id_seq') as social_auth_association_id_seq from social_auth_association;
select max(id) as social_auth_code_max, nextval('social_auth_code_id_seq') as social_auth_code_id_seq from social_auth_code;
select max(id) as social_auth_nonce_max, nextval('social_auth_nonce_id_seq') as social_auth_nonce_id_seq from social_auth_nonce;
select max(id) as social_auth_usersocialauth_max, nextval('social_auth_usersocialauth_id_seq') as social_auth_usersocialauth_id_seq from social_auth_usersocialauth;
select max(id) as south_migrationhistory_max, nextval('south_migrationhistory_id_seq') as south_migrationhistory_id_seq from south_migrationhistory;
select max(id) as sql_features_max, nextval('sql_features_id_seq') as sql_features_id_seq from sql_features;
select max(id) as sql_implementation_info_max, nextval('sql_implementation_info_id_seq') as sql_implementation_info_id_seq from sql_implementation_info;
select max(id) as sql_languages_max, nextval('sql_languages_id_seq') as sql_languages_id_seq from sql_languages;
select max(id) as sql_packages_max, nextval('sql_packages_id_seq') as sql_packages_id_seq from sql_packages;
select max(id) as sql_parts_max, nextval('sql_parts_id_seq') as sql_parts_id_seq from sql_parts;
select max(id) as sql_sizing_max, nextval('sql_sizing_id_seq') as sql_sizing_id_seq from sql_sizing;
select max(id) as sql_sizing_profiles_max, nextval('sql_sizing_profiles_id_seq') as sql_sizing_profiles_id_seq from sql_sizing_profiles;
select max(id) as table_constraints_max, nextval('table_constraints_id_seq') as table_constraints_id_seq from table_constraints;
select max(id) as table_privileges_max, nextval('table_privileges_id_seq') as table_privileges_id_seq from table_privileges;
select max(id) as tables_max, nextval('tables_id_seq') as tables_id_seq from tables;
select max(id) as tagging_tag_max, nextval('tagging_tag_id_seq') as tagging_tag_id_seq from tagging_tag;
select max(id) as tagging_taggeditem_max, nextval('tagging_taggeditem_id_seq') as tagging_taggeditem_id_seq from tagging_taggeditem;
select max(id) as taggit_tag_max, nextval('taggit_tag_id_seq') as taggit_tag_id_seq from taggit_tag;
select max(id) as taggit_taggeditem_max, nextval('taggit_taggeditem_id_seq') as taggit_taggeditem_id_seq from taggit_taggeditem;
select max(id) as tastypie_apiaccess_max, nextval('tastypie_apiaccess_id_seq') as tastypie_apiaccess_id_seq from tastypie_apiaccess;
select max(id) as tastypie_apikey_max, nextval('tastypie_apikey_id_seq') as tastypie_apikey_id_seq from tastypie_apikey;
select max(id) as triggered_update_columns_max, nextval('triggered_update_columns_id_seq') as triggered_update_columns_id_seq from triggered_update_columns;
select max(id) as triggers_max, nextval('triggers_id_seq') as triggers_id_seq from triggers;
select max(id) as udt_privileges_max, nextval('udt_privileges_id_seq') as udt_privileges_id_seq from udt_privileges;
select max(id) as upload_upload_max, nextval('upload_upload_id_seq') as upload_upload_id_seq from upload_upload;
select max(id) as upload_uploadfile_max, nextval('upload_uploadfile_id_seq') as upload_uploadfile_id_seq from upload_uploadfile;
select max(id) as usage_privileges_max, nextval('usage_privileges_id_seq') as usage_privileges_id_seq from usage_privileges;
select max(id) as user_defined_types_max, nextval('user_defined_types_id_seq') as user_defined_types_id_seq from user_defined_types;
select max(id) as user_mapping_options_max, nextval('user_mapping_options_id_seq') as user_mapping_options_id_seq from user_mapping_options;
select max(id) as user_mappings_max, nextval('user_mappings_id_seq') as user_mappings_id_seq from user_mappings;
select max(id) as user_messages_message_max, nextval('user_messages_message_id_seq') as user_messages_message_id_seq from user_messages_message;
select max(id) as user_messages_thread_max, nextval('user_messages_thread_id_seq') as user_messages_thread_id_seq from user_messages_thread;
select max(id) as user_messages_userthread_max, nextval('user_messages_userthread_id_seq') as user_messages_userthread_id_seq from user_messages_userthread;
select max(id) as view_column_usage_max, nextval('view_column_usage_id_seq') as view_column_usage_id_seq from view_column_usage;
select max(id) as view_routine_usage_max, nextval('view_routine_usage_id_seq') as view_routine_usage_id_seq from view_routine_usage;
select max(id) as views_max, nextval('views_id_seq') as views_id_seq from views;
select max(id) as view_table_usage_max, nextval('view_table_usage_id_seq') as view_table_usage_id_seq from view_table_usage;
select max(id) as zinnia_category_max, nextval('zinnia_category_id_seq') as zinnia_category_id_seq from zinnia_category;
select max(id) as zinnia_entry_max, nextval('zinnia_entry_id_seq') as zinnia_entry_id_seq from zinnia_entry;
select max(id) as zinnia_entry_authors_max, nextval('zinnia_entry_authors_id_seq') as zinnia_entry_authors_id_seq from zinnia_entry_authors;
select max(id) as zinnia_entry_categories_max, nextval('zinnia_entry_categories_id_seq') as zinnia_entry_categories_id_seq from zinnia_entry_categories;
select max(id) as zinnia_entry_related_max, nextval('zinnia_entry_related_id_seq') as zinnia_entry_related_id_seq from zinnia_entry_related;
select max(id) as zinnia_entry_sites_max, nextval('zinnia_entry_sites_id_seq') as zinnia_entry_sites_id_seq from zinnia_entry_sites;
select max(id) as zinnia_tinymce_filemodel_max, nextval('zinnia_tinymce_filemodel_id_seq') as zinnia_tinymce_filemodel_id_seq from zinnia_tinymce_filemodel;