
CREATE TABLE ports (
    port_id INT PRIMARY KEY,
    port_name VARCHAR(50),
    country VARCHAR(50)
);

INSERT INTO ports VALUES (1, 'Rotterdam', 'Netherlands');
INSERT INTO ports VALUES (2, 'Singapore', 'Singapore');
INSERT INTO ports VALUES (3, 'Shanghai', 'China');
INSERT INTO ports VALUES (4, 'Fujairah', 'UAE');
INSERT INTO ports VALUES (5, 'Busan', 'South Korea');
INSERT INTO ports VALUES (6, 'Antwerp', 'Belgium');
INSERT INTO ports VALUES (7, 'Hamburg', 'Germany');
INSERT INTO ports VALUES (8, 'Los Angeles', 'USA');

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(50),
    rating INT
);

INSERT INTO suppliers VALUES (1, 'Shell', 4);
INSERT INTO suppliers VALUES (2, 'BP', 5);
INSERT INTO suppliers VALUES (3, 'Total', 4);
INSERT INTO suppliers VALUES (4, 'Emirates Fuel', 4);
INSERT INTO suppliers VALUES (5, 'Chevron', 5);
INSERT INTO suppliers VALUES (6, 'PetroChina', 4);

CREATE TABLE fuel_prices (
    id INT PRIMARY KEY,
    port VARCHAR(50),
    fuel_type VARCHAR(20),
    price DECIMAL(10,2),
    date DATE
);

INSERT INTO fuel_prices VALUES (1, 'Singapore', 'MGO', 520, '2024-02-12');
INSERT INTO fuel_prices VALUES (2, 'Los Angeles', 'MGO', 489, '2024-01-15');
INSERT INTO fuel_prices VALUES (3, 'Singapore', 'IFO380', 458, '2024-01-01');
INSERT INTO fuel_prices VALUES (4, 'Los Angeles', 'IFO380', 456, '2024-03-04');
INSERT INTO fuel_prices VALUES (5, 'Singapore', 'VLSFO', 513, '2024-03-26');
INSERT INTO fuel_prices VALUES (6, 'Shanghai', 'IFO380', 525, '2024-01-01');
INSERT INTO fuel_prices VALUES (7, 'Shanghai', 'MGO', 629, '2024-03-01');
INSERT INTO fuel_prices VALUES (8, 'Busan', 'MGO', 629, '2024-02-27');
INSERT INTO fuel_prices VALUES (9, 'Singapore', 'MGO', 637, '2024-02-02');
INSERT INTO fuel_prices VALUES (10, 'Los Angeles', 'MGO', 558, '2024-02-10');
INSERT INTO fuel_prices VALUES (11, 'Rotterdam', 'VLSFO', 574, '2024-01-24');
INSERT INTO fuel_prices VALUES (12, 'Busan', 'MGO', 621, '2024-03-19');
INSERT INTO fuel_prices VALUES (13, 'Rotterdam', 'MGO', 495, '2024-02-16');
INSERT INTO fuel_prices VALUES (14, 'Singapore', 'IFO380', 453, '2024-02-19');
INSERT INTO fuel_prices VALUES (15, 'Busan', 'VLSFO', 525, '2024-03-07');
INSERT INTO fuel_prices VALUES (16, 'Busan', 'IFO380', 546, '2024-02-20');
INSERT INTO fuel_prices VALUES (17, 'Shanghai', 'VLSFO', 544, '2024-02-07');
INSERT INTO fuel_prices VALUES (18, 'Shanghai', 'IFO380', 635, '2024-03-25');
INSERT INTO fuel_prices VALUES (19, 'Singapore', 'VLSFO', 470, '2024-03-18');
INSERT INTO fuel_prices VALUES (20, 'Singapore', 'MGO', 577, '2024-02-27');
INSERT INTO fuel_prices VALUES (21, 'Fujairah', 'IFO380', 597, '2024-01-14');
INSERT INTO fuel_prices VALUES (22, 'Fujairah', 'VLSFO', 541, '2024-01-05');
INSERT INTO fuel_prices VALUES (23, 'Hamburg', 'IFO380', 625, '2024-01-20');
INSERT INTO fuel_prices VALUES (24, 'Los Angeles', 'VLSFO', 456, '2024-02-05');
INSERT INTO fuel_prices VALUES (25, 'Shanghai', 'IFO380', 565, '2024-01-17');
INSERT INTO fuel_prices VALUES (26, 'Los Angeles', 'MGO', 643, '2024-01-27');
INSERT INTO fuel_prices VALUES (27, 'Hamburg', 'IFO380', 577, '2024-03-13');
INSERT INTO fuel_prices VALUES (28, 'Singapore', 'IFO380', 561, '2024-03-11');
INSERT INTO fuel_prices VALUES (29, 'Fujairah', 'VLSFO', 598, '2024-02-01');
INSERT INTO fuel_prices VALUES (30, 'Shanghai', 'VLSFO', 522, '2024-02-11');
INSERT INTO fuel_prices VALUES (31, 'Fujairah', 'VLSFO', 625, '2024-02-08');
INSERT INTO fuel_prices VALUES (32, 'Hamburg', 'VLSFO', 521, '2024-02-18');
INSERT INTO fuel_prices VALUES (33, 'Busan', 'VLSFO', 620, '2024-02-06');
INSERT INTO fuel_prices VALUES (34, 'Fujairah', 'IFO380', 517, '2024-02-23');
INSERT INTO fuel_prices VALUES (35, 'Hamburg', 'MGO', 555, '2024-03-25');
INSERT INTO fuel_prices VALUES (36, 'Hamburg', 'IFO380', 538, '2024-01-17');
INSERT INTO fuel_prices VALUES (37, 'Rotterdam', 'MGO', 528, '2024-02-02');
INSERT INTO fuel_prices VALUES (38, 'Singapore', 'MGO', 588, '2024-03-21');
INSERT INTO fuel_prices VALUES (39, 'Singapore', 'IFO380', 563, '2024-02-01');
INSERT INTO fuel_prices VALUES (40, 'Shanghai', 'MGO', 507, '2024-01-31');
INSERT INTO fuel_prices VALUES (41, 'Rotterdam', 'MGO', 548, '2024-03-06');
INSERT INTO fuel_prices VALUES (42, 'Singapore', 'VLSFO', 551, '2024-02-16');
INSERT INTO fuel_prices VALUES (43, 'Shanghai', 'IFO380', 574, '2024-03-05');
INSERT INTO fuel_prices VALUES (44, 'Fujairah', 'VLSFO', 563, '2024-02-03');
INSERT INTO fuel_prices VALUES (45, 'Singapore', 'IFO380', 622, '2024-02-09');
INSERT INTO fuel_prices VALUES (46, 'Antwerp', 'MGO', 519, '2024-03-15');
INSERT INTO fuel_prices VALUES (47, 'Rotterdam', 'VLSFO', 463, '2024-01-23');
INSERT INTO fuel_prices VALUES (48, 'Busan', 'MGO', 553, '2024-03-24');
INSERT INTO fuel_prices VALUES (49, 'Singapore', 'VLSFO', 461, '2024-01-08');
INSERT INTO fuel_prices VALUES (50, 'Fujairah', 'VLSFO', 623, '2024-03-17');
INSERT INTO fuel_prices VALUES (51, 'Los Angeles', 'IFO380', 564, '2024-01-08');
INSERT INTO fuel_prices VALUES (52, 'Rotterdam', 'IFO380', 528, '2024-02-16');
INSERT INTO fuel_prices VALUES (53, 'Rotterdam', 'IFO380', 614, '2024-03-22');
INSERT INTO fuel_prices VALUES (54, 'Antwerp', 'MGO', 620, '2024-02-27');
INSERT INTO fuel_prices VALUES (55, 'Rotterdam', 'VLSFO', 557, '2024-01-15');
INSERT INTO fuel_prices VALUES (56, 'Rotterdam', 'IFO380', 626, '2024-02-20');
INSERT INTO fuel_prices VALUES (57, 'Busan', 'MGO', 484, '2024-01-25');
INSERT INTO fuel_prices VALUES (58, 'Rotterdam', 'MGO', 520, '2024-01-16');
INSERT INTO fuel_prices VALUES (59, 'Busan', 'VLSFO', 511, '2024-03-07');
INSERT INTO fuel_prices VALUES (60, 'Fujairah', 'VLSFO', 575, '2024-01-08');
INSERT INTO fuel_prices VALUES (61, 'Hamburg', 'VLSFO', 453, '2024-01-27');
INSERT INTO fuel_prices VALUES (62, 'Singapore', 'VLSFO', 498, '2024-03-20');
INSERT INTO fuel_prices VALUES (63, 'Fujairah', 'MGO', 554, '2024-01-18');
INSERT INTO fuel_prices VALUES (64, 'Rotterdam', 'IFO380', 512, '2024-03-29');
INSERT INTO fuel_prices VALUES (65, 'Hamburg', 'MGO', 526, '2024-02-24');
INSERT INTO fuel_prices VALUES (66, 'Antwerp', 'VLSFO', 582, '2024-01-25');
INSERT INTO fuel_prices VALUES (67, 'Fujairah', 'IFO380', 590, '2024-01-01');
INSERT INTO fuel_prices VALUES (68, 'Busan', 'VLSFO', 574, '2024-02-09');
INSERT INTO fuel_prices VALUES (69, 'Antwerp', 'MGO', 558, '2024-02-02');
INSERT INTO fuel_prices VALUES (70, 'Antwerp', 'VLSFO', 585, '2024-03-18');
INSERT INTO fuel_prices VALUES (71, 'Los Angeles', 'IFO380', 456, '2024-03-14');
INSERT INTO fuel_prices VALUES (72, 'Los Angeles', 'VLSFO', 587, '2024-03-02');
INSERT INTO fuel_prices VALUES (73, 'Rotterdam', 'MGO', 571, '2024-03-06');
INSERT INTO fuel_prices VALUES (74, 'Singapore', 'VLSFO', 503, '2024-02-13');
INSERT INTO fuel_prices VALUES (75, 'Hamburg', 'IFO380', 521, '2024-01-18');
INSERT INTO fuel_prices VALUES (76, 'Rotterdam', 'VLSFO', 576, '2024-01-20');
INSERT INTO fuel_prices VALUES (77, 'Antwerp', 'MGO', 588, '2024-03-25');
INSERT INTO fuel_prices VALUES (78, 'Singapore', 'VLSFO', 597, '2024-02-10');
INSERT INTO fuel_prices VALUES (79, 'Hamburg', 'VLSFO', 506, '2024-01-15');
INSERT INTO fuel_prices VALUES (80, 'Los Angeles', 'MGO', 550, '2024-01-29');
INSERT INTO fuel_prices VALUES (81, 'Rotterdam', 'IFO380', 453, '2024-02-01');
INSERT INTO fuel_prices VALUES (82, 'Busan', 'IFO380', 555, '2024-02-06');
INSERT INTO fuel_prices VALUES (83, 'Los Angeles', 'VLSFO', 544, '2024-01-10');
INSERT INTO fuel_prices VALUES (84, 'Hamburg', 'VLSFO', 622, '2024-03-29');
INSERT INTO fuel_prices VALUES (85, 'Los Angeles', 'VLSFO', 491, '2024-03-26');
INSERT INTO fuel_prices VALUES (86, 'Hamburg', 'MGO', 521, '2024-01-03');
INSERT INTO fuel_prices VALUES (87, 'Singapore', 'VLSFO', 613, '2024-03-21');
INSERT INTO fuel_prices VALUES (88, 'Antwerp', 'IFO380', 534, '2024-02-14');
INSERT INTO fuel_prices VALUES (89, 'Hamburg', 'MGO', 582, '2024-01-08');
INSERT INTO fuel_prices VALUES (90, 'Antwerp', 'MGO', 466, '2024-03-29');
INSERT INTO fuel_prices VALUES (91, 'Rotterdam', 'VLSFO', 524, '2024-03-06');
INSERT INTO fuel_prices VALUES (92, 'Busan', 'IFO380', 587, '2024-03-02');
INSERT INTO fuel_prices VALUES (93, 'Singapore', 'MGO', 639, '2024-03-14');
INSERT INTO fuel_prices VALUES (94, 'Rotterdam', 'MGO', 572, '2024-01-23');
INSERT INTO fuel_prices VALUES (95, 'Singapore', 'VLSFO', 453, '2024-02-22');
INSERT INTO fuel_prices VALUES (96, 'Hamburg', 'VLSFO', 588, '2024-02-14');
INSERT INTO fuel_prices VALUES (97, 'Los Angeles', 'MGO', 592, '2024-01-28');
INSERT INTO fuel_prices VALUES (98, 'Shanghai', 'VLSFO', 506, '2024-01-07');
INSERT INTO fuel_prices VALUES (99, 'Antwerp', 'MGO', 518, '2024-02-06');
INSERT INTO fuel_prices VALUES (100, 'Hamburg', 'MGO', 611, '2024-01-11');