-- ranks origins of bands
SELECT `origin`, SUM(`fans`) AS nb_fans FROM metal_bands GROUP BY `origin` ORDER BY SUM(`fans`) DESC;
