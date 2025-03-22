-- tables

create table books(
	book_id SERIAL primary key,
	title VARCHAR(255) not null,
	sub_title VARCHAR(255),
	publication_date DATE not null, 
	publisher VARCHAR(100) not null,
	auth_id INT not null,
	print_length INT,
	ISBN_10 INT,
	ISBN_13 VARCHAR(255),
	foreign key(auth_id) references authors(auth_id)
);


create table authors(
	auth_id SERIAL primary key,
	first_name VARCHAR(50) not null,
	last_name VARCHAR(50) not null,
	bio VARCHAR(255)
);

alter table books add cat_id INT not null;
alter table books add constraint books_cat_id_fk foreign key(cat_id) references categories(cat_id);

create table categories(
	cat_id SERIAL primary key,
	name VARCHAR(255) not null
);

-- insert data Authors
insert into authors(first_name, last_name, bio) values ('Al', 'Stewart', 'Al Sweigart is a software developer and tech book author living in Houston.');
insert into authors(first_name, last_name, bio) values ('Eric', 'Mathes', 'Read a book to discover :)');

insert into authors(first_name, last_name, bio) values 
('Jon', 'Gjengset', 'Something very short about Jon'),
('Tilman', 'M. Davies', 'Something very short about Tilman'),
('Nora', 'Sandler', 'Something very short about Nora'),
('Carol', 'Nicols', 'Carol Nichols is a member of the Rust Crates.io Team and a former member of the Rust Core Team.'),
('Robert', 'C. Martin', 'Robert Cecil Martin (colloquially known as Uncle Bob) is an American software engineer and author.'),
('Villiam', 'E. Shotts', 'About me');


insert into books(title, sub_title, publication_date, publisher, auth_id, print_length, isbn_10, isbn_13, cat_id) values
('Python Crash Course, 3rd Edition', 'A Hands-On, Project-Based Introduction to Programming', '2023-01-10', 'No Strach Press', 2, 552 ,1718502702, '978-1718502703', 1 ),
('Automate the Boring Stuff with Python 2nd Edition', 'Practical Programming for Total Beginners', '2019-11-12', 'No Strach Press', 1, 500, 1593279922, '978-1593279929', 1 ),
('The Big Book of Small Python Projects', '81 Easy Practice Programs', '2021-06-25', 'No Strach Press', 1, 536, 1718501242, '978-1718501249', 1 ),
('The Linux Command Line, 2nd Edition', 'Complete Introduction', '2019-03-07', 'No Strach Press', 8, 480,  1593279523 , '978-1593279523', 4 );


select * from books;

insert into categories('name') values
('Programming'),
('Mathematics'),
('Statistics'),
('Computer Science'),
('Physics'),
('Economics'),
('Electrical Engeneering'),
('Chemistry');

-- queries
select * from authors;

