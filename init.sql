-- データベースを作成
CREATE DATABASE IF NOT EXISTS demo_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 作成したデータベースを使用
USE demo_database;

-- テーブルを作成
CREATE TABLE  IF NOT EXISTS demo_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    text TEXT
);

-- サンプルデータの挿入（オプション）
-- INSERT INTO demo_table (name, text) VALUES
-- ('name1', 'text1'),
-- ('name2', 'text2');
