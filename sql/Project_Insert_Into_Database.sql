#3a
INSERT INTO Airline
VALUES("China Eastern");

#3b
INSERT INTO Airport
VALUES(
    "JFK",
    "John F. Kennedy International Airport",
    "New York"
);

INSERT INTO Airport
VALUES(
    "PVG",
    "Shanghai Pudong International Airport",
    "Shanghai"
);

#3C
INSERT INTO Customer
VALUES(
    "triet.vo@nyu.edu",
    "123123",
    "Triet Vo",
    "123",
    "MetroTech Street",
    "NYC",
    "NY",
    "123-456-7890",
    "3212",
    "2025-01-01",
    "US",
    "2000-01-01"
);

INSERT INTO Customer
VALUES(
    "triet.triet@gmail.com",
    "123321",
    "Tree Vo",
    "321",
    "MetroTech Park",
    "NYC",
    "NY",
    "321-654-0987",
    "2123",
    "2026-01-01",
    "US",
    "1999-01-01"
);

INSERT INTO Customer
VALUES(
    "tree@gmail.com",
    "321123",
    "Tree Tree",
    "212",
    "Jay Street",
    "NYC",
    "NY",
    "123-123-1234",
    "2222",
    "2027-01-01",
    "US",
    "1998-01-01"
);

#3d
INSERT INTO Airplane
VALUES("China Eastern", "1234", 500);

INSERT INTO Airplane
VALUES("China Eastern", "4321", 600);

INSERT INTO Airplane
VALUES("China Eastern", "3213", 700);

#3e
INSERT INTO AirlineStaff
VALUES(
    "GreenTrees",
    "treetreetree",
    "China Eastern",
    "Tree",
    "Vo",
    "1997-01-01"
);

#3f
INSERT INTO Flight
VALUES(
    "China Eastern",
    "98765",
    "2021-11-13 20:00:00",
    "PVG",
    "2021-11-14 11:00:00",
    "JFK",
    1500.00,
    "1234",
    "China Eastern",
    "Delayed"
);

INSERT INTO Flight
VALUES(
    "China Eastern",
    "38419",
    "2021-11-12 05:30:00",
    "JFK",
    "2021-11-12 20:45:00",
    "PVG",
    1050.00,
    "3213",
    "China Eastern",
    "Delayed"
);

INSERT INTO Flight
VALUES(
    "China Eastern",
    "45678",
    "2021-11-12 23:45:00",
    "JFK",
    "2021-11-13 14:45:00",
    "PVG",
    1350.00,
    "4321",
    "China Eastern",
    "On-Time"
);

#3g
INSERT INTO Ticket
VALUES(
    "1600203940",
    1450.00,
    "China Eastern",
    "98765",
    "2021-11-13 20:00:00",
    "Credit",
    "0123456789012345",
    "Triet Vo",
    "2025-05-05"
);

INSERT INTO Ticket
VALUES(
    "5930185231",
    1150.00,
    "China Eastern",
    "38419",
    "2021-11-12 05:30:00",
    "Debit",
    "5432109876543210",
    "Tree Vo",
    "2024-10-25"
);

INSERT INTO Ticket
VALUES(
    "6370182746",
    1500.00,
    "China Eastern",
    "45678",
    "2021-11-12 23:45:00",
    "Credit",
    "2345678190347052",
    "Tree Tree",
    "2025-08-30"
);

INSERT INTO Purchases
VALUES(
    "triet.vo@nyu.edu",
    "1600203940",
    "2021-10-07 23:56:21"
);

INSERT INTO Purchases
VALUES(
    "triet.triet@gmail.com",
    "5930185231",
    "2021-08-07 15:12:30"
);

INSERT INTO Purchases
VALUES(
    "tree@gmail.com",
    "6370182746",
    "2021-11-06 00:32:15"
);