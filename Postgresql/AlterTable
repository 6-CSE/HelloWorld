CREATE TABLE tbl_generos (
ID_Genero Tinyint IDENTITY,
Genero VARCHAR(25)
CONSTRAINT pk_id_genero PRIMARY KEY (ID_Genero)
);

ALTER TABLE tbl_livros
ADD ID_Genero Tinyint
CONSTRAINT fk_id_genero FOREIGN KEY (ID_Genero)
REFERENCES tbl_generos (ID_Genero) ON DELETE CASCADE;

INSERT INTO tbl_generos (Genero) VALUES ('Ficção');


INSERT INTO tbl_Livros (Nome_Livro, ISBN, Data_Pub,
Preco_Livro, ID_Autor, ID_editora, ID_Genero)
VALUES
('As Aventuras de Robinson Crusoé','98653696912','18700509', 32.50, 6, 10,3);

SELECT * FROM tbl_livros;
