TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`%` TRIGGER `car_before_delete` BEFORE DELETE ON `car` FOR EACH ROW DELETE FROM rating WHERE car_id = OLD.id'
sql_modes=1411383296
definers='root@%'
client_cs_names='utf8mb4'
connection_cl_names='utf8mb4_general_ci'
db_cl_names='utf8mb4_general_ci'
created=162349925118
