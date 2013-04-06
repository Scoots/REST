CREATE SCHEMA `KIXEYE` ;

CREATE  TABLE `KIXEYE`.`USER` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `first_name` VARCHAR(45) NOT NULL ,
  `last_name` VARCHAR(45) NOT NULL ,
  `nickname` VARCHAR(45) NOT NULL ,
  `creation_time` DATETIME NOT NULL ,
  PRIMARY KEY (`user_id`) ,
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) )
COMMENT = 'Stores USER information that is used in the other tables.  Only deals with data that is available at USER creation time.';

CREATE  TABLE `KIXEYE`.`USER_STATISTICS` (
  `user_id` INT NOT NULL ,
  `num_wins` INT NOT NULL ,
  `num_losses` INT NOT NULL ,
  `win_streak` INT NOT NULL ,
  `last_seen_time` DATETIME NULL )
COMMENT = 'This table will hold all statistics relating to a USER';

CREATE  TABLE `KIXEYE`.`BATTLE` (
  `attacker_id` INT NOT NULL ,
  `defender_id` INT NOT NULL ,
  `winner_id` INT NOT NULL ,
  `start_time` DATETIME NOT NULL ,
  `end_time` DATETIME NOT NULL )
COMMENT = 'Stores battle data instance.  The attacker, defender, and winner ids all relate to the USER table.  Any addition to this table should modify the USER_STATISTICS table, incrementing num_wins, num_losses, win_streak';


USE `kixeye`;
DROP procedure IF EXISTS `CreateUser`;

DELIMITER $$
USE `kixeye`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `CreateUser`(
	first_name varchar(45),
	last_name varchar(45),
	nickname varchar(45))
BEGIN
	INSERT INTO kixeye.user(first_name, last_name, nickname, creation_time)
		VALUES (first_name, last_name, nickname, UTC_TIMESTAMP());

	SET @newId = LAST_INSERT_ID();

	INSERT INTO kixeye.user_statistics(user_id, num_wins, num_losses, win_streak)
		VALUES (@newId, 0, 0, 0);
END$$

DELIMITER ;

USE `kixeye`;
DROP procedure IF EXISTS `AddBattle`;

DELIMITER $$
USE `kixeye`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddBattle`(
	attacker INT,
	defender INT,
	winner INT,
	startTime DATETIME,
	endTime DATETIME)
BEGIN
	-- Insert the values into the battle table
	INSERT INTO kixeye.battle(attacker_id, defender_id, winner_id, start_time, end_time)
		VALUES(attacker, defender, winner, startTime, endTime);

	-- Modify the values of the user_statistics table for the winner
	UPDATE kixeye.user_statistics AS us
		SET us.num_wins = us.num_wins + 1, us.win_streak = us.win_streak + 1
		WHERE us.user_id = winner;

	-- Update the losses data
	-- If the winner was the attacker then set loss data on the defender
	-- If the winner was the defender then set loss data on the attacker
	UPDATE kixeye.user_statistics AS us
		SET us.num_losses = us.num_losses + 1, us.win_streak = 0
		WHERE IF (winner = attacker, us.user_id = defender, us.user_id = attacker);

	-- In the case where the winner is neither the attacker nor defender, this will not behave correctly
	-- In the case where the attacker and defender are the same id, this will not behave correctly
		
END$$

DELIMITER ;


USE `kixeye`;
DROP procedure IF EXISTS `GetUserFromId`;

DELIMITER $$
USE `kixeye`$$
CREATE PROCEDURE `kixeye`.`GetUserFromId` (
	user_id INT)
BEGIN
	SELECT *
	FROM kixeye.user AS u
		INNER JOIN kixeye.user_statistics AS us
		ON us.user_id = user_id
	WHERE u.user_id = user_id;
END$$

DELIMITER ;

USE `kixeye`;
DROP procedure IF EXISTS `GetUserFromNickname`;

DELIMITER $$
USE `kixeye`$$
CREATE PROCEDURE `kixeye`.`GetUserFromNickname` (
	nickname NVARCHAR(45))
BEGIN
	SELECT user_id
		FROM kixeye.user AS u
		WHERE u.nickname = nickname;

	-- This won't work with multiple people who have the same nickname
END$$

DELIMITER ;

USE `kixeye`;
DROP procedure IF EXISTS `ModifyUserFirstName`;

DELIMITER $$
USE `kixeye`$$
CREATE PROCEDURE `kixeye`.`ModifyUserFirstName` (
	user_id INT,
	first_name NVARCHAR(45))
BEGIN
	UPDATE kixeye.user as u
		SET u.first_name = first_name
		WHERE u.user_id = user_id;
END$$

DELIMITER ;

USE `kixeye`;
DROP procedure IF EXISTS `ModifyUserLastName`;

DELIMITER $$
USE `kixeye`$$
CREATE PROCEDURE `kixeye`.`ModifyUserLastName` (
	user_id INT,
	last_name NVARCHAR(45))
BEGIN
	UPDATE kixeye.user AS u
		SET u.last_name = last_name
		WHERE u.user_id = user_id;
END$$

DELIMITER ;

USE `kixeye`;
DROP procedure IF EXISTS `ModifyUserNickname`;

DELIMITER $$
USE `kixeye`$$
CREATE PROCEDURE `kixeye`.`ModifyUserNickname` (
	user_id INT,
	nickname NVARCHAR(45))
BEGIN
	UPDATE kixeye.user AS u
		SET u.nickname = nickname
		WHERE u.user_id = user_id;
END$$

DELIMITER ;

