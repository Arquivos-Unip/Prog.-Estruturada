import { Sequelize } from "sequelize";

const registro = 2;
const autor = "pedro";
const titulo = "livro";
const editora = "editora";
const ano = "2022";
const quantidade = 2;
const valor = 250;

const produto = Sequelize.define("produtos", {
  registro,
  autor,
  titulo,
  editora,
  ano,
  quantidade,
  valor,
});

