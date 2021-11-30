CREATE TABLE Airline(
    name VARCHAR(50),
    PRIMARY KEY(name)
); 

CREATE TABLE AirlineStaff(
    username VARCHAR(20),
    password VARCHAR(300) NOT NULL,
    airline VARCHAR(50),
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    date_of_birth DATE NOT NULL,
    PRIMARY KEY(username),
    FOREIGN KEY(airline) REFERENCES Airline(name)
); 

CREATE TABLE StaffPhoneNumbers(
    username VARCHAR(20),
    phone_number VARCHAR(20),
    PRIMARY KEY(username, phone_number),
    FOREIGN KEY(username) REFERENCES AirlineStaff(username)
); 

CREATE TABLE Airport(
    code VARCHAR(3),
    name VARCHAR(25) NOT NULL,
    city VARCHAR(20) NOT NULL,
    PRIMARY KEY(code)
); 

CREATE TABLE Airplane(
    airline VARCHAR(50),
    ID VARCHAR(8),
    num_seats NUMERIC(5, 0) NOT NULL,
    PRIMARY KEY(airline, ID),
    FOREIGN KEY(airline) REFERENCES Airline(name)
); 

CREATE TABLE Flight(
    airline_name VARCHAR(50),
    flight_num VARCHAR(5),
    depart_datetime DATETIME,
    depart_airport VARCHAR(3) NOT NULL,
    arrival_datetime DATETIME NOT NULL,
    arrival_airport VARCHAR(3) NOT NULL,
    base_price NUMERIC(6, 2) NOT NULL,
    airplane_ID VARCHAR(8) NOT NULL,
    airplane_airline_name VARCHAR(50) NOT NULL,
    status VARCHAR(20),
        PRIMARY KEY(
            airline_name,
            flight_num,
            depart_datetime
        ),
        FOREIGN KEY(airline_name) REFERENCES Airline(name),
        FOREIGN KEY(
            airplane_airline_name,
            airplane_ID
        ) REFERENCES Airplane(airline,ID)
);

CREATE TABLE Customer(
    email VARCHAR(50),
    password VARCHAR(300) NOT NULL,
    name VARCHAR(20) NOT NULL,
    add_building_num VARCHAR(10) NOT NULL,
    add_street VARCHAR(100) NOT NULL,
    add_city VARCHAR(30) NOT NULL,
    add_state VARCHAR(30) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    passport_num VARCHAR(20) NOT NULL,
    passport_expiration DATE NOT NULL,
    passport_country VARCHAR(20) NOT NULL,
    date_of_birth DATE NOT NULL,
    PRIMARY KEY(email)
); 

CREATE TABLE Takes(
    cust_email VARCHAR(50),
    flight_airline VARCHAR(50),
    flight_num VARCHAR(5),
    flight_depart_datetime DATETIME,
    comment VARCHAR(250),
    rating NUMERIC(3, 0),
    PRIMARY KEY(
        cust_email,
        flight_airline,
        flight_num,
        flight_depart_datetime
    ),
    FOREIGN KEY(
        flight_airline,
        flight_num,
        flight_depart_datetime
    ) REFERENCES Flight(
        airline_name,
        flight_num,
        depart_datetime
    ),
    FOREIGN KEY(cust_email) REFERENCES Customer(email)
); 

CREATE TABLE Ticket(
    ID VARCHAR(50),
    sold_price NUMERIC(6, 2) NOT NULL,
    airline VARCHAR(50),
    flight_num VARCHAR(5),
    depart_datetime DATETIME,
    pay_card_type VARCHAR(10) NOT NULL,
    pay_card_num VARCHAR(16) NOT NULL,
    pay_name_on_card VARCHAR(20) NOT NULL,
    pay_card_expiration DATE NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY(
        airline,
        flight_num,
        depart_datetime
    ) REFERENCES Flight(
        airline_name,
        flight_num,
        depart_datetime
    )
); 

CREATE TABLE Purchases(
    cust_email VARCHAR(50),
    t_ID VARCHAR(50),
    date_time DATETIME NOT NULL,
    PRIMARY KEY(cust_email, t_ID),
    FOREIGN KEY(cust_email) REFERENCES Customer(email),
    FOREIGN KEY(t_ID) REFERENCES Ticket(ID)
);