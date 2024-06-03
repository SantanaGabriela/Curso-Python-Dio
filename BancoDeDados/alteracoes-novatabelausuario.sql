INSERT INTO usuarios_nova
SELECT * from usuarios;

-- Excluindo tabela anterior --
DROP table usuarios;

-- Renomeando nova tabela --
ALTER TABLE usuarios_nova RENAME usuarios;


-- Ou opção 2 : Alterar tamanho da coluna endereço -- 
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(100);