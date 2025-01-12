CREATE TABLE Building (
  build_floor_id INTEGER PRIMARY KEY AUTOINCREMENT,
  floor_no INT NOT NULL
);

CREATE TABLE Person (
  person_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  contact VARCHAR(15),
  destination INT
);

CREATE TABLE Lift (
  lift_id INTEGER PRIMARY KEY AUTOINCREMENT,
  capacity INT NOT NULL,
  current_floor INT NOT NULL
);

CREATE TABLE Person_Building (
  person_build_id INTEGER PRIMARY KEY AUTOINCREMENT,
  person_id INT NOT NULL,
  build_floor_id INT NOT NULL,
  FOREIGN KEY (person_id) REFERENCES Person(person_id),
  FOREIGN KEY (build_floor_id) REFERENCES Building(build_floor_id)
);

CREATE TABLE Lift_Building (
  lift_build_id INTEGER PRIMARY KEY AUTOINCREMENT,
  lift_id INT NOT NULL,
  build_floor_id INT NOT NULL,
  status VARCHAR(20) NOT NULL,
  FOREIGN KEY (lift_id) REFERENCES Lift(lift_id),
  FOREIGN KEY (build_floor_id) REFERENCES Building(build_floor_id)
);

CREATE TABLE Person_Lift (
  person_lift_id INTEGER PRIMARY KEY AUTOINCREMENT,
  lift_id INT NOT NULL,
  person_id INT NOT NULL,
  start_floor INT NOT NULL,
  end_floor INT NOT NULL,
  FOREIGN KEY (lift_id) REFERENCES Lift(lift_id),
  FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

INSERT INTO Building (floor_no) VALUES (1), (2), (3), (4), (5);

INSERT INTO Person (name, contact, destination) 
VALUES 
('pradeep', '1234567890', 1),
('abhishek', '9876543210', 5),
('arjun', '4567891230', 2),
('moiz', '7891234560', 4),
('parth', '3216549870', 3);

INSERT INTO Lift (capacity, current_floor)
VALUES 
(10, 1),
(8, 3),
(15, 2),
(12, 4),
(6, 5);

INSERT INTO Person_Building (person_id, build_floor_id)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO Lift_Building (lift_id, build_floor_id, status)
VALUES 
(1, 1, 'active'),
(2, 2, 'active'),
(3, 3, 'inactive'),
(4, 4, 'active'),
(5, 5, 'maintenance');

INSERT INTO Person_Lift (lift_id, person_id, start_floor, end_floor)
VALUES 
(1, 1, 1, 1),
(2, 2, 3, 5),
(3, 3, 2, 2),
(4, 4, 4, 3),
(5, 5, 5, 4);
