-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts hbtn_0c_0.first_table table to UTF8
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts hbtn_0c_0.first_table.name field to UTF8
ALTER TABLE hbtn_0c_0.first_table MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
