SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tv
-- -----------------------------------------------------
DROP database IF EXISTS `tv` ;

-- -----------------------------------------------------
-- Schema tv
-- -----------------------------------------------------
CREATE database IF NOT EXISTS `tv` DEFAULT CHARACTER SET utf8 ;
USE `tv` ;

-- -----------------------------------------------------
-- Table `tv`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`User` ;

CREATE TABLE IF NOT EXISTS `tv`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NULL,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tv`.`Genres`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`Genres` ;

CREATE TABLE IF NOT EXISTS `tv`.`Genres` (
  `genre_id` INT NOT NULL,
  `genre` VARCHAR(45) NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tv`.`Shows`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`Shows` ;

CREATE TABLE IF NOT EXISTS `tv`.`Shows` (
  `show_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `creator` VARCHAR(45) NULL,
  `seasonCount` INT NULL,
  `yearsRunning` INT NULL,
  `release_year` INT NULL,
  `genre_id` INT NULL,
  PRIMARY KEY (`show_id`),
  INDEX `genre_fk_idx` (`genre_id` ASC) VISIBLE,
  CONSTRAINT `genre_fk`
    FOREIGN KEY (`genre_id`)
    REFERENCES `tv`.`Genres` (`genre_id`)
    ON DELETE Cascade
    ON UPDATE Cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tv`.`Seasons`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`Seasons` ;

CREATE TABLE IF NOT EXISTS `tv`.`Seasons` (
  `seasons_id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `episode_count` INT NULL,
  `playlist_id` INT NULL,
  `show_id` INT NULL,
  PRIMARY KEY (`seasons_id`),
  INDEX `show_name_idx` (`show_id` ASC) VISIBLE,
  CONSTRAINT `show_name`
    FOREIGN KEY (`show_id`)
    REFERENCES `tv`.`Shows` (`show_id`)
    ON DELETE Cascade
    ON UPDATE Cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tv`.`Playlists`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`Playlists` ;

CREATE TABLE IF NOT EXISTS `tv`.`Playlists` (
  `playlist_id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `created` DATETIME NULL,
  `updated` DATETIME NULL,
  `followers` VARCHAR(45) NULL,
  `user_id` INT NULL,
  PRIMARY KEY (`playlist_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `tv`.`User` (`id`)
    ON DELETE Cascade
    ON UPDATE Cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tv`.`Episodes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`Episodes` ;

CREATE TABLE IF NOT EXISTS `tv`.`Episodes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `director` VARCHAR(45) NULL,
  `episodeNo` VARCHAR(45) NULL,
  `length` INT NULL,
  `playlist_id` INT NULL,
  `release_date` DATETIME NULL,
  `genre` VARCHAR(45) NULL,
  `season_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `season_id_idx` (`season_id` ASC) VISIBLE,
  INDEX `playlist_fk_idx` (`playlist_id` ASC) VISIBLE,
  CONSTRAINT `season_id`
    FOREIGN KEY (`season_id`)
    REFERENCES `tv`.`Seasons` (`seasons_id`)
    ON DELETE Cascade
    ON UPDATE Cascade,
  CONSTRAINT `playlist_fk`
    FOREIGN KEY (`playlist_id`)
    REFERENCES `tv`.`Playlists` (`playlist_id`)
    ON DELETE Cascade
    ON UPDATE Cascade)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tv`.`Ratings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tv`.`Ratings` ;

CREATE TABLE IF NOT EXISTS `tv`.`Ratings` (
  `rating_id` INT NOT NULL AUTO_INCREMENT,
  `score` VARCHAR(45) NULL,
  `created` DATETIME NULL,
  `updated` DATETIME NULL,
  `user_id` INT NULL,
  `show_id` INT NULL,
  PRIMARY KEY (`rating_id`),
  INDEX `user_fk_idx` (`user_id` ASC) VISIBLE,
  INDEX `show_fk_idx` (`show_id` ASC) VISIBLE,
  CONSTRAINT `user_fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `tv`.`User` (`id`)
    ON DELETE Cascade
    ON UPDATE Cascade,
  CONSTRAINT `show_fk`
    FOREIGN KEY (`show_id`)
    REFERENCES `tv`.`Shows` (`show_id`)
   ON DELETE Cascade
    ON UPDATE Cascade)
ENGINE = InnoDB;