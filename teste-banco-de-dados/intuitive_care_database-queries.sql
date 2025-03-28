create database intuitive_care;

use intuitite_care;

CREATE TABLE registro_operadoras (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(50),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(50),
    Fax VARCHAR(50),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao VARCHAR(100),
    Data_Registro_ANS DATE
);

CREATE TABLE demonstracoes_contabeis (
    DATA DATE NOT NULL,
    REG_ANS INT NOT NULL,
    CD_CONTA_CONTABIL VARCHAR(50) NOT NULL,
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15, 2),
    VL_SALDO_FINAL DECIMAL(15, 2),
    PRIMARY KEY (DATA, REG_ANS, CD_CONTA_CONTABIL)
);

-- 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre
SELECT 
    r.Registro_ANS,
    r.Razao_Social,
    SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS Despesa
FROM demonstracoes_contabeis dc
JOIN registro_operadoras r 
    ON dc.REG_ANS = r.Registro_ANS
WHERE dc.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
  AND dc.DATA BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY r.Registro_ANS, r.Razao_Social
ORDER BY Despesa DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano

SELECT 
    r.Registro_ANS,
    r.Razao_Social,
    SUM(dc.VL_SALDO_FINAL - dc.VL_SALDO_INICIAL) AS Despesa
FROM demonstracoes_contabeis dc
JOIN registro_operadoras r 
    ON dc.REG_ANS = r.Registro_ANS
WHERE dc.DESCRICAO LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
  AND dc.DATA BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY r.Registro_ANS, r.Razao_Social
ORDER BY Despesa DESC
LIMIT 10;
