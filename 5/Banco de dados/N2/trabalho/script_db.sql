create table paciente (
	pac_mat INTEGER PRIMARY KEY AUTOINCREMENT,
	pac_nome varchar(40) not null,
	pac_mes_aniv INTEGER check (pac_mes_aniv between 01 and 12),
	pac_genero varchar(1) check (pac_genero in ('M', 'F')));

create table especialidade (
	esp_cod INTEGER PRIMARY KEY AUTOINCREMENT,
	esp_nome varchar(40) not null);

create table medico (
	med_crm INTEGER PRIMARY KEY,
	med_nome varchar(40) not null);

create table laboratorio (
	lab_cod INTEGER PRIMARY KEY AUTOINCREMENT,
	lab_nome varchar(40) not null);

create table consulta (
	con_num INTEGER PRIMARY KEY AUTOINCREMENT,
	con_data date not null,
	con_hora varchar(5) not null,
	con_num_sala INTEGER not null,
	con_situac varchar(01) check (con_situac in ('A','R','C')),
	pac_mat INTEGER not null,
	med_crm INTEGER not null,
	foreign key (pac_mat) references paciente(pac_mat),
	foreign key (med_crm) references  medico(med_crm));

create table medicamento (
	mdc_cod INTEGER PRIMARY KEY AUTOINCREMENT,
	mdc_nome varchar(40) not null,
	lab_cod INTEGER not null,
	foreign key (lab_cod) references laboratorio(lab_cod));

create table sintoma (
	sin_cod INTEGER PRIMARY KEY AUTOINCREMENT,
	sin_nome varchar(40) not null);

create table efeito_colateral (
	mdc_cod INTEGER,
	sin_cod INTEGER,
	PRIMARY KEY (mdc_cod, sin_cod),
	foreign key (mdc_cod) references medicamento (mdc_cod),
	foreign key (sin_cod) references sINTEGERoma(sin_cod));	

create table receita (
	con_num INTEGER,
	mdc_cod INTEGER,
	rec_quant INTEGER check(rec_quant > 0),
	PRIMARY KEY (con_num, mdc_cod),
	foreign key (con_num) references consulta (con_num),
	foreign key (mdc_cod) references medicamento(mdc_cod) );

create table contra_indicacao(
	pac_mat INTEGER,
	mdc_cod INTEGER,
	PRIMARY KEY (pac_mat, mdc_cod),
	foreign key (pac_mat) references paciente(pac_mat),
	foreign key (mdc_cod) references medicamento(mdc_cod) );

create table formacao (
	med_crm INTEGER,
	esp_cod INTEGER,
	PRIMARY KEY (med_crm, esp_cod),
	foreign key (med_crm) references medico (med_crm),
	foreign key (esp_cod) references especialidade(esp_cod));	


insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Joao Luis', 01, 'M');
insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Ricardo Almeida', 04, 'M');
insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Luis Arantes', 07, 'M');
insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Rafael da Silva', 12, 'M');
insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Rafael Nogueira', 02, 'M');
insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Priscila Dantas', 01, 'F');
insert into paciente (pac_nome, pac_mes_aniv, pac_genero)
values ('Larissa Durval', 02, 'F');

insert into especialidade (esp_nome)
values ('Otorrinolaringologia');
insert into especialidade (esp_nome)
values ('Pediatria');
insert into especialidade (esp_nome)
values ('Neurologia');
insert into especialidade (esp_nome)
values ('Ortopedia');
insert into especialidade (esp_nome)
values ('Cardiologia');
insert into especialidade (esp_nome)
values ('Dermatologia');
insert into especialidade (esp_nome)
values ('Psiquiatria');
insert into especialidade (esp_nome)
values ('Hematologia');

insert into medico (med_crm, med_nome)
values (203, 'Luisa Garcia');
insert into medico (med_crm, med_nome)
values (411, 'Gustavo Souza');
insert into medico (med_crm, med_nome)
values (536, 'Thais Rodrigues');
insert into medico (med_crm, med_nome)
values (702, 'Paula Lacerda');
insert into medico (med_crm, med_nome)
values (987, 'Bruno Santos');

insert into laboratorio (lab_nome)
values ('EMS Corp');
insert into laboratorio (lab_nome)
values ('Hypera Pharma');
insert into laboratorio (lab_nome)
values ('Ache');
insert into laboratorio (lab_nome)
values ('Bayer');
insert into laboratorio (lab_nome)
values ('Eurofarma');
insert into laboratorio (lab_nome)
values ('Roche');

insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-02-18', '13:30', 10, 'R', 1, 411);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-02-19', '16:30', 18, 'R', 2, 203);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-02-22', '14:30', 23, 'C', 3, 702);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-02-25', '13:30', 23, 'A', 2, 987);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-03-01', '10:30', 11, 'A', 6, 702);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-03-09', '08:30', 10, 'A', 1, 411);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-03-13', '09:30', 10, 'R', 4, 411);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-03-15', '14:30', 11, 'R', 5, 203);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-04-10', '10:30', 11, 'R', 3, 203);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-04-12', '08:30', 21, 'C', 3, 411);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-04-16', '08:30', 10, 'R', 1, 411);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-04-22', '09:30', 22, 'R', 05, 987);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-04-12', '10:30', 22, 'R', 2, 987);
insert into consulta (con_data, con_hora, con_num_sala, con_situac, pac_mat, med_crm)
values ('2024-04-18', '09:30', 10, 'R', 4, 411);

insert into medicamento (mdc_nome, lab_cod)
values ('Nimesulida', 1);
insert into medicamento (mdc_nome, lab_cod)
values ('Prednisolona', 5);
insert into medicamento (mdc_nome, lab_cod)
values ('Dipirona', 6);
insert into medicamento (mdc_nome, lab_cod)
values ('Amoxil', 3);

insert into sintoma (sin_nome)
values ('Azia');
insert into sintoma (sin_nome)
values ('Cefaleia');
insert into sintoma (sin_nome)
values ('Urticaria');
insert into sintoma (sin_nome)
values ('Febre');
insert into sintoma (sin_nome)
values ('Hipotensao');
insert into sintoma (sin_nome)
values ('Sono');
insert into sintoma (sin_nome)
values ('Gastrite');

insert into efeito_colateral (mdc_cod,sin_cod)
values (1, 1);
insert into efeito_colateral (mdc_cod,sin_cod)
values (1, 6);
insert into efeito_colateral (mdc_cod,sin_cod)
values (1, 4);
insert into efeito_colateral (mdc_cod,sin_cod)
values (2, 1);
insert into efeito_colateral (mdc_cod,sin_cod)
values (2, 5);
insert into efeito_colateral (mdc_cod,sin_cod)
values (3, 2);
insert into efeito_colateral (mdc_cod,sin_cod)
values (3, 4);
insert into efeito_colateral (mdc_cod,sin_cod)
values (1, 2);
insert into efeito_colateral (mdc_cod,sin_cod)
values (3, 7);
insert into efeito_colateral (mdc_cod,sin_cod)
values (3, 1);

insert into receita (con_num, mdc_cod, rec_quant)
values (1, 1, 1);
insert into receita (con_num, mdc_cod, rec_quant)
values (2, 1, 3);
insert into receita (con_num, mdc_cod, rec_quant)
values (2, 2, 2);
insert into receita (con_num, mdc_cod, rec_quant)
values (7, 1, 1);
insert into receita (con_num, mdc_cod, rec_quant)
values (7, 2, 4);
insert into receita (con_num, mdc_cod, rec_quant)
values (8, 2, 3);
insert into receita (con_num, mdc_cod, rec_quant)
values (8, 4, 2);
insert into receita (con_num, mdc_cod, rec_quant)
values (9, 1, 1);
insert into receita (con_num, mdc_cod, rec_quant)
values (9, 3, 2);
insert into receita (con_num, mdc_cod, rec_quant)
values (13, 3, 2);
insert into receita (con_num, mdc_cod, rec_quant)
values (14, 2, 2);

insert into contra_indicacao (pac_mat, mdc_cod)
values (1, 3);
insert into contra_indicacao (pac_mat, mdc_cod)
values (1, 1);
insert into contra_indicacao (pac_mat, mdc_cod)
values (3, 2);
insert into contra_indicacao (pac_mat, mdc_cod)
values (1, 4);

insert into formacao (med_crm, esp_cod)
values (203, 2);
insert into formacao (med_crm, esp_cod)
values (203, 5);
insert into formacao (med_crm, esp_cod)
values (411, 1);
insert into formacao (med_crm, esp_cod)
values (411, 5);
insert into formacao (med_crm, esp_cod)
values (536, 3);
insert into formacao (med_crm, esp_cod)
values (702, 7);
insert into formacao (med_crm, esp_cod)
values (987, 8);