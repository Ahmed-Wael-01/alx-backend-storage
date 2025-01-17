-- list long lasted glam rock band
SELECT `band_name`, IFNULL(`split`, '2022') - `formed` AS lifespan FROM metal_bands WHERE `style` REGEXP 'Glam rock?' ORDER BY IFNULL(`split`, '2022') - `formed` DESC;
