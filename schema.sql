
CREATE TABLE `Users` (
  `user_id` INTEGER,
  `email` VARCHAR(64),
  `password` VARCHAR(10),
  `name` VARCHAR(40),
  PRIMARY KEY (`user_id`)
);

    
CREATE TABLE `Tasks` (
  `task_id` INTEGER,
  `title` VARCHAR(40) ,
  `created_at` DATETIME ,
  `completed_at` DATETIME ,
  `user_id` INTEGER ,
  PRIMARY KEY (`task_id`)
);

