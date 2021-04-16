-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16-Abr-2021 às 21:10
-- Versão do servidor: 10.4.17-MariaDB
-- versão do PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `llama`
--
CREATE DATABASE IF NOT EXISTS `llama` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `llama`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tabela_teste`
--

DROP TABLE IF EXISTS `tabela_teste`;
CREATE TABLE `tabela_teste` (
  `nome` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `idade` int(11) NOT NULL,
  `altura` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tabela_teste`
--

INSERT INTO `tabela_teste` (`nome`, `id`, `cpf`, `idade`, `altura`) VALUES
('Ana', 21, '01000', 29, 1.89),
('Yuri', 22, '02000', 65, 1.69),
('Flavia', 23, '03000', 22, 1.76),
('Naiane', 25, '05000', 86, 1.67);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `tabela_teste`
--
ALTER TABLE `tabela_teste`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `aqui_un` (`cpf`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tabela_teste`
--
ALTER TABLE `tabela_teste`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
