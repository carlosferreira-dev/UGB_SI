-- script_db.sql
CREATE TABLE paciente (
    pac_mat INTEGER PRIMARY KEY AUTOINCREMENT,
    pac_nome TEXT NOT NULL,
    pac_mes_aniv INTEGER CHECK (pac_mes_aniv BETWEEN 1 AND 12),
    pac_genero TEXT CHECK (pac_genero IN ('M', 'F'))
);

CREATE TABLE especialidade (
    esp_cod INTEGER PRIMARY KEY AUTOINCREMENT,
    esp_nome TEXT NOT NULL
);

CREATE TABLE medico (
    med_crm INTEGER PRIMARY KEY,
    med_nome TEXT NOT NULL
);

CREATE TABLE laboratorio (
    lab_cod INTEGER PRIMARY KEY AUTOINCREMENT,
    lab_nome TEXT NOT NULL
);

CREATE TABLE consulta (
    con_num INTEGER PRIMARY KEY AUTOINCREMENT,
    con_data TEXT NOT NULL,
    con_hora TEXT NOT NULL,
    con_num_sala INTEGER NOT NULL,
    con_situac TEXT CHECK (con_situac IN ('A', 'R', 'C')),
    pac_mat INTEGER NOT NULL,
    med_crm INTEGER NOT NULL,
    FOREIGN KEY (pac_mat) REFERENCES paciente(pac_mat),
    FOREIGN KEY (med_crm) REFERENCES medico(med_crm)
);

CREATE TABLE medicamento (
    mdc_cod INTEGER PRIMARY KEY AUTOINCREMENT,
    mdc_nome TEXT NOT NULL,
    lab_cod INTEGER NOT NULL,
    FOREIGN KEY (lab_cod) REFERENCES laboratorio(lab_cod)
);

CREATE TABLE sintoma (
    sin_cod INTEGER PRIMARY KEY AUTOINCREMENT,
    sin_nome TEXT NOT NULL
);

CREATE TABLE efeito_colateral (
    mdc_cod INTEGER,
    sin_cod INTEGER,
    PRIMARY KEY (mdc_cod, sin_cod),
    FOREIGN KEY (mdc_cod) REFERENCES medicamento(mdc_cod),
    FOREIGN KEY (sin_cod) REFERENCES sintoma(sin_cod)
);

CREATE TABLE receita (
    con_num INTEGER,
    mdc_cod INTEGER,
    rec_quant INTEGER CHECK (rec_quant > 0),
    PRIMARY KEY (con_num, mdc_cod),
    FOREIGN KEY (con_num) REFERENCES consulta(con_num),
    FOREIGN KEY (mdc_cod) REFERENCES medicamento(mdc_cod)
);

CREATE TABLE contra_indicacao (
    pac_mat INTEGER,
    mdc_cod INTEGER,
    PRIMARY KEY (pac_mat, mdc_cod),
    FOREIGN KEY (pac_mat) REFERENCES paciente(pac_mat),
    FOREIGN KEY (mdc_cod) REFERENCES medicamento(mdc_cod)
);

CREATE TABLE formacao (
    med_crm INTEGER,
    esp_cod INTEGER,
    PRIMARY KEY (med_crm, esp_cod),
    FOREIGN KEY (med_crm) REFERENCES medico(med_crm),
    FOREIGN KEY (esp_cod) REFERENCES especialidade(esp_cod)
);

INSERT INTO paciente (pac_nome, pac_mes_aniv, pac_genero)
VALUES ('Joao Luis', 1, 'M'),
       ('Ricardo Almeida', 4, 'M'),
       ('Luis Arantes', 7, 'M'),
       ('Rafael da Silva', 12, 'M'),
       ('Rafael Nogueira', 2, 'M'),
       ('Priscila Dantas', 1, 'F'),
       ('Larissa Durval', 2, 'F');

INSERT INTO especialidade (esp_nome)
VALUES ('Otorrinolaringologia'),
       ('Pediatria'),
       ('Neurologia'),
       ('Ortopedia'),
       ('Cardiologia'),
       ('Dermatologia'),
       ('Psiquiatria'),
       ('Hematologia');

INSERT INTO medico (med_crm, med_nome)
VALUES (203, 'Luisa Garcia'),
       (411, 'Gustavo Souza'),
       (536, 'Thais Rodrigues'),
       (702, 'Paula Lacerda'),
       (987, 'Bruno Santos');

INSERT INTO laboratorio (lab_nome)
VALUES ('EMS Corp'),
       ('Hypera Pharma'),
       ('Achi'),
       ('Bayer'),
       ('Eurofarma'),
       ('Roche');

INSERT INTO consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
VALUES ('2024-02-18', '13:30', 10, 'R', 1, 411),
       ('2024-02-19', '16:30', 18, 'R', 2, 203),
       ('2024-02-22', '14:30', 23, 'C', 3, 702),
       ('2024-02-25', '13:30', 23, 'A', 2, 987),
       ('2024-03-01', '10:30', 11, 'A', 6, 702),
       ('2024-03-09', '08:30', 10, 'A', 1, 411),
       ('2024-03-13', '09:30', 10, 'R', 4, 411),
       ('2024-03-15', '14:30', 11, 'R', 5, 203),
       ('2024-04-10', '10:30', 11, 'R', 3, 203),
       ('2024-04-12', '08:30', 21, 'C', 3, 411),
       ('2024-04-16', '08:30', 10, 'R', 1, 411),
       ('2024-04-22', '09:30', 22, 'R', 5, 987),
       ('2024-04-12', '10:30', 22, 'R', 2, 987),
       ('2024-04-18', '09:30', 10, 'R', 4, 411);

INSERT INTO medicamento (mdc_nome, lab_cod)
VALUES ('Nimesulida', 1),
       ('Prednisolona', 5),
       ('Dipirona', 6),
       ('Amoxil', 3);

INSERT INTO sintoma (sin_nome)
VALUES ('Azia'),
       ('Cefaleia'),
       ('Urticária'),
       ('Febre'),
       ('Hipotensão'),
       ('Sono');

INSERT INTO efeito_colateral (mdc_cod, sin_cod)
VALUES (1, 1),
       (1, 6),
       (1, 4),
       (2, 1),
       (2, 5),
       (3, 2),
       (3, 4),
       (1, 2);

INSERT INTO receita (con_num, mdc_cod, rec_quant)
VALUES (1, 1, 1),
       (2, 1, 3),
       (2, 2, 2),
       (7, 1, 1),
       (7, 2, 4),
       (8, 2, 3),
       (8, 4, 2),
       (9, 1, 1),
       (9, 3, 2),
       (13, 3, 2),
       (14, 2, 2);

INSERT INTO contra_indicacao (pac_mat, mdc_cod)
VALUES (1, 3),
       (1, 1),
       (3, 2),
       (1, 4);

INSERT INTO formacao (med_crm, esp_cod)
VALUES (203, 2),
       (203, 5),
       (411, 1),
       (411, 5),
       (536, 3),
       (702, 7),
       (987, 8);
